# Meat Saturated Fat Quick Reference (USDA FDC, verified 2026-08-16; chicken parts extended 2026-09-10)

Per 100 g, cooked unless noted. Source: USDA FoodData Central SR Legacy;
raw JSONs archived under `raw/sources/usda/` in the private Wiki.

| Item | FDC | kcal | Protein | Fat | Sat fat |
| --- | --- | ---: | ---: | ---: | ---: |
| Chicken breast, skinless, braised | 171140 | 157 | 32.1 | 3.2 | **1.01** |
| Pork top loin, lean only, roasted | 168254 | 173 | 27.2 | 6.3 | **1.93** |
| Pork top loin, lean+fat, roasted | 167842 | 192 | 26.4 | 8.8 | 2.84 |
| Chicken drumstick, meat+skin, braised (卤鸡腿) | 174497 | 187 | 22.7 | 10.7 | **2.94** |
| Beef ribeye filet, lean only, grilled | 174702 | 208 | 28.4 | 10.3 | 3.62 |
| Duck, meat only, roasted | 172411 | 201 | 23.5 | 11.2 | 3.95 |
| Beef top sirloin, lean+fat, broiled | 169458 | 219 | 29.0 | 10.5 | 4.09 |
| Chicken thigh, meat+skin, roasted | 173625 | 232 | 23.3 | 14.7 | 4.11 |
| Pork shoulder, lean only, roasted | 167846 | 230 | 25.3 | 13.5 | 4.79 |
| Pork shoulder, lean+fat, roasted | 167844 | 292 | 23.3 | 21.4 | 7.86 |
| Duck, meat+skin, roasted (烧鸭/烤鸭) | 172409 | 337 | 19.0 | 28.4 | **9.67** |
| Chicken skin alone, braised | 172854 | 443 | 14.6 | 42.8 | **11.91** |
| Pork belly (五花肉), raw | 167812 | 518 | 9.3 | 53.0 | **19.33** |

## Chicken parts — extended (verified 2026-09-10)

| Item | FDC | kcal | Protein | Fat | Sat fat |
| --- | --- | ---: | ---: | ---: | ---: |
| Chicken breast, meat+skin, roasted | 171075 | 197 | 29.8 | 7.8 | 2.19 |
| Chicken wing, meat only, roasted | 172392 | 203 | 30.5 | 8.1 | 2.26 |
| Chicken thigh, meat only, roasted | 172388 | 179 | 24.8 | 8.2 | 2.31 |
| Chicken leg, meat only, roasted | 172380 | 174 | 24.2 | 7.8 | 2.11 |
| Chicken drumstick, meat+skin, roasted | 173612 | 191 | 23.4 | 10.2 | 2.74 |
| Chicken wing, meat+skin, roasted | 173630 | 254 | 23.8 | 16.9 | **4.98** |
| Chicken skin, roasted (leg+thigh skin) | 174496 | 462 | 16.6 | 44.0 | **12.1** |

- 带皮排序（熟烤）：翅 4.98 > 大腿 4.11 > 小腿 2.74 > 胸 2.19；去皮：胸 ≈1.0，翅 ≈ 大腿 ≈ 2.3。**鸡翅是「皮占比」最高的常规部位**（鸡皮/鸡尾除外）。
- CFCT 生肉对照（SFA% × fat，accessed 2026-09-10）：鸡胸脯肉 1.71 / 鸡翅 3.61 / 鸡腿 4.45 g/100g（880/881/882）——来源间翅腿排序不一致，按「都属高位」使用。

## Rules of thumb for lipid coaching

- **Cut/skin dominates species.** Same animal spans 10× (pork loin 1.9 vs
  belly 19.3). Ask "带不带皮？哪个部位？" before "哪种肉？".
- Chicken skin and pork belly are the sat-fat concentrators; duck with skin
  ≈ 2.5× duck meat-only. Whole skin-on cuts stay moderate because meat
  dilutes the skin (drumstick w/skin 2.9 g).
- Braised drumstick with skin (沙县卤鸡腿) ≈ 2.9 g/100 g — a good pick.
- Chicken wing, skin-on roasted ≈ **5 g**/100 g — highest regular part after skin/tail (skin-only ≈ 12). Skinless: wing ≈ thigh ≈ 2.3, breast ≈ 1.0. Peeling skin moves any chicken part into the low band — the skin is the switch, the cut is secondary.
- Frying/battering (辣子鸡, 炸鸡排) adds oil beyond these values — treat
  preparation method as the primary variable, skin as secondary.
- Estimates for restaurant dishes: sat ≈ total fat × 0.40–0.50 for beef/pork
  fatty cuts; × 0.25–0.30 for chicken/duck (skin-on); salmon ≈ 0.20–0.25.
- **Per-gram-protein lens: see `references/protein-source-sfa-cost.md`** — it
  normalizes these meat values against fish, tofu, dairy and eggs, and carries the
  iso-protein swap arithmetic used when the user asks whether a food is "值不值".
