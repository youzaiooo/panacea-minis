---
name: health-coach
description: >
  记录并分析餐食、体重与补充剂，把数据落进个人健康档案。当用户申报吃了/喝了什么（文字或照片）、
  给出体重或身体测量、提到补充剂或药物、或要求当日营养汇总与目标对比时，使用本技能。
  本技能也是 Panacea（`panacea` 技能）的餐食记录主流程——任何饮食记录场景都应加载。
---

# Health Coach

Provide three focused capabilities for Panacea: meal analysis, weight tracking,
and supplement review. Follow the `panacea` skill for medical evidence, safety,
privacy, and Health Wiki governance. This skill does not replace those rules.

## Storage and Privacy

- The Health Wiki root is `/var/minis/memory/panacea-wiki` (unless the user has
  explicitly stored it elsewhere). All health data lives below it.
- Store health data only below the Wiki root; never create a parallel `health/`
  directory and never commit personal data to any repository.
- Preserve original files in `raw/` when the user provides a report or image.
- Separate user statements, label transcriptions, image observations, calculations,
  and clinical interpretation in every record.
- Do not create or change personal nutrition targets until the user or clinician
  supplies them. Do not infer age, sex, body metrics, disease status, or medication.

Initialize an empty Wiki safely with:

```sh
sh scripts/init.sh   # defaults to /var/minis/memory/panacea-wiki
```

The script only creates missing directories and templates. It never overwrites
existing records or calculates a diet prescription.

## Dietary Profile and Meal Workflow

Treat a user message or image that clearly describes food or drink consumed as a
meal-log event by default. Record it unless the user says not to record it, asks
to correct or delete it, or the message is only a hypothetical question. Keep the
profile at `dietary-profile.md`; create it from
`templates/dietary-profile.md` only when missing. Do not populate health goals,
restrictions, allergies, diagnoses, or clinician instructions unless the user has
explicitly supplied them.

For each log event:

1. Preserve any original image under `raw/images/` with a date/time-based name
   when it can be retained privately; reference it from the meal record. Do not
   store the image outside the Wiki root or treat its contents as a measurement.
2. Create one record per consumed occasion under
   `records/meals/YYYY-MM-DD-HHMM-short-name.md`. If the time or meal type is
   unknown, use the message-received time, mark it as provisional, and allow the
   user to correct it later. Do not silently assign breakfast, lunch, or dinner.
3. Link the meal record into `records/daily/YYYY-MM-DD.md` and recalculate only
   machine-maintained cumulative values. Preserve all user notes and prior meal
   links. Never merge distinct foods or overwrite historical source data.
4. Update `dietary-profile.md` only with durable, user-confirmed preferences or
   explicitly provided goals. Do not infer a pattern or target from one meal.

## Meal Analysis

For every meal photo, food description, menu, or package label:

1. Identify foods and separate packaged items, single ingredients, and mixed dishes.
2. Transcribe a visible nutrition label and net content exactly when supplied. Treat
   this as the primary nutrition source for that product.
3. For foods without a label, aggregate traceable sources: the manufacturer,
   restaurant, or regulator's official document, plus an authoritative
   food-composition database — China Food Composition Table (see
   `chinese-food-composition-sourcing`) or USDA FDC (see
   `authoritative-nutrition-sources`). Record the URL or citation and access
   date. Do not use search snippets, lifestyle articles, or uncited database
   entries as numeric sources.
4. Compare only values with the same basis (for example, per 100g or the same
   labelled serving). Do not average mismatched or materially conflicting values.
   Prefer a user-provided package label, then the product's official source. State
   any unresolved discrepancy and keep both source trails.
5. If a source has no match or fails (site blocked, entry missing), continue with
   the next-strongest authoritative source and label the result as web-derived,
   rather than silently inventing a replacement value.
6. Estimate a photo-only portion as a range, not a precise weight. State the visual
   anchors used (container, utensils, known package size, or plate dimensions) and
   mark confidence `high`, `medium`, or `low`.
7. For a mixed cooked dish, list its visible components and give a wider range. Ask
   for the key missing facts when they would materially change the result: recipe,
   oil, sauces, sugar, edible portion, package net content, or serving count.
8. Calculate the best estimate and range for energy, protein, carbohydrate, total
   fat, fiber, saturated fat, and sodium when the source supports them. Never invent
   missing micronutrients or pretend an image provides laboratory precision.
9. Complete the log event using `templates/meal-record.md` under
   `records/meals/YYYY-MM-DD-HHMM-short-name.md`. Rebuild that date's cumulative
   totals with `templates/daily-nutrition.md` under `records/daily/` without
   deleting user notes.
10. Compare totals with an explicit user- or clinician-provided target only. Otherwise
    report totals and state that no individualized target is on file.

Present the result with the food table first, then uncertainty, cited sources, and
one or two practical next steps. Do not present an estimated value as a measured
value.

## Weight Tracking

When the user provides a weight, waist circumference, or body-composition value:

1. Record the reported value, unit, date, measurement conditions, and source in
   `records/measurements/` using `templates/weight-record.md`.
2. Preserve all raw measurements. Calculate a trend only from dated observations;
   identify the time window and do not treat a short-term change as body-fat change.
3. Show the trend and data gaps. Compare it with a user- or clinician-defined goal
   only when one exists.
4. Do not prescribe a calorie deficit, medication, or treatment in response to a
   weight trend. Route medical causes, rapid unexplained changes, and treatment
   decisions through the `panacea` skill's safety boundaries.

## Supplement Review

Use this module only for a named supplement, its label, a logged dose, or a direct
supplement question:

1. Transcribe product, active ingredients, form, amount per serving, and the user's
   reported use without guessing a dose.
2. Research benefits, limitations, adverse effects, and interaction concerns using
   the `panacea` evidence-first order. Prefer guidelines, systematic reviews,
   clinical trials, and regulator or manufacturer label information; cite the
   source used.
3. Record a durable user-reported regimen under `records/medications/` only under
   the Wiki rules in the `panacea` skill. Clearly label it as user-reported.
4. Do not recommend starting, stopping, substituting, or changing a dose. For a
   possible drug interaction, pregnancy, kidney or liver disease, a child, or a
   serious adverse effect, direct the user to a pharmacist or clinician.

## Scope

This skill owns the *recording workflow* (meal/weight/supplement logging and
meal estimation). General medical Q&A, lab interpretation, symptom assessment,
disease management, prescribed medicines, and Wiki governance belong to the
`panacea` skill and its companion skills.

## Record Conventions

Use these paths when present:

| Data | Path |
| --- | --- |
| Personal baseline and preferences | `profile.md` |
| Dietary logging preferences and user-confirmed patterns | `dietary-profile.md` |
| User or clinician nutrition targets | `nutrition-goals.md` |
| Individual meals | `records/meals/` |
| Daily nutrition summaries | `records/daily/` |
| Weight and body measurements | `records/measurements/` |
| User-reported supplement use | `records/medications/` |
| Original private materials | `raw/reports/`, `raw/images/`, `raw/sources/` |
| Food product database (label-sourced) | `concepts/food-database.md` (index), `concepts/foods/` (product pages) |

## Food Product Database (Label Transcription)

**Panacea 的硬性规则：只要用户发送包装标签照片，必须转录并建档到 Wiki 产品库——不得只在餐食记录里带过。** 遗漏即视为错误。

When the user provides a packaged food label photo:

1. Copy the label image to `raw/images/` with a date-based name.
2. Transcribe the label EXACTLY — product name, brand, manufacturer, ingredients list, and nutrition facts per 100g — into a new product page under `concepts/foods/<short-slug>.md`.
3. The product name must match the label verbatim (e.g., "臻全麦吐司（面包）", not "全麦面包"). Same food type, different brand/product = separate page.
4. Reference the label photo path in the product page.
5. Update the index at `concepts/food-database.md` to include the new product.
6. In the meal record, reference the product page as a source rather than duplicating the full label transcription.

**来源分级：** 「实物包装标签照片」是**一级来源**；**商家/电商「商品参数」页截图是二级来源**，通常缺产品名、品牌、生产商、SC、执行标准、条形码、贮存条件——必须显式写入产品页的"验证状态"表（用户口述 vs 截图可见），并注明**实物标签优先**。中国标签强制项只有 1+4；若标签额外标示**饱和脂肪或糖**，记为该产品的规范加分项（可直接用于血脂评估）。

Read `references/evidence-sources.md` before doing nutritional calculations or a
supplement review.

## Safety Boundaries

- Do not claim clinical-grade accuracy from an image.
- Do not set aggressive calorie deficits, minimum intake, or therapeutic diets by default.
- Do not turn generic reference ranges into a diagnosis.
- Ask before making irreversible restructures or bulk changes to the health Wiki.
