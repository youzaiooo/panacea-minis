---
name: chinese-food-composition-sourcing
description: >
  中国食材与家常菜的营养数值查询：中国食物成分表（CFCT）取数、多来源交叉核对、缺失字段修补。
  记录中餐或核对某中国食物的营养数字时加载。
---

# Chinese Food Composition Sourcing

Use for the numeric half of meal logging when foods are Chinese ingredients or
home-style restaurant dishes: find the strongest regional per-100g values
(China Food Composition Table), cross-check numbers across sources, and patch
missing fields without inventing values.

## 1. CFCT official platform (primary regional source)

The official query platform of 《中国食物成分表》(第六版) — run by 中国疾病
预防控制中心营养与健康所 + 中国营养学会:

- Search UI: `https://nlc.chinanutri.cn/fq/`
- Detail page: `https://nlc.chinanutri.cn/fq/foodinfo/<id>.html` — extracts
  cleanly with 网页阅读. Per-100g table: energy (kJ), protein, fat, CHO,
  sodium, and a 脂肪酸 section giving **SFA/MUFA/PUFA as % of total fat**.
- **Find IDs reliably — POST the site's own JSON endpoint (verified 2026-09-17).**
  The category `foodlist_*.htm` pages are JS-rendered from an AJAX call, so
  curling them returns an empty table (the food rows are not in the HTML).
  Query the backend directly:

  ```sh
  curl -s -X POST "https://nlc.chinanutri.cn/fq/FoodInfoQueryAction!queryFoodInfoList.do" \
    -H "X-Requested-With: XMLHttpRequest" \
    -H "Referer: https://nlc.chinanutri.cn/fq/foodlist_0_14_0_0_0_1.htm" \
    --data-urlencode "categoryOne=14" --data-urlencode "categoryTwo=0" \
    --data-urlencode "foodName=西梅" --data-urlencode "pageNum=1" \
    --data-urlencode "field=0" --data-urlencode "flag=0"
  ```

  Returns JSON `list` rows; `row[0]` = foodinfo id, `row[2]` = 食物名,
  `row[3]` = 食部, `row[4]` = 水分, `row[5]` = 能量(kJ), `row[6]` = 蛋白质.
  categoryOne=14 is 水果类及制品 (categoryTwo 55/56/57/58/59/60 = 仁果/核果/
  浆果/柑橘/热带/瓜果; 23 = 速食食品 with 125 = 快餐食品). Then fetch
  `foodinfo/<id>.html`. This is far more reliable than 联网搜索
  `site:` queries or guessing numeric ids. **缺 header/参数会静默返回空结果**（`list` 为空，
  不是「该食物不存在」）：`X-Requested-With: XMLHttpRequest`、`Referer`、`categoryOne` 三者
  缺一即空——先补齐再重试，不要据此改用弱来源。 NOTE: this platform's 总膳食纤维
  field IS populated for some foods (西梅 1.50 g/100g) even though 李子 shows blank
  — check per food, don't assume it is always empty.
- **第二条找 id 路径（POST 返回空时用，已验）**：该端点在**缺会话/参数不对时会静默返回空**
  （body 长度 ~1，不是「食物不存在」）。**补 header 重试一次仍空就换路，不要改用弱来源**：
  1. 联网搜索 查 `<食物名> nlc.chinanutri.cn foodinfo`——结果标题直接带 id
     （如 `foodinfo/1098.html` = 虾皮）；
  2. 抓 `https://nlc.chinanutri.cn/fq/foodinfo/<id>.html`（普通 UA，无需 header 即可），
     用正则取值：`钙\(Ca\)\s*([\d.]+)` · `蛋白质\(Protein\)\s*([\d.]+)` ·
     `钠\(Na\)\s*([\d.]+)` · `能量[^0-9]{0,80}?([\d.]+)\s*kJ`。
- **id 按品类成段排列 → 用「扫区间」批量建表**：逐 id 取「标题 + 数值」，按关键词过滤即可一次捞出一整类，
  比逐个搜名称快得多。**必须先在 Python 里按关键词过滤再 print**，否则一次刷出上百行白烧上下文。
  已验区间、代表条目与可直接复用的取数片段见 `references/cfct-id-lookup-and-calcium.md`
  （豆类及制品 330–350 · 蔬菜嫩茎叶花菜类 460–505 · 鱼虾蟹贝类 1090–1125 · 调味品 1510–1550）。
- kJ ÷ 4.184 = kcal. "—" = untested (fiber often missing → patch from USDA).
- howtoeat.cn mirrors CFCT 6th-ed values — acceptable fallback, prefer the
  official page for citations.
- Keep extracted values in the Wiki under `raw/sources/` with access date.

Worked values (2026-08-17, 沙县鸡腿饭): see
`references/cfct-values-2026-08-17.md` — 鸡腿 882, 米饭(蒸) 287, 蛋 978,
甘蓝 463, 豆腐干 346, plus the SFA fractions and cross-check notes.

## 2. Field-gap patches — per-food SFA fractions (NOT one blanket rule)

Missing/zero saturated-fat fields are common in aggregated databases. Patch with the food's own SFA
fraction of total fat (CFCT 脂肪酸 section or USDA), not a single rule:

| Food | SFA % of total fat |
| --- | ---: |
| Beef products (牛筋丸 etc) | ~45 |
| Chicken, skin-on (卤鸡腿) | 34.2 (CFCT 鸡腿) — the 45% beef rule overestimates by ~30% |
| Egg (卤蛋/煮蛋) | ~31–32 |
| Tofu products (豆腐干) | 15.6 (CFCT 豆腐干) |

Fiber gaps: USDA references (cooked cabbage ~1.9g/100g, broccoli ~2.6g/100g,
cooked white rice ~0.4g/100g). Always label patched values as estimates in
the meal record.

## 3. Prepared-dish entries can be outliers

Dish entries in aggregated databases sometimes deviate strongly from official base foods.
Example: a 卤蛋 entry at 216 kcal/100g with 13.8g CHO vs CFCT 蛋
143 kcal/100g / 2.8g CHO — likely a sweetened-marinade or data-entry口径.
Resolution:
1. Compute with the official base-food value + a small marinade adjustment.
2. Keep the outlier as the stated upper bound in the plausible range.
3. Record the discrepancy in the meal record's uncertainty section.

Legitimate raw-vs-cooked differences are NOT outliers: CFCT 生鸡腿 180 kcal
vs 卤鸡腿 (菜肴) 127 kcal/100g — braising renders fat out. Consistent
same-basis values (米饭 116 vs CFCT 118 kcal/100g) corroborate each other.

## 4. Whole-dish cross-check

When a database has a composite dish entry (卤鸡腿饭 123 kcal/100g): multiply by
the total estimated portion weight (~410g → ~504 kcal) and compare with the
component sum (~430 kcal). Component sum should sit in the lower-middle of
the dish-entry figure; a large gap signals a portion or oil assumption error.
Cite the cross-check in the meal record — it strengthens confidence cheaply.

## 4.5 双源冲突（USDA vs CFCT）：给区间，不挑一个

同一食物两库差异常是**折算方法差异**，不是食物差异——判据是看成分之间是否自相矛盾：

- **判据**：若**碳水几乎相同**（例 14.2 vs 14.32 g/100 g）而**能量差 20–30%**（53 vs 68 kcal），
  那是口径差异（中国表对水果类多按**可消化碳水**折算，USDA 用 Atwater）→ **不得据此断言某一库"错"**。
- **处置**：记录里**同时列两库**，能量与争议微量营养素**给区间**，并声明主口径 + 理由；
  区间两端都要出现在正文，不能只在附录里。
- **高变异营养素禁用单值**：VC 随品种/成熟度可差数倍（番石榴 USDA 228.3 vs CFCT 68.0 mg/100 g）
  → **只给区间**，Uncertainty 里写明「品种/成熟度未知」。
- **一库缺字段就直接借另一库并标注**（CFCT 番石榴无纤维/脂肪酸字段 → 纤维取 USDA 5.4 g/100 g），
  不要因为"两库不一致"就放弃纤维这类关键指标。
- **先查 Wiki 既有口径再选主库**：`concepts/*.md`（如 `fruits-fiber` 已定番石榴 = USDA FDC 173044）、
  `concepts/foods/`、`dietary-profile.md` 常已记明主库与 ID → **沿用**。同一食物出现两套数字的代价，
  比选哪一库都大。

## 5. Reference lookup before re-querying

查值顺序：① **技能 references 里的已验值文件**
（`verified-values-*.md`、`skinless-poultry-and-corn-2026-08-29.md`、`chicken-parts-sfa-2026-09-10.md`、`cfct-values-2026-09-14.md`（腊肠816/草鱼1003/菜心453/咸鸭蛋995-996）、`cfct-values-2026-09-20.md`（**油麦菜 482 / 萝卜干 1550 钠 4203 / 带皮鸡肉混合部位 FDC 171450 / 黄油 173410**） 等，含品种/部位对照；**番石榴 = CFCT 719（热带水果）
/ USDA FDC 173044（既有主口径）——双源差异见「4.5 双源冲突」节**）
+ **健康 Wiki 最近同款餐记录**（含既定口径）→ ② 只有两处都没有时才联网重新查询。
参考文献全部命中即跳过外部查询——重复查询既慢、又易引入口径漂移。

若某来源的具体条目曾被采用，在 Wiki 里记录其 ID 与口径——下次同类食物直接沿用，避免口径漂移。

## 6. 用户不回复时按默认口径估算（learned 2026-09-05）

一句话餐报后 clarify（做法/品种）超时是常态，不要卡住：按最常规默认落账并
在记录 Uncertainty + 回复里显式标注待确认项与影响幅度，邀请一句话更正。

| 食物 | 默认口径 | 影响幅度（更正方向） |
| --- | --- | --- |
| 蛋（未说做法） | 水煮：55g/个 ≈76 kcal / P6.3 / 饱和1.7g / Na62 | 煎/炒蛋 +90~130 kcal、脂肪 +10g |
| 玉米（未说品种/毛重） | 整根带棒 ~275g × 食部46% ≈127g 可食部，按 CFCT 292 中性基准 113 kcal/100g | 糯玉米 +75~95 kcal、碳水明显更高；若为玉米粒称量则能量近翻倍 |

Total 表给 plausible range 覆盖两端（9/5 例 275–480 kcal），best estimate 用
中值，不装精确。已验值所在：`references/skinless-poultry-and-corn-2026-08-29.md`
（玉米全套）与 Wiki 记录 2026-08-29-1446-snack-egg-corn.md（蛋口径）。

## 7. USDA 搜索响应结构坑 + 拉面店新锚点（2026-09-05）

- `foods/search?dataType=SR%20Legacy` 返回**平铺** `foodNutrients[].nutrientId`
  （没有嵌套 `nutrient.id` —— 按 API 文档写 `nutrient.id` 直接 KeyError，本日实测）。
  容错解析：`n.get('nutrient',{}).get('id') or n.get('nutrientId')`；detail 端点
  才是嵌套格式。原始 JSON 存档到 `raw/sources/usda/usda-fdc-<slug>-<date>.json`
  供餐食记录引用。
- **USDA 报 HTTP 429（`DEMO_KEY` 全局共享限流，约 30 次/小时）时，不要在限流窗口内重试**：
  中国常见食材（肉/蛋/豆制品/蔬果）直接改走 §1 的 CFCT 官方 POST 端点（无配额、已验可用）。
  CFCT 是**生/食部**基准且 SFA 以**占脂肪百分比**给出——折算后必须标明基准，
  **不得与 USDA 熟制值同列比较**。原计划要取、但两库都取不到的值，
  在记录里留作**显式缺口**并写明替代口径，**绝不编造数字填空**。
- SR Legacy **没有熟拉面/熟猪五花**条目 → 已验代理（数值与完整工作表见
  `references/usda-fdc-ramen-anchors-2026-09-05.md`）：
  - 熟蛋面 FDC 169732：138 kcal / P4.5 / F2.1 / SFA0.4 / 纤维1.2 / Na5 per 100g
    —— 代理拉面店熟面与替玉（每份熟重 ~200g ≈ 280 kcal）。
  - 生猪五花 FDC 167812：518 kcal / F53 / SFA19.3 / P9.3 per 100g —— 卤制出油
    折算熟重 ~450 kcal / SFA ~15，日式叉烧（五花卷）锚点；梅花肉则 ~230 kcal。
- 市售「豚骨拉面」泡面/杯面条目（88–132 kcal/100g）是即食口径，勿用于店售整碗。

## 8. 纤维缺失时的两条硬路径（2026-09-18，五黑豆浆案例）

标签未标纤维是常态（中国非强制项；GB 28050-2025 强制项 = 能量/蛋白/脂肪/饱和脂肪/碳水/糖/钠）。不要因此把纤维当 0。

1. **碳水账定上限（最可靠，无需外部数据）**：`纤维上限 = 碳水化合物 − 糖`。依据 GB 28050 配套问答——未单独标示纤维时纤维并入碳水数值。得到的是**上限**，不是估计值。
2. **固体量估算**：`(蛋白+脂肪+碳水) − 添加糖 = 豆谷固体`，再乘混合干基纤维比例（大豆/黑豆 ~9%、黑芝麻 ~11%、黑米 ~3.5%）得中位值；给范围与 low–medium 置信度。

坑与替代源：

- **部分数据库的纤维字段常缺失或为 0**（不可当作「该食物无纤维」）——不要用它给纤维值下结论。
- **USDA「Okara」FDC 172452 在 SR Legacy 缺纤维字段**（无 nutrientId 1079，只有 proximates/矿物质/氨基酸）→ 需改引综述：豆渣干基膳食纤维 ~40–50%（PMC10345676；成分口径 脂肪10/蛋白25/**纤维50**/其他15）。
- **PMC 网页版要 cookie**（网页阅读 返回 "Cookies must be enabled"）→ 改走 Europe PMC REST：`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC<id>/fullTextXML`。
- **CFCT 平台无「豆渣/豆腐渣」条目**；「豆浆」= id **338**（水分96.4/65kJ/蛋白1.8/脂肪0.7/碳水1.1/钠3.0mg，**无纤维字段**）；「豆浆粉」= id 331。
- 纤维类型要分开说：豆渣/大豆纤维以**不溶性**为主（饱腹/排便/肠道），LDL-C 证据更强的是**水溶性**纤维（车前子壳、燕麦 β-葡聚糖）；大豆纤维的小型 RCT 证据 = PMID 23881774（n=39，勿过度解读）。

## 9. 中国人群摄入量、营养标准阈值（回答「中国人普遍缺 X 吗」）

这类问题要的是**人群分布与对照阈值**，不是食物成分表：

- **数字去 Europe PMC REST 取**：China CDC Weekly、卫生研究、CHNS/CNTCS 队列均被索引，且**数值就在摘要里**
  （均值/中位数摄入量、低于 EAR 的人群比例）：
  `search?query=<urlencoded>&format=json&pageSize=5&resultType=core`，单条用 `query=EXT_ID:<pmid>`。
  已验 query 形状：`(TITLE:"calcium intake" AND ABSTRACT:"Chinese")`、
  `(ABSTRACT:"<nutrient> intake" AND ABSTRACT:"China" AND (ABSTRACT:"inadequate" OR ABSTRACT:"below"))`。
  **引用时照拄分母与阈值**（mean vs median、EAR vs RNI、调查年份）；**不要转述媒体口径的「X% 的人缺 Y」**。
- **阈值与声称口径去国标 PDF 取**：网页阅读 能直接读国标正文（GB 28050—2025 附录 A 的 NRV 表、
  附录 C 的含量声称门槛、附录 D 的允许作用声称用语）——比任何二手页/商品页可靠，也便于告诉用户「看包装识字」。
- **「摄入不足」是分布，不是诊断**：报摄入水平的**必须并报它对照的推荐值**，并说明推荐值带安全裕量
  （RNI vs 更低的 EAR），再配上结局证据（包括「未发现关联」与非线性 J 型的情形）；否则读者会得出
  「人人都要补剂」的错误结论。
- **自己的推算不得包装成调查值**：查不到引用值就给**显式粗估**（标「粗估，非调查/实测值」并写推导依据），
  不得让它看上去像引文。

## Boundaries

- Food-data source skill only — no diagnosis, no targets, no prescriptions.
- Do not treat patched/estimated values as measured values; label them.
- Meal-record ownership stays with health-coach; this skill supplies and
  verifies the numbers.
