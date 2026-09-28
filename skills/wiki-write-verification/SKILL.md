---
name: wiki-write-verification
description: >
  健康档案写盘核对：证明一批写入已落盘且未被静默截断，校验链接、计数、表格行与复用数字。
  报告"已创建/更新 N 页"之前，或任何向 Wiki 写入完成后加载。
---

# Wiki Write Verification

Use when a task ends by writing or updating pages in a markdown knowledge base (Panacea 私人健康
Wiki at /var/minis/memory/panacea-wiki): **prove the write set landed and stayed
consistent** — links, counts, table rows, and reused derived numbers. Domain conventions live in the
Wiki-specific skills; this skill is the mechanical verification layer that is the same for every Wiki
and that no diff summary can do for you. Run it before you report "N pages created/updated".

## Procedure

1. Write the pages/edits (the domain skill governs content and provenance).
2. Run the bundled verifier over the files you touched:
   `python3 scripts/verify_wiki_writes.py <path> [<path> …]` — no args checks the 8 most recently
   modified pages, `--all` checks every page under `records/` and `concepts/`. It prints missing
   files, unresolved wikilinks, `.md`-suffixed links, and the page/product counts. Table links escape
   the pipe as `\|`, so they surface as "unresolved" with a trailing backslash — a pre-existing false
   positive: classify it, don't "fix" it.
3. Sweep the write set for **truncated writes**: read back each file's tail; a dropped tail still reports
   success, and only a read-back shows it. Rewrite any truncated file in chunks before any other check is
   meaningful.
4. Read back every edited region that sits inside a table **or that inserts a line next to an existing
   entry heading** (see the line-edit pitfall below).
5. Recompute dependents of anything you corrected: daily totals, summary lines, index descriptions.
6. Report to the user: files changed, measured counts (from the script's output, never from memory
   or a mental tally), and the 1–3 open questions that would change the numbers.

**A zero search result is a claim about your pattern, not yet about the Wiki.** Before reporting that
an entry, record, or file "does not exist", re-run with a fragment you know is present — the date you
just wrote, a word from the heading you created. Heading formats differ from prose
(`## [YYYY-MM-DD] title` versus `YYYY-MM-DD title`), so a pattern composed from memory returns 0 for a
record sitting right there, and acting on that false "missing" recreates it as a duplicate.

## Page counts and index headers

- **Count files, never grep the index page.** A page's own text mentions the folder names it indexes,
  so `grep -c` over-counts.
- **Fix one counting formula for the whole Wiki and state it in the header**: pages = `*.md` files
  excluding `raw/` and the infrastructure pages (`index.md`, `log.md`, `SCHEMA.md`).
  ```sh
  find "$WIKI" -name '*.md' -not -path '*/raw/*' | grep -vE '/(index|log|SCHEMA)\.md$' | wc -l
  ```
  Proportional tables (products, foods) likewise: `ls concepts/foods/*.md | wc -l`, not index rows.
- **When the convention changes, record both numbers once** in the header and state that historical
  values are not retro-edited — otherwise the next session reads a "wrong" count and re-derives it.
- **After changing a declared count, grep the header line for every occurrence of the old number**: the
  same line usually states the total more than once (the declared total, the inline `find … | wc -l`
  explanation, and the alternate-formula figure). Update them in one pass, then re-read the line — a
  half-updated header contradicts itself and the next session re-derives a "wrong" count from it.
- **Never rewrite historical/append-only entries.** A correction goes in a new entry naming the old
  and the new value; the old entry keeps its original text.
- **A count that moved without your writing anything means a concurrent writer, not your arithmetic.**
  The same Wiki is often maintained from more than one session at once. Enumerate what actually arrived
  and diff against the index rather than re-deriving your own tally:
  `find "$WIKI" -name '*.md' -not -path '*/raw/*' -newermt '<today 00:00>' -printf '%TH:%TM %p\n'`
  (or `-mmin`/`-cmin`). Then set the declared count to the **measured** value and list the new pages in the
  header, distinguishing which ones this round wrote from which ones another session did.
- **Re-read the header line immediately before patching it.** A parallel session can rewrite the same
  line, so an `old_string` read a few tool calls ago fails to match. On a no-match: read the line once,
  retry once with the fresh text; if the failure is because the parallel session already wrote the same
  fact, **skip the patch** — writing it again leaves the same fact stated twice with different wording.

## Line edits: insert on whole lines, then read back

`patch` replaces exactly the text you hand it, so a **line prefix** leaves the rest of that line
orphaned and the write still reports success: inserting a table row off a prefix merges two rows;
inserting a `##` entry heading off a prefix (log and index entry titles are long and carry a `|`
subtitle) leaves a dangling ` | rest of the old title` line with no heading above it. Both look like
clean replacements in the diff. Therefore:

- **Every insertion next to an existing line** — table row, log/index entry heading, list bullet —
  makes `old_string` the **complete** line (including its trailing newline where the tool accepts it)
  and `new_string` that same line plus the new line. Never anchor on a fragment ending mid-line.
- **Read back the exact line range afterwards**: for tables count cells row by row; for entry headings
  confirm every `##` title is whole and that no line starts with the subtitle separator. A diff only
  says "replaced"; it cannot show a merge or an orphan.
- **Repairing an orphan**: read the region, then patch the fragment back into its full heading (or
  delete it) — never leave it as loose prose under the entry.
- **A no-match on text you just copied out of a tool result usually means an extra escape layer,
  not a changed file.** Results arrive JSON-encoded, so a backslash shown as `\\` in the output is a
  single `\` on disk — retyping what you saw reproduces the wrong byte count. Cut `old_string` back to
  a distinctive substring that stops **before** the `[[…\|…]]` (or any backslash-bearing) region; the
  shorter anchor skips the escapes entirely. Escalate to the scripted replace only if that still fails.
- **Very long single-line edits** (an `index.md` count line, a long entry title): if `patch` reports no
  match for text you just read back verbatim, stop re-guessing `old_string`. Switch to a scripted exact
  replace that asserts the match count first, then write and re-verify:
  `n = s.count(old); assert n == 1; s = s.replace(old, new)` followed by a re-read of that line.
- **A script printing its own "OK" has proved only its string surgery, never the write.** Assert the
  write tool's returned payload (`bytes_written` / `verified`) and re-read the target with an
  independent command (`grep`, `cat`, `stat`) before reporting the change: a whole-file rewrite that
  never landed raises nothing, and a read helper that returns paginated content, line-numbered content,
  or a dedup/status dict instead of the body is not byte-faithful input for a write-back — take the raw
  bytes from disk (`open()` / `cat`) when a script rewrites a file.
- **Entries built in a loop must be bracket-balanced per line.** An unclosed `[[` does not raise and
  does not fail link resolution — the entry silently stops being a link, so its target then looks
  *absent from the index* and invites a duplicate page. After bulk-building index/log entries, assert
  `line.count('[[') == line.count(']]')` across the file, alongside the existing target-existence check.

## Reused derived numbers: re-verify the constant first

Copying a derived value from an earlier page ("10 g of X ≈ +Y g of Z") propagates whatever constant
produced it, and a small conversion error compounds across a record series until a comfortable budget
reads as over-limit — a direction-changing error. So:

- Re-derive from the authoritative source constant before reusing it, then archive the value under
  `raw/sources/` when it feeds records (cite the identifier you looked up, not the page you copied).
- Do not carry a ratio across categories: dairy fat, egg, fried dough and poultry skin all differ.
  A ratio is valid only for the matrix it was measured in.
- When one of your own earlier pages is wrong: patch it **in place** with a labelled correction
  (new value + constant/source + the old value quoted once), then **recompute every dependent
  aggregate**. Record the correction in the current log entry; leave historical entries untouched.

## Truncated writes report success — write long pages in chunks

A long write or patch whose argument overruns the budget is **silently truncated**: the tool
returns success, the diff summary looks right, and everything in the dropped tail is gone — usually the one
structural piece nobody thinks to check (e.g. a table's header/separator row, leaving the cells present but
the table rendering as plain prose). No diff and no success message can reveal this.

- **Keep each call's content to roughly 1,200–1,500 characters.** For longer pages write the head first and
  end it with an anchor comment (`<!-- PART2 -->`), then `patch` that anchor into the next chunk, ending with
  `<!-- PART3 -->`, and so on. **Every anchor comment must be gone from the finished file.**
- **Sweep before reporting:** confirm each file's last line is a real sentence, plus a byte count in the
  expected range（写入可能静默截断——成功返回不等于全文落盘）。
- **Then check the structure the tail should have carried**: every new table has a header + separator row;
  every section you intended to write is present.
- Line numbers shift with each edit, so match `old_string` on content fragments (anchors, whole table rows),
  never on a previously-read line number.

## Amendment chains: a record revisited after it was written

A live record is often amended later the same day — the user adds an item to a meal already reported, a
correction arrives, or a standalone item is reported afterwards. Treat it as an amendment chain, not a rewrite:

- **Keep the superseded number visible**: strike the old total row with `~~…~~` and label it "superseded by
  vN". A figure that changed must be traceable to the reason it changed; the log entry for the change goes in
  as a new entry, leaving the previous one's text intact.
- **Version monotonically in every affected page**: the entry itself (`v1 → v2`) and the day/summary page
  (`v4 → v5 → v6`), renaming the previous interpretation block to "vN (retained)" instead of deleting it.
  Several bumps in one day are normal, not a sign something went wrong.
- **The write set for an amendment is bigger than the amended file**: the entry, the day summary, the index
  entry for the entry *and* for the day, the log entry — plus any page counting the number of records. Update
  them in the same round, then re-count.
- **Re-derive the aggregate, never hand-patch it**: recompute the cumulative from every item of the period and
  quote the figure you actually computed — the same number must appear in the table, the summary lines and the
  reply. A mismatch between an enumerated count and a declared total is a hard error, so re-fetch or recompute.
- **When an addendum answers a question you asked about an earlier record, attach it there**; if its timing is
  unstated, say so and note that only the attribution changes, not the period total.
- **An item filed under a day other than the one it was reported on makes the write set span two day
  summaries — verify both, and verify the item appears in exactly one.** Check that the attributed day's
  cumulative includes it and that the reported day's carries an explicit "belongs to <date>, excluded
  from today" note: filed in neither day it is silently lost, in both it is double-counted, and neither
  failure shows up in a single-file read-back.

## Timestamps and "files changed" claims are hard assertions

Live records carry a time, and the entry's own text often enumerates what was updated. Both are
verifiable claims, not narration:

- **Take the timestamp in the same round you write the entry** — run `date` and paste its output. Never
  derive it from an earlier `date` call plus elapsed minutes: host clocks jump (suspend/resume, NTP
  correction, timezone change) and one jump silently misdates every entry written after it. When a bad
  stamp is found, correct it **in place** with the basis named (`stat -c '%y'` of the same batch of files),
  not with a footnote at the end of the log.
- **Land every write before writing the sentence that lists them.** A log/entry line enumerating "updated
  files" must be written after those files are saved, then each path re-checked (`grep` for the new text,
  `stat` for a fresh mtime). If a claim turns out to have preceded the write, do the missing write and mark
  it inside that entry ("补落地 at HH:MM") rather than editing the claim away.
- **Two-phase round makes it true by construction**: (a) all content writes, (b) the log entry, the counts,
  and the reply. Never interleave the claim into phase (a).

## Support files

- `scripts/verify_wiki_writes.py` — stdlib-only checker for link resolution, file existence, page and
  product counts (default `/var/minis/memory/panacea-wiki`).
- `references/derived-number-reuse.md` — failure modes when copying a derived number across pages, the
  verified constants worth reusing (butter SFA, whole-wheat bread), and the labelled-correction
  procedure for a page that used the wrong constant.
