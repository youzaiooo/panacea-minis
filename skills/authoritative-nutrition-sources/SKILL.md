---
name: authoritative-nutrition-sources
description: >
  权威营养数据源：USDA FoodData Central 查询、官方站点被反爬时的替代路径、数值口径核对。
  需要 USDA/官方数值，或官方页取数失败时加载。
---

# Authoritative Nutrition Sources

Use when Panacea needs food-composition numbers or guideline evidence for meal
logging and lipid-aware advice: aggregated databases return `0`/no match, a packaged food has
no label, an alcohol/lipid question needs a cited number, or an official site
blocks scraping. This skill fills the "authoritative web source" half of the
meal-aggregation rule (package label first, then official source, then database).

## USDA FoodData Central API (primary numeric source)

No signup needed — `DEMO_KEY` works (rate-limited; fine for a few lookups):

- Detail: `https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key=DEMO_KEY`
- Search: `https://api.nal.usda.gov/fdc/v1/foods/search?query=<urlencoded>&dataType=SR%20Legacy&pageSize=5&api_key=DEMO_KEY`
- Fetch with `curl` or python `urllib` + browser User-Agent header; parse
  `foodNutrients[].nutrient.id` against the table below.
- The API intermittently fails the first connection attempt with an SSL
  connect error (curl exit 35). Retry with backoff before declaring failure
  — `scripts/usda_fdc_lookup.py` already retries internally.

| Nutrient ID | Name |
| --- | --- |
| 1008 | Energy (kcal) |
| 1003 | Protein (g) |
| 1004 | Total fat (g) |
| 1258 | Fatty acids, total saturated (g) |
| 1079 | Fiber, total dietary (g) |
| 1093 | Sodium (mg) |

`dataType=SR Legacy` = classic per-100g composition dataset. A ready-to-run
lookup script ships with this skill: `scripts/usda_fdc_lookup.py`.

**When the API is rate-limited (HTTP 429 — DEMO_KEY is shared/global):** the
human-readable page for the same food renders the full nutrient table and
网页阅读 handles it — `https://fdc.nal.usda.gov/food-details/<fdcId>/nutrients`
(observed working 2026-09-10 for 170393). Fallback if that fails: local
Firecrawl render, `curl -X POST http://localhost:3002/v1/scrape -d '{"url":"<url>","formats":["markdown"]}'`.
Archive the extracted page under `raw/sources/usda/` when it feeds a record.

## Antibot-Blocked Official Sites: Fallback Ladder

When 网页阅读 returns 500/"document_antibot" (observed on heart.org and
ahajournals.org), do NOT conclude the source is unavailable:

1. Re-find the same recommendation at an alternate authoritative publisher —
   e.g. the Chinese dietary guideline's official site `dg.cnsoc.org` and the
   NLA's `lipid.org` both scrape fine.
2. For numeric food values, switch to the USDA FDC API above instead of a webpage.
3. Try `curl` with a browser UA from the terminal before declaring failure.
4. Only if every path fails, state the blocker and cite the next-strongest
   verified source. Never fabricate a number to fill the gap.

Keep the raw response trail in the health Wiki's `raw/sources/` when values
feed a meal record.

## Lipid-Context Knowledge Bank

For alcohol questions in a lipid-management context, see the
`lipid-management-evidence` Skill's `references/triglyceride-evidence-bank.md`
— cited TG guideline numbers (中国血脂管理指南 2023 分层, NLA LipidSpin 2022)
and alcohol–TG dose effects. For meat/poultry saturated-fat numbers (chicken
skin = the SFA concentrator; chicken parts extended 2026-09-10), see the same
Skill's `references/meat-saturated-fat-usda.md`.

## Boundaries

- This is a food-data and guideline-evidence source, not a diagnosis tool.
- Do not duplicate other database workflows; use this for the authoritative
  web-source side and for data-gap patches (e.g. broccoli fiber,
  egg saturated fat).
- Verify numbers against the cited page/API response before using them in a
  meal record; label estimates as estimates.
