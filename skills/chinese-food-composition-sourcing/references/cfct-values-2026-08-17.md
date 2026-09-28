# CFCT Platform: Extracted Values — 沙县鸡腿饭 (2026-08-17)

Provenance: official China Food Composition Table query platform
(nlc.chinanutri.cn), operated by 中国疾病预防控制中心营养与健康所 +
中国营养学会. All values per 100g, accessed 2026-08-17.

## Extracted values

| Food | ID | Energy kcal (kJ) | Protein g | Fat g | CHO g | Na mg | Key extras |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 鸡腿 (raw, bone-in) | 882 | 180 (753) | 16.0 | 13.0 | Tr | 64.4 | Edible 69%; cholesterol 162mg; **SFA 34.2%** of fat |
| 米饭(蒸)(均值) | 287 | 118 (493) | 2.6 | 0.3 | 25.9 | 2.5 | Fiber untested |
| 蛋（鸡蛋，均值） | 978 | 143 (599) | 13.3 | 8.8 | 2.8 | 131.5 | Edible 88%; cholesterol 585mg; SFA untested |
| 甘蓝[圆白菜，卷心菜] | 463 | 24 (102) | 1.5 | 0.2 | 4.6 | 27.2 | Vitamin C 40mg; fiber untested |
| 豆腐干(均值) | 346 | 143 (597) | 16.2 | 3.6 | 11.5 | 76.5 | **SFA 15.6%** of fat; Ca 308mg |

kJ→kcal conversion: ÷4.184 (753 kJ = 180 kcal; 493 kJ = 118 kcal).

## 交叉核对 results (same session)

| Item | 聚合库 (per 100g) | CFCT (per 100g) | Verdict |
| --- | --- | --- | --- |
| 米饭(蒸) | 116 kcal (code mifan_zheng) | 118 kcal | Consistent (±2%) |
| 卤鸡腿 (菜肴) | 127 kcal, 16.26 P, 5.89 F (fd6ba167) | 生鸡腿 180 kcal, 13.0 F | Legit raw-vs-cooked gap (braising renders fat) |
| 卤蛋 | 216 kcal, 15.1 P, 13.8 CHO (fd3f7834) | 蛋 143 kcal, 2.8 CHO | **Outlier** — 聚合库条目 likely sweet marinade; used CFCT + marinade adjust, 聚合库 as upper bound |
| 豆腐干 | 福荫卤豆腐干 169 kcal (fd311e28) | 豆腐干均值 143 kcal | 聚合库卤制产品 used as basis, CFCT as lower bound |

## Worked meal estimate (component sum)

Portions from photo: 卤鸡腿 edible 70g, 米饭 125g, 卤蛋 55g, 包菜 120g,
卤豆制品 40g → total ~410g. Component sum ≈ 430 kcal / 30.4g protein /
15.3g fat / 52.4g carbs / ~3.0g fiber / ~3.7g sat fat (patched via SFA
fractions) / ~950mg sodium (low confidence).

Whole-dish cross-check: 聚合库 卤鸡腿饭 (e203ce57_c_509307) 123 kcal/100g ×
410g ≈ 504 kcal → component sum sits in the lower-middle. Plausible range
370–530 kcal.

## Platform quirks learned

- `site:nlc.chinanutri.cn/fq/foodinfo <name>` in web_search is the reliable
  way to find IDs; multi-keyword OR queries returned empty results — search
  one food per query.
- The site's own foodlist search URL (`foodlist_米饭_0_0_0_0_1.htm`) uses
  URL-encoded Chinese and loads values lazily via JS — web_extract only got
  the first rows; detail pages (foodinfo/<id>.html) are fully server-rendered
  and extract completely.
- Detail-page tables include "同类排名/同类均值" columns — parse only the
  含量 column.
