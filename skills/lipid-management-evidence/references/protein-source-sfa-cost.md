# Protein-Source Sat-Fat Cost — per gram of protein, plus swap arithmetic

Verified 2026-09-20 against USDA FDC SR Legacy, the CFCT official platform
(`chinese-food-composition-sourcing` §1), and package labels. Prompted by
"低脂奶 500 ml 只给 25 g 蛋白却有 5 g 饱和脂肪，还不如吃鸡肉" — the arithmetic is
correct; the useful answer is the normalized ranking below.

## The ranking (what 20 g of protein costs in saturated fat)

| Source | Basis / id | SFA per 20 g protein | g SFA per g protein |
| --- | --- | ---: | ---: |
| 鳕鱼, cooked | USDA 171956 (105 kcal / 22.8 P / 0.86 F / 0.168 SFA per 100 g) | **0.15 g** (88 g) | 0.007 |
| **去皮鸡胸, cooked** | USDA 171477 (165 / 31.0 / 3.57 / 1.01) | **0.65 g** (65 g) | **0.033** |
| Salmon, wild, cooked | USDA 171998 (182 / 25.4 / 8.13 / 1.26) | 0.99 g (79 g) | 0.050 |
| 北豆腐 | CFCT 334 (99 kcal / 12.2 P / 4.8 F; SFA = 15.1% of fat → 0.72) | 1.18 g (164 g) | 0.059 |
| 鸡胸脯肉, raw | CFCT 880 (133 / 19.4 / 5.0; SFA = 34.2% of fat → 1.71) | 1.76 g (103 g) | 0.088 |
| Salmon, farmed, cooked | USDA 175168 (206 / 22.1 / 12.4 / 2.4) | 2.17 g (90 g) | 0.109 |
| 带皮混合鸡肉, cooked | USDA 171450 (239 / 27.3 / 3.79) | 2.78 g (73 g) | 0.139 |
| **低脂牛奶** | product label (55 kcal / 5.0 P / 1.5 F / 1.0 SFA per 100 ml) | **4.00 g** (400 ml) | **0.200** |
| **鸡蛋 (OMEGA-3)** | product label (137 / 12.1 / 9.6 / 2.8 per 100 g) | **4.63 g** (165 g ≈ 3.3 个) | **0.231** |

Ordering to reuse: **fish ≈ skinless poultry < tofu < skin-on poultry < low-fat
dairy ≈ eggs**. Eggs cost MORE per gram of protein than low-fat milk — the
counter-intuitive case worth stating out loud when the user blames the dairy.

Basis warning: CFCT rows are 生/食部 and give SFA as a % of fat; USDA rows are
cooked. Convert and label, and never list a raw CFCT number in the same column
as cooked USDA values without a basis note.

## Worked swaps (arithmetic verified 2026-09-20)

| Swap | SFA | Protein | Energy |
| --- | ---: | ---: | ---: |
| 110 g 带皮鸡 (263 kcal / 30.0 P / 4.17 SFA) → 97 g 去皮鸡胸 (160 kcal / 30.0 P / 0.98 SFA) | **−3.19 g** | equal (30 g) | −103 kcal |
| Milk 500 → 200 ml + 48 g 去皮鸡胸 (restores the 15 g protein) | **−2.52 g** | equal (~25 g) | −86 kcal |
| Both | 14.60 → **~8.9 g** (of a 15 g budget) | unchanged | **~−190 kcal** |

Consequences to state with the numbers:

- Standalone dairy budget figure: **500 ml low-fat milk = 5.0 g SFA ≈ 34% of a
  15 g/day budget**, and it is usually the single largest line item — but it
  also carries ~750 mg calcium per 500 ml, so reduce or switch to 0-fat rather
  than dropping dairy blindly.
- The 带皮→去皮 swap is free: identical protein, fewer calories, no loss of
  anything. Offer it FIRST, before any quantity reduction or food removal.
- The swaps remove ~190 kcal, so a user who is under-eating must recover them
  with carbs/veg/fruit; protein must stay at target throughout.
- Food-matrix caveat travels with the numbers: dairy-as-a-food is not associated
  with higher CVD risk (see `references/meat-saturated-fat-usda.md` neighbours
  and the private Wiki's `concepts/dairy-fat-and-lipids.md`), yet saturated fat
  still counts against the budget. Concede the arithmetic, keep the budget.

## Private Wiki companions

- `concepts/protein-sources-and-sfa-cost.md` — same table with the full source
  trail and the "常见误读" list.
- `raw/sources/2026-09-20-protein-sfa-cost-sources.md` — per-PMID abstracts
  and every id used above.
