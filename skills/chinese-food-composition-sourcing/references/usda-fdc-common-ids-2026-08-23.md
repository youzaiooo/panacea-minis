# USDA FDC Common Food IDs + Web-Page Extraction (verified 2026-08-22/23)

USDA 参考用于：CFCT 缺失值（纤维、SFA）、中国食物成分表没有的西式食材、
以及产品标签缺纤维时的估计。来源归档在 `/var/minis/memory/panacea-wiki/raw/sources/usda/`。

## Web-page path (when you don't need the API)

- Detail URL pattern: `https://fdc.nal.usda.gov/food-details/{FDC_ID}/nutrients`
- 网页阅读 works on these pages. Pages are huge; you get head+tail
  truncated text and the full page is saved to a cache file (path in the
  result footer).
- **Key nutrients (Sodium, saturated fat, Potassium, Fiber) often sit in the
  omitted middle** → grep the saved cache file instead of re-reading it:
  `search_files(pattern="Sodium|saturated|Potassium", path=<cache file>)`
  One grep pass returns exactly the lines needed (e.g. `Sodium, Na 2mg`,
  `Fatty acids, total saturated 0.037g`).
- Find FDC IDs via 联网搜索; third-party mirrors (rawpawiq.com,
  getfoodfacts.com, labelgrade.com) reveal the numeric ID but only the
  official `fdc.nal.usda.gov` page may be cited.
- Archive a copy into `/var/minis/memory/panacea-wiki/raw/sources/usda/` before citing in a meal record.

## Common FDC IDs (SR Legacy, per 100g)

| Food | FDC ID | Energy kcal | P g | CHO g | Fat g | Fiber g | Sat fat g | Sodium mg | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 黄瓜（带皮，生） | 168409 | 15 | 0.65 | 3.63 | 0.11 | 0.5 | 0.037 | 2 | 糖 1.67 |
| 番茄（红熟，生） | 170457 | 18 | 0.88 | 3.89 | 0.2 | 1.2 | 0.028 | 5 | 糖 2.63 |
| 全麦面包（市售） | 172688 | 252 | 12.4 | 42.7 | 3.5 | 6.0 | — | — | **标签缺纤维的面包用 6.0g/100g 估计**（臻全麦吐司等） |
| 西瓜（生） | 167765 | 30 | 0.61 | 7.55 | 0.15 | 0.4 | 0.016 | — | 糖 6.2（果糖 3.36）；钾 112 |
| 甜豆奶（市售甜豆奶参考） | 2257044 | 41 | 2.78 | 3.0 | 1.96 | <0.75 | — | — | 蔗糖 2.58；Foundation 数据。中国现磨甜豆浆用 CFCT 338 + 添加糖估算 |

## Lipid-context reuse

- 西瓜 1 kg ≈ 300 kcal / 62 g 糖（果糖 33.6 g）→ 对 TG 2.2 的用户，一次性
  大量果糖会暂时推高 TG；舒适剂量 ~500 g。沟通模式：能量账放得下（+300 kcal
  后仍落目标）≠ 糖账放得下——糖和饱和脂肪是两个独立预算。
- 面包标签无纤维 → USDA 172688 的 6 g/100g 是稳定估计值（已用于臻全麦吐司）。
