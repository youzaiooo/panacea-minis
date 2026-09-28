---
name: weight-management-evidence
description: >
  热量预算与体重管理问答：热量赤字、基础代谢（BMR）、活动耗能、"吃够基础代谢"类问题。
  用户问减重速度、热量目标，或质疑某热量说法时加载。
---

# Weight Management Evidence

Evidence-backed numbers for calorie-budget discussions in Panacea's
weight/lipid management context. Complements the `panacea` and `health-coach`
skills (which hold the meal workflow); this skill owns the
*calorie-strategy evidence* so it is not re-searched from scratch each time.

## When to Use

- User proposes a calorie rule: "吃够基础代谢就行", deficit size, minimum intake.
- User asks whether activities "burn calories": 动脑/打游戏/睡眠.
- Weight-trend discussion needs a deficit/floor reference or a guideline citation.

## Key Numbers (verify in `references/energy-budget-evidence.md` before quoting)

| Item | Value | Source |
| --- | --- | --- |
| Recommended deficit | 500–1,000 kcal/day | NHLBI 1998 clinical guidelines |
| LCD floor, men | 1,200–1,500 kcal/day (1998) / 1,500–1,800 (2013 AHA/ACC/TOS) | guidelines |
| Weight-loss lipid benefit | 3–5% loss lowers TG & glucose; 5–10% improves LDL/BP | NHLBI page 2025-12 |
| BMR (men, Mifflin-St Jeor) | 10×kg + 6.25×cm − 5×age + 5; ±10–15% error → floor range, not exact | Mifflin 1990 |
| Brain at rest | ~20% of RMR (≈0.18 kcal/min at 1,300 RMR) | Raichle & Gusnard PNAS 2002 |
| Thinking/gaming increment | negligible vs baseline (single-digit kcal/h at most) | Messier review via SciAm 2012-07-18 |
| Sleep whole-body | ~15% below resting wakefulness; SMR vs BMR gap ~5% | Sharma & Kavuru 2010; PMID 15895522 |
| Brain in NREM vs REM | SWS = night's lowest activity; REM ≈ waking-like in limbic regions | Maquet 1997 J Neurosci; Maquet 2005 |

## Communication Patterns

- Endorse "eat at BMR as floor, never below ~1,500 kcal" when a daily calorie
  target ≈ the user's BMR. Treat the target as a budget, not a hunger-driven
  number; assess adequacy instead of dismissing "eating at BMR".
- Protein and fiber targets are set by weight/lipid goals and do NOT
  scale down with calories — say this explicitly when the user proposes eating less.
- Sedentary TDEE already includes "activity all day" intuition — warn against
  double-counting activity when estimating the deficit.
- 动脑/打游戏 burns almost nothing; the real trap is post-mental-work stress
  eating (+~200 kcal study, PubMed 18725427 — do NOT misattribute to "JAMA 2018").
- Sleep: don't chase a calorie surplus by sleeping less — sleep deprivation
  raises next-day intake (ghrelin/leptin). All brain/sleep costs are inside BMR.

## Evidence Rules

- Re-verify citations with 联网搜索与网页阅读 before quoting in a reply
  (per the `panacea` skill's evidence procedure).
- PubMed/PMC web pages are often cookie/reCAPTCHA-walled; use
  `eutils.ncbi.nlm.nih.gov` esearch+efetch with a browser UA as the fallback —
  it returns abstracts reliably.
- Present BMR/floor numbers as ranges with error bars, never as exact values.
