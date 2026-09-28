# USDA FDC API Pitfalls (observed 2026-08-16)

These notes live next to the food-estimation workflow that uses USDA.

## DEMO_KEY rate limit: ~30 requests per HOUR

- Symptom: `HTTP Error 429: Too Many Requests` after roughly 30 API calls
  (searches + details combined), persisting for about an hour even with
  sleeps between retries.
- Mitigation:
  1. Batch ALL searches first, then ALL detail calls (fewer round trips).
  2. When 429 starts, STOP calling. The lookup script saves every response
     to `raw/sources/usda/` — parse the saved JSONs (`usda-fdc-<id>-detail.json`)
     for the nutrients you still need.
  3. Still missing a value for a **Chinese staple** (肉/蛋/豆制品/蔬果)? Route it to
     the CFCT official platform instead of waiting out the window — its POST
     endpoint carries no quota (`chinese-food-composition-sourcing` §1). CFCT is
     生/食部 basis and gives SFA as a % of fat: convert it, label the basis, and
     never place a raw CFCT figure in the same column as cooked USDA values.
  4. Wait for the hourly reset before resuming; then fetch remaining IDs
     one at a time with short pauses.

**A value you could not retrieve stays a stated gap, never an invented number.**
Name the missing item and what was substituted, and say so in the reply — a
blank cell plus a stated basis beats a plausible-looking fabricated value that
later feeds a daily aggregate.
- The script's internal retry/backoff does NOT help against 429 — it retries
  within the same rate window.

## Parse by nutrient ID, not name

SR Legacy JSON lists "Energy" twice (kJ ≈ 4.18× kcal, and kcal versions) —
a name-keyed dict can silently pick the kJ value (e.g. chicken breast shows
659 "Energy" instead of 157 kcal). Use `nutrient.id`:

| ID | Nutrient |
| --- | --- |
| 1008 | Energy (kcal) |
| 1003 | Protein |
| 1004 | Total lipid (fat) |
| 1258 | Fatty acids, total saturated |
| 1079 | Fiber, total dietary |
| 1093 | Sodium |

## JSON shape quirks

- `foodNutrients[]` entries sometimes lack `amount` (derivation-only rows) —
  filter `x.get('amount') is not None` before building the lookup dict.
- Verified meat values live in `references/meat-saturated-fat-usda.md`;
  raw JSONs in `raw/sources/usda/` of the private Wiki.
