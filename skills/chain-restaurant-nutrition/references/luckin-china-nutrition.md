# 瑞幸 Luckin China — Sweetness-Tier Nutrition Snapshot

Verified 2026-08-25 while logging 椰青美式 (coconut-water Americano).

## Official data status

- luckincoffee.com (CN) has no public per-item nutrition table (SPA/marketing pages).
- Therefore: 聚合库条目 (user-submitted, AI-watermarked) + USDA
  ingredient-level cross-check, labeled as estimates (medium confidence).

## 聚合库条目 — 瑞幸 椰青冰萃美式 (per 100ml; 杯 unit = 450g incl. ice)

| Tier | code | kcal/100ml | carbs/100ml | 杯(450g) kcal | 杯 carbs g |
| --- | --- | ---: | ---: | ---: | ---: |
| 不额外加糖 | aceb2f5d1782199232 | 9 | 2.2 | ~40 | ~10 |
| 微甜 | 78bd4b6c1782199232 | 15 | 3.6 | ~68 | ~16 |
| 少少甜 | eaf6bbaa1781269147 | 21 | 5.0 | ~95 | ~23 |
| 少甜 | 440273311781269147 | 25 | 6.1 | ~113 | ~27 |
| 标准甜 | d1a354391781269147 | 32 | 7.8 | ~144 | ~35 |

- All tiers: protein ~0.1, fat 0, sat fat 0, fiber 0 per 100ml (0 脂, official selling point).
- 聚合库钠值: 12.9–13.7 mg/100ml (~58–62mg/cup) — likely under-read vs
  USDA-based (~200mg for ~200ml coconut water). Flag, don't fight it (user doesn't track Na).
- Caffeine ~100–150mg/cup (2 espresso shots, 常规值, not tracked).

## Added-sugar derivation

标准甜 − 不额外加糖 carbs = 7.8 − 2.2 = 5.6g/100ml ≈ 25g/cup added syrup —
about half the WHO <50g/day cap in one drink. Frame for TG-management talk.

## USDA cross-check (FDC 170174, Nuts, coconut water, per 100g)

19 kcal / 0.72g protein / 0.2g fat / 3.71g carbs / 1.1g fiber / 105mg Na / 0.176g sat.
不额外加糖 40 kcal/cup ≈ 200ml coconut water + espresso — consistent with
聚合库's 9 kcal/100ml × 4.5.

## Workflow notes

1. 查「椰青美式」的瑞幸分层条目，取各甜度档的值。
   Distinguish 瑞幸 vs 库迪 vs bottled drinks: 库迪 超燃椰青美式 has the same tier
   pattern (全糖 31 / 半糖 20 / 不额外加糖 9 kcal/100ml).
2. `detail` each tier to confirm the unit basis (`杯` weight) before multiplying.
3. Ask the user which tier. If unanswered, check the personal Wiki meal history
   for the same product+context first — a user-confirmed tier beats the generic
   default (2026-08-25→08-26: 早上椰青 = 不额外加糖; reused as default 2026-09-03
   with correction-pending, no user pushback). Only with no precedent on file,
   default 标准甜 + state the range (40–144 kcal) + mark correction-pending.

## 瑞幸 全冰黑巧美式 (verified 2026-09-11)

- Product: 「全冰去水」series (launched ~2026-06; 大杯 ¥20 / 超大杯 ¥23). Recipe
  = espresso + 冷冻椰浆 ~70ml + 巧克力预调液 ~30ml (+ optional 香草籽糖浆), all
  ice, no water — a coconut-latte-style drink, NOT a plain black americano.
- Official nutrition: still none (re-checked 2026-09-11).
- 条目 `fd0e4ff4`「瑞幸 全冰黑巧美式」— per 100g: E44 / P1.45 / F3.13 /
  C3.13; unit 「份」= 415 g = WHOLE CUP **including ice**.
  - ⚠️ Trap: do NOT scale by 415g (44×4.15 ≈ 183 kcal — ice carries no
    calories; this overestimates ~2.6×). Scale by the drinkable liquid portion
    (~150–175g) → ≈66–77 kcal, or use the community figure directly.
- Community consensus (non-official; June-2026 smzdm/douyin/xhs aggregation):
  大杯 16oz 不另加糖 ≈64–77 kcal; 超大杯 24oz ≈89–102; each sweetness tier
  ≈+18 kcal; 椰浆减半 ≈50. Cited split: 椰浆≈51 + 可可液≈8 + 香草糖≈5 kcal.
- Logging basis for 「全冰黑巧美式 + 不加糖」: 大杯 ≈70 kcal (range 64–77),
  sat fat ≈3g (range 2–4; coconut-dominated — USDA coconut milk fat is ≈89%
  saturated, so a thicker 椰乳 base trends to ~3.5g), protein ≈1g, carbs ≈6g,
  fat ≈4.5g — label low–medium confidence, non-official. Ask for cup size
  (超大杯 +30–45%).
- Source trail: `raw/sources/luckin-dark-choco-americano-community-2026-09-11.md`
  (private Wiki).
- Tooling note: when searxng engines time out / 联网搜索 returns empty for
  Chinese queries, `curl -A '<desktop UA>' 'https://www.baidu.com/s?wd=<encoded>'`
  works and surfaces smzdm/xhs/douyin/weibo snippets; smzdm “AIGC” aggregation
  posts quote douyin/xhs reviews with kcal figures — community corroboration
  only (low–medium), never official.
