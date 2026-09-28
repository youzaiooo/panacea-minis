---
name: health-coach-clinical-context
description: >
  当每日营养汇总缺少营养目标（nutrition-goals.md 为空）时，检查 profile.md 中的病史与医生指示，
  为每日汇总的 Interpretation 一节提供临床背景。用户有既往病史且汇总缺少目标时必须加载。
---

# Clinical Context Fallback for Daily Summaries

## Trigger

When `nutrition-goals.md` has no numeric targets set (all fields empty), but
`profile.md` contains health conditions, diagnoses, or clinician instructions.

## Problem

The standard health-coach daily summary template says "no target on file" when
`nutrition-goals.md` is empty. But users may have registered their health
conditions and clinician guidance in `profile.md` and reasonably expect those
to be acknowledged in every meal review. Saying only "no target on file" feels
dismissive and ignores registered information.

## Rule

Before writing a daily summary's Interpretation section, check both
`nutrition-goals.md` AND `profile.md`:

1. If `nutrition-goals.md` has numeric targets → use them (standard behavior).
2. If `nutrition-goals.md` is empty BUT `profile.md` has health conditions or
   clinician instructions → present "clinical context only" with a brief summary
   of the relevant conditions/instructions, rather than "no target on file."
3. If both are empty → "no target on file" is appropriate.

Never infer numeric targets from clinical context. Only reference what is
explicitly recorded.

## Example

When `profile.md` says:
  - 高脂血症混合型：TC 7.03, LDL-C 4.33, TG 2.20
  - 医生建议：饮食和生活方式调整，暂不需药物

The daily summary should say:
  "Target status: clinical context only — 轻度混合型高脂血症，医生建议饮食调整"
  NOT just "未设定"
