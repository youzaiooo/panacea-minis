# Skinless poultry (USDA) + corn (CFCT) — verified 2026-08-29

会话后半段新增数据（前半段猪蹄/鸡腿带皮/鸭类/麦香鱼见同目录 `cfct-values-2026-08-29.md`）。

## 去皮禽类 — USDA FDC API 精确值（熟重 /100g）

| Item | FDC ID | kcal | 蛋白 | 脂肪 | SFA |
| --- | --- | ---: | ---: | ---: | ---: |
| 去皮鸡腿（leg, meat only, roasted） | 172380 | 174 | 24.2 | 7.8 | 2.11 |
| 去皮鸭（整鸭 meat only, roasted；**无独立鸭腿条目**，用此近似并标注） | 172411 | 201 | 23.5 | 11.2 | 3.95 |
| 去皮鸭肉（生） | 172410 | 135 | 18.3 | 5.95 | 2.32 |
| 去皮鸡腿（生） | 173619 | 120 | 19.2 | 4.22 | 1.05 |

- 对比结论：去皮后**鸭饱和脂肪仍是鸡的近 2 倍**（3.95 vs 2.11 g/100g），脂肪 +44%；蛋白打平（23.5–24.2g）。鸭腿是深色肉，实际略高于整鸭均值
- 200g 熟去皮肉示例：鸡腿 350 kcal / 饱和 4.2g vs 鸭腿 400 kcal / 饱和 7.9g（当天已有 4.3g 时吃鸭腿 → 12.2g，逼近日限 15g）
- API 用法：`https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=<urlencoded>&dataType=SR%20Legacy&pageSize=5`（python urllib，无需注册 key）；"duck leg meat only" 无独立条目 → 放宽到 "duck meat only" 并标注近似。完整端点/字段见 authoritative-nutrition-sources 技能

## 玉米（CFCT 292 玉米(鲜) + 品种差异口径）

- CFCT 292 玉米(鲜)：113 kcal/100g 可食部 / P4.0 / F1.2 / C22.8 / 钠 1.1mg / **食部 46%**（棒芯占一半多——带棒毛重必须 ×46% 折算）；纤维 CFCT 无字段 → USDA 甜玉米 cooked ~2.4g/100g
- **品种差异巨大，必须询问用户**：聚合库 甜玉米 107 / 煮玉米 84 / 糯玉米 172 kcal/100g；甜玉米脂肪略高（2.5 vs 1.2g）但碳水低（17.8 vs 22.8）
- 换算示例：275g 带棒 × 46% ≈ 127g 可食部 ≈ 136 kcal（甜玉米）；若用户称的是玉米粒则能量近翻倍（+160 kcal）——记录时必问是否带棒
- 用户确认品种后的更正处理：本餐 219 → 212 kcal，meal record 保留 "User correction" 行（品种确认 + 重算），daily/log 同步重算
