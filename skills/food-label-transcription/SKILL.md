---
name: food-label-transcription
description: >
  包装食品标签转录与建档：标签照片→逐字转录→产品库页（concepts/foods/），并回溯修正餐食记录。
  用户发来任何包装标签照片（正面、配料或营养成分表）时加载。
---

# Food Label Transcription

Transcribe packaged-food labels into Panacea's personal health Wiki product database (`concepts/foods/`). This skill handles the full pipeline: image ingestion, multi-image merging, product page creation, index updates, and retroactive meal-record correction. Load alongside `health-coach`.

## When to Use

- User sends one or more photos of a packaged food label (any surface: front, nutrition panel, ingredients, jar overview).
- User asks to "record a label" or "建档" a food product.
- A meal was logged with an estimated value for a packaged food, and the user later provides the actual label — the meal record must be updated.

## Multi-Image Label Workflow

Packaged foods often spread their label across multiple surfaces. The user may attach 2-4 photos without indicating which is which. Handle this systematically:

1. **Call `vision_analyze` on EVERY attached image** in parallel, each with the same detailed prompt:
   > 请完整转录这张产品包装标签上的所有文字信息，包括：产品名称、品牌、净含量、配料表、营养成分表（每100g的所有项目及数值）、生产商、产品标准号、生产日期、保质期等一切可见信息。不要遗漏任何一项营养数值。

   Each `vision_analyze` result will capture what's visible on that surface. Some images will return "营养成分表未展示" — that's fine, the data lives on another surface.

2. **Merge the results** into a single coherent product record. Prefer the 喷码 (inkjet print) date over a pre-printed date field when both appear. Note in the product page which image contributed which data via a 标签存档 table.

3. **Copy images to `raw/images/`** with date-based names and face suffixes (e.g. `-label-front.jpg`, `-label-nutrition.jpg`, `-label-jar.jpg`).

## Product Page Structure

Create the page at `concepts/foods/<short-slug>.md`. Use this template:

```markdown
# <Brand> <Product Name>

## 产品信息
- **产品名称：** (verbatim from label)
- **品牌：** (verbatim, including ®/™ marks)
- **产品类型：** (if listed)
- **净含量：**
- **配料：** (verbatim list)
- **生产日期（喷码）：**
- **保质期：**
- **贮存条件：**
- **产品标准号：**
- **食品生产许可证编号：**
- **产地：**

## 营养成分表（每100g）
| 项目 | 每100g | NRV% |
| --- | ---: | ---: |
| 能量 | ...kJ (≈...kcal) | ...% |
| 蛋白质 | ...g | ...% |
| 脂肪 | ...g | ...% |
| 碳水化合物 | ...g | ...% |
| 膳食纤维 | ...g | ...% |
| 钠 | ...mg | ...% |

## 标签存档
| 图片 | 路径 |
| --- | --- |
| (描述) | `raw/images/YYYY-MM-DD-<slug>-<face>.jpg` |

## 计算速查（基于标签实际值）
| 用量 | 能量 | (key nutrients) |
| --- | ---: | ---: |
| 1g / 5g / serving | | |
```

## Chinese Label Format: Carb/Fiber Separation

Chinese GB 28050 nutrition labels may list dietary fiber (膳食纤维) as a separate row rather than as a sub-item of total carbohydrate. When the label shows 碳水化合物 = 0g but 膳食纤维 = 89.7g, the product's non-fiber digestible carbohydrate is 0g. Do NOT add fiber to the carbohydrate figure — the label already excludes it. This format is common for pure-fiber products (psyllium husk, konjac, etc.).

When a meal record was previously created using an estimated carb value that included fiber, update it to match the label's actual split.

## Post-Transcription: Update Meal Records

After creating/updating the product page:

1. Search for any meal records from the **current day** that used an estimated value for the same food.
2. Update the meal record: replace the estimate row with label-based values, bump confidence to `high`, update the totals, and note the correction in Record Provenance → User corrections.
3. Recalculate that day's `records/daily/YYYY-MM-DD.md` cumulative values.
4. Update `concepts/food-database.md` index and `index.md` to include the new product.

## 先要正面（背面永远不够）

**背面成分表只能给出 1+4（能量/蛋白/脂肪/碳水/钠）**；决定量级的**配料表**在正面。收到背面照后应 **主动请用户补拍正面**（产品名、配料、净含量、保质期都在那里）。

- **配料表能定性含糖量**：一旦确认“唯一含碳水的添加物是白砂糖”，碳水差额法估算的置信度就从 medium 提到 **medium-high**；若看到麦芽糊精/糖浆/甜味剂，则需重算或改为“总碳水口径”。
- **蔗糖 = 葡萄糖 + 果糖（约 50/50，定义性）** → 需要果糖量时可直接换算（如 22.5 g 蔗糖 ≈ 11 g 果糖）。
- **两面营养成分表数值一致 = 免费的双重复核**，应在产品页显式记录“正/背两面一致 ✅”。
- **净含量常不在成分表那一面**；若两面都没拍到，份量必须标“用户口述”，不得写成标签值。

## 只拍到部分标签时（背面成分表最常见）

用户常常只拍一张**背面成分表**，产品名/配料表/净含量都不在画面里。此时：

1. **分列两层**：产品页和餐记录里必须显式分开「标签可见值」与「用户口述/推算值」，逐项标置信度。
   产品名若来自用户口述，写“**用户口述（标签照片未显示产品名 → 未经标签验证）**”，**不得当成标签值**。
2. **照片横置先转正再 OCR**：PIL 两个方向各存一份，选能读通的那张；**两次读数一致后才定稿**（本类图一次读常漏行）。
3. **无糖含量标注是常态**（中国 1+4 标签只强制能量+蛋白+脂肪+碳水+钠）→ 用**碳水差额法**估算添加糖：
   `添加糖 ≈ 本产品每100ml碳水 − 同类无糖基准的天然碳水`（豆浆基准用 CFCT id 338：1.1 g/100g），标注“medium 置信”并注明配料表未拍到。
4. **用致敏原反推配方**：营养表未列饱和脂肪时，若配料/致敏原**无乳**→ 按纯大豆脂肪比例（CFCT 338 豆浆实测 SFA 占脂肪 24.0%）折算；若**有乳**则用乳脂比例。
5. **宏量校核必做**：蛋白×4 + 脂肪×9 + 碳水×4 应接近标签 kJ÷4.184 的 kcal（本类产品常差 <1 kcal）。

## Pitfalls

- **Vision model may hallucinate nutrition numbers.** When two images show the same nutrition panel but differ slightly, prefer the clearer image. If values seem implausible (e.g., kJ and kcal don't match), flag it.
- **Aggregated databases are unreliable for fiber supplements.** They often return fiber=0 for psyllium/konjac products and show wildly divergent calorie estimates (15-544 kcal/100g). When the user provides a label, it is always the primary source — do not cross-validate against aggregated databases for pure-fiber products.
- **喷码 dates can differ from pre-printed date fields.** The inkjet-printed date (喷码) on the package is the actual production date; a pre-printed date field on the label design may be a template placeholder.
- **Brand names may appear differently across surfaces.** The jar front may show the registered brand while the nutrition-panel side shows subsidiary/co-branding names. Use the registered brand as the primary name and note others.
