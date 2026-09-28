#!/usr/bin/env python3
"""Verify a markdown-Wiki write set: file existence + wikilink resolution + page/product counts.

Usage:
    python3 verify_wiki_writes.py                      # 8 most recently modified pages
    python3 verify_wiki_writes.py <path> [<path> ...]  # only these files (relative to WIKI or absolute)
    python3 verify_wiki_writes.py --all                # every page under records/ and concepts/

Checks:
  1. Each target file exists.
  2. Each [[wikilink]] resolves to a .md inside the Wiki; a link that ends in `.md` is reported as a
     convention violation (wiki links carry no extension).
  3. Page count = .md files excluding raw/ and index.md/log.md/SCHEMA.md (one fixed formula for the
     whole Wiki); product count = concepts/foods/*.md.

Exit code: 0 when clean, 1 when a file is missing or a link is unresolved.
WIKI root = $WIKI_PATH, default /var/minis/memory/panacea-wiki.
"""

import glob
import os
import re
import sys

WIKI = os.environ.get("WIKI_PATH") or os.path.expanduser("/var/minis/memory/panacea-wiki")
INFRA = {"index.md", "log.md", "SCHEMA.md"}
LINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\\?\|[^\]]*)?\]\]")


def _norm(path):
    path = path.strip()
    return path[2:] if path.startswith("./") else path


def count_pages():
    total = 0
    for root, _dirs, files in os.walk(WIKI):
        rel = os.path.relpath(root, WIKI)
        if "raw" in rel.split(os.sep):
            continue
        for name in files:
            if name.endswith(".md") and name not in INFRA:
                total += 1
    return total


def _md_under(sub):
    out = []
    for root, _dirs, files in os.walk(os.path.join(WIKI, sub)):
        for name in files:
            if name.endswith(".md"):
                full = os.path.join(root, name)
                out.append((os.path.getmtime(full), os.path.relpath(full, WIKI)))
    return out


def default_files(limit=8):
    candidates = _md_under("records") + _md_under("concepts")
    candidates.sort(reverse=True)
    return [rel for _mtime, rel in candidates[:limit]]


def all_files():
    return sorted(rel for _mtime, rel in _md_under("records") + _md_under("concepts"))


def main(argv):
    if not os.path.isdir(WIKI):
        print("WIKI root does not exist:", WIKI)
        return 1
    explicit = [a for a in argv if not a.startswith("--")]
    if "--all" in argv:
        targets = all_files()
    elif explicit:
        targets = [_norm(a) for a in explicit]
    else:
        targets = default_files()

    missing, unresolved, bad_suffix, checked = [], [], [], 0
    for rel in targets:
        path = rel if os.path.isabs(rel) else os.path.join(WIKI, rel)
        if not os.path.isfile(path):
            missing.append(rel)
            continue
        checked += 1
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for raw in LINK_RE.findall(text):
            target = raw.strip()
            if not target or target.startswith("#"):
                continue
            if target.endswith(".md"):
                bad_suffix.append((rel, target))
                candidate = target
            else:
                candidate = target + ".md"
            if not os.path.isfile(os.path.join(WIKI, _norm(candidate))):
                unresolved.append((rel, target))

    print("WIKI =", WIKI)
    print("checked pages =", checked, "/", len(targets))
    print("page count (fixed formula) =", count_pages())
    print("product count (concepts/foods) =",
          len(glob.glob(os.path.join(WIKI, "concepts", "foods", "*.md"))))
    print("missing files:", missing or "none")
    print("unresolved wikilinks:", unresolved or "none")
    if bad_suffix:
        print("WARNING: wikilinks with .md suffix (drop the suffix):")
        for rel, target in bad_suffix:
            print("   ", rel, "->", target)
    else:
        print("wikilinks with .md suffix: none")
    return 1 if (missing or unresolved) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
