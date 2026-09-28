# USDA FDC API Parsing Pitfalls (learned 2026-09-03)

For ingredient cross-checks against USDA FoodData Central (meal logging).

Endpoints (no signup; `DEMO_KEY` is rate-limited but fine for a few lookups):

- Detail: `https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key=DEMO_KEY`
- Search: `https://api.nal.usda.gov/fdc/v1/foods/search?query=<urlencoded>&dataType=SR%20Legacy&pageSize=6&api_key=DEMO_KEY`

## Pitfalls

1. **Energy appears TWICE in detail `foodNutrients`** — kcal (nutrient id 1008)
   and kJ (1047). Parse by `nutrient.id` or `unitName == "KCAL"`; matching by
   name alone grabs the kJ entry first → values ~4.2× too high. Example: beef
   top sirloin came back "916" (kJ) — true value 219 kcal/100g. A "916 kcal"
   cooked steak is a unit bug, not data.
2. **SR Legacy search responses usually omit `foodNutrients`** — a search/cached
   search JSON gives description + fdcId only. Call the detail endpoint for
   per-100g values (this also means cached search files can't be quoted for
   numbers without a detail fetch).
3. **Never assume an FDC ID maps to the food you want**: an assumed 169464 for
   "top sirloin, separable lean only" actually returned "Beef, short loin,
   t-bone steak, separable lean and fat". Verify the returned `description`
   matches before archiving under a descriptive filename, and delete any
   mislabeled archive immediately — a file named after the wrong food poisons
   future lookups.
4. **Sanity-check magnitudes before archiving**: cooked gai lan/Chinese broccoli
   ~22 kcal/100g, cooked lean beef 180–220 kcal/100g, cooked white rice
   116–130 kcal/100g. Numbers ~4× off are the kJ trap, not exotic data.

## Known-good IDs (verified 2026-09-03)

| Food | FDC ID | kcal/100g | Notes |
| --- | ---: | ---: | --- |
| Broccoli, chinese (芥蓝), cooked | 169392 | ~22 | fiber 2.5g/100g |
| Beef, top sirloin, lean & fat, 0" trim, choice, broiled | 169458 | ~219 | 29.0P / SFA 4.09 / 100g |
| Rice, white, medium-grain, cooked | 168930 | ~130 | 聚合库 mifan_zheng says 116 — cross-check range |
