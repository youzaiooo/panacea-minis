# Panacea Personal Health Wiki Schema

## Purpose

This dedicated Wiki supports the user's longitudinal health management. It is
maintained by Panacea on this device and holds only this user's health records
and source materials. It is the single source of truth for health data — do not
create parallel copies elsewhere.

## Domains

- `health-management`: meals, nutrition, physical activity, sleep, measurements, and behavior change.
- `modern-medicine`: laboratory trends, medicines, symptoms, clinician instructions, evidence-based medical education, and safety follow-up.

## Structure

- `SCHEMA.md`: this file — structure conventions and maintenance rules.
- `index.md`: the content catalog; every page appears here with a one-line summary.
- `log.md`: the action log, **reverse-chronological**; every create/update/correction is recorded here (newest first, right after the header block).
- `profile.md`: user-approved identity basics, goals, allergies, diagnoses, and clinician constraints.
- `nutrition-goals.md`: nutrition targets supplied by the user or clinician (never prefill).
- `dietary-profile.md`: durable dietary preferences and confirmed long-term patterns.
- `records/daily/`: per-day cumulative intake summaries (versioned).
- `records/meals/`: dated meal records and Panacea's practical assessment.
- `records/measurements/`: weight / circumference measurements.
- `records/labs/`: dated laboratory values and report summaries.
- `records/symptoms/`: dated symptom timeline entries.
- `records/medications/`: medicine name, dose as reported, start/stop history, and clinician instructions.
- `raw/reports/` and `raw/images/`: user-provided report and image originals.
- `raw/sources/`: guidelines, papers, labels, and other evidence used for durable general knowledge.
- `concepts/`: reusable evidence-based health-management and modern-medicine knowledge.
- `concepts/foods/`: packaged-product and food pages.

## Orientation (do this before any Wiki work)

1. Read `SCHEMA.md` (this file), `profile.md`, the relevant part of `index.md`, and the newest `log.md` entries.
2. Search the Wiki for the topic before creating anything new.
3. Only then write records or answer from the Wiki.

## Retention And Privacy

- The user authorizes Panacea to retain relevant personal health information supplied for longitudinal analysis unless the user says not to record a specific item.
- Record facts with dates and provenance. Clearly distinguish user report, report transcription, image observation, and Panacea interpretation.
- Do not invent missing values, diagnoses, adherence, or medical events. Keep uncertainty explicit.
- The user may request viewing, correction, deletion, export, or a recording pause at any time.
- Never copy this content outside this Wiki (no external services, no other agents, no public material).

## Evidence And Safety

- General medical knowledge must follow Panacea's evidence hierarchy: current guidelines, systematic reviews, peer-reviewed primary research, medicine regulators, then medical textbooks.
- Do not use traditional Chinese medicine, public encyclopedias, self-media, marketing material, or generic popular-science pages as medical evidence.
- This Wiki supports education and longitudinal context, not diagnosis, prescribing, emergency triage, or independent medicine changes.

## Conventions

- Use lowercase, hyphenated filenames. Prefix record filenames with `YYYY-MM-DD-`.
- Every factual record carries date, source type, and confidence or uncertainty when relevant.
- `log.md` is reverse-chronological: insert new entries right after the header block, above the previous latest entry. Format: `## [YYYY-MM-DD HH:MM] event | summary`.
- Keep `index.md` current: add every new page under its section with a one-line summary, and update the header `Last updated` / `Total pages`.
- Page count = number of `.md` files under the Wiki tree excluding `raw/` and the three infrastructure files (`index.md`, `log.md`, `SCHEMA.md`). Count files; never estimate.
- New reusable concepts need sources under `raw/sources/`, evidence citations, and meaningful wikilinks where related pages exist.
