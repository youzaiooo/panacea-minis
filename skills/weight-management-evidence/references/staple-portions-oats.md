# Staple-Food Portioning + Oat β-Glucan Evidence (learned 2026-08-28)

Worked example (reference case carried over from the original project):
171 cm / 67.5 kg sedentary adult with mixed hyperlipidemia and a
1,600–1,800 kcal weight-loss budget; asked how much dry oat-rice to cook for
dinner, then reported 75g dry actually cooked (≈ half a measuring cup).

## Portioning Flow

1. BMR (Mifflin-St Jeor) = 10×67.5 + 6.25×171 − 5×27 + 5 ≈ 1,614 kcal.
2. Sedentary TDEE ×1.35–1.4 ≈ 2,100–2,250 kcal; budget 1,600–1,800.
3. Dinner share ~550–650 kcal; staple ≈ 1/3 ≈ 200–280 kcal.
4. Dry weight: 346–389 kcal/100g → dinner staple 60–75g dry:
   - 50–60g after heavy lunch / no exercise
   - 75g cap after exercise
   - 65g dry oat-rice ≈ 1 small bowl cooked (170–200g; oat groats absorb
     ~1:2.5–3 water; soak 30–60 min before cooking)
5. Oat-vs-rice blend ratio barely matters: 389 vs 365 kcal/100g dry ⇒
   ≤18 kcal across any blend. Advise tracking TOTAL dry weight, not ratio.
   Real difference: fiber 10.6 vs 1.3 g/100g, protein 16.9 vs 7.1 g/100g.
6. Pair with protein + veg: 100–150g lean meat/fish/egg/tofu + 200g veg.

## Oat β-Glucan Lipid Evidence (verified 2026-08-28)

- FDA health claim, 21 CFR 101.81 (approved 1997): diets low in saturated
  fat and cholesterol that include soluble fiber from whole oats (β-glucan)
  may reduce risk of coronary heart disease.
- Othman RA, Moghadasian MH, Jones PJ. "Cholesterol-lowering effects of oat
  β-glucan." Nutr Rev. 2011;69(6):299–309. PMID 21631511: daily intake of
  ≥3 g oat β-glucan lowers plasma TC and LDL by 5–10%; mean TC −5%, LDL −7%.
- Whole oats ~3.5–6% β-glucan ⇒ 65g oat serving ≈ 2–3 g β-glucan (near the
  daily effective dose).
- USDA FDC numbers (per 100g dry): oats (FDP) 389 kcal / 16.9 P / 10.6 fiber
  / 1.22 SFA; white rice long-grain raw enriched 365 kcal / 7.13 P / 80 C /
  1.3 fiber / 0.18 SFA.

## Source Access Notes

- federalregister.gov → anti-bot wall. Use the eCFR API instead:
  `https://www.ecfr.gov/api/versioner/v1/full/{YYYY-MM-DD}/title-21.xml?part=101&section=101.81`
  (curl + browser UA works).
- pubmed.ncbi.nlm.nih.gov → cookie wall. Use NCBI E-utilities:
  `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21631511&rettype=abstract&retmode=text`
- USDA FDC API DEMO_KEY rate-limits with 429 after a few lookups; the web page
  `https://fdc.nal.usda.gov/food-details/{fdcId}/nutrients` can be read directly (see `authoritative-nutrition-sources` skill for
format quirks).

## Record Handling (partial-meal reports)

When only the staple is reported (e.g. 75g dry oat-rice) before sides were eaten,
use this pattern: create the meal record with the known item, mark 配菜待补充 in
Uncertainty, update the daily cumulative as 进行中, then patch both when
sides arrive. Oat-rice blend ratio unknown → estimate 1:1 with pure-oats /
pure-rice as the range bounds.
