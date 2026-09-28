# KFC China: Nutrition Proxy Method (verified 2026-08-21)

KFC China publishes NO official nutrition data (kfc.com.cn has no nutrition page;
circulating "官方热量表" are self-media and conflict). Working estimation method:

## Proxy sources

- **US KFC official values via CalorieKing transcription** — kfc.com/nutrition and
  /full-nutrition-guide block scraping (geo-redirect + antibot), but CalorieKing's
  transcription page extracts cleanly:
  Original Recipe Chicken Breast, bone-in = **390 kcal / 21g fat / 4g sat / 11g carbs /
  39g protein / 1190mg Na per piece (6.1 oz)**.
  URL: https://www.calorieking.com/us/en/foods/f/calories-in-menu-items-original-recipe-chicken-breast-bone-in/PzEG8ieZSxu_okFK4Rq4Ww
- **交叉核对**: 「肯德基 吮指原味鸡」code=`kendejishunzhiyuanweiji` =
  346 kcal/100g, fat 21.3g/100g, protein 29.7g/100g. Sat field is 0 (data gap) —
  apply US ratio ~19% of total fat (~4g sat per 100g).

## New-item estimation recipe (原味鸡肉霸堡, 2026-08-21)

KFC "肉霸堡" products = fried chicken pieces replacing the bun (no bread).
Estimate ≈ 1.5–2 × US Original Recipe piece equivalent:

- 霸堡 (two thick fried cutlets + vinegar slaw, no bun) ≈ **550 kcal / sat ~6.5g / Na ~1200mg**
- 吮指原味鸡 ×1 ≈ **280 kcal / sat ~3.5–4.5g**

## Reporting rules

- Warn that ONE fried-chicken meal can consume the whole ≤15g/day sat-fat budget
  (套餐A 霸堡+2原味鸡 ≈ 12–17g sat).
- Report sat fat as a RANGE, never a single precision value.
- Mark confidence medium for the burger estimate; the portion/pieces count is the
  dominant uncertainty — ask the user which combo they actually ate.
