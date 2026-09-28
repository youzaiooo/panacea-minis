---
name: lipid-management-evidence
description: >
  血脂/甘油三酯咨询的循证口径：指南分层数字、化验值沟通、餐厅与外卖的脂质估算、饱和脂肪预算。
  涉及胆固醇、甘油三酯、LDL/HDL、饱和脂肪、血脂×饮食的问题时加载。
---

# Lipid Management Evidence Bank

Use for Panacea TG/lipid consultations: cited guideline numbers, lab-expectation
conversations, and restaurant/takeout food estimation in a lipid context.
Education and meal support only — never diagnosis or treatment.

Complements the `panacea`, `health-coach`, and `authoritative-nutrition-sources` skills
(core meal-log workflow lives there). This skill carries the curated
evidence bank and techniques used in lipid consultations.

## When to Use

- User asks whether a TG/lipid value is "normal", "much", or improved by feel.
- User wants white rice / refined carbs / takeout in a TG-management context.
- User asks about 无糖饮料/人工甜味剂（健怡可乐、零度可乐等）安全性或减重作用 —
  see `references/artificial-sweetener-evidence.md` (JECFA ADI 40mg/kg, IARC 2B
  hazard-vs-risk framing, WHO 2023 conditional NSS guideline, JAMA 2022
  substitute-meta, per-user ADI math, caffeine/teeth/pKU caveats).
- Estimating a restaurant or branded cooked dish (grilled fish, fried items)
  where branded/commercial entries and USDA plain-cooked values diverge.
- User asks whether exercise offsets saturated fat / how exercise affects
  lipids — see `references/exercise-lipids-evidence.md` (acute exercise →
  postprandial lipemia; training → modest all-lipid improvements; dietary
  SFA→LDL is a separate, non-offsettable lever).
- Retrieving a classification table from a long clinical-guideline PDF.
- **User challenges a number or a food's worth** ("一个水果怎么可能有这么高的饱和脂肪",
  "低脂奶性价比很低，我还不如吃鸡肉") — see 「挑战处理 + 约束归一化」 below.
  Never edit a correct record to appease the challenge.
- Comparing protein sources against the sat-fat budget —
  `references/protein-source-sfa-cost.md` (per-gram-protein SFA table +
  iso-protein swap arithmetic).

## Evidence Retrieval: Large Guideline PDFs — Extract Then Grep

Do NOT page through a long PDF with a truncating web reader:

1. Fetch the PDF URL and save the full text to a local file first.
2. Search (grep) that saved file for the table's header labels
   (e.g. `边缘升高`, `1.7～2.3`, `生物变异`) — lands directly on the table.
3. Read a ±60-line window around the hit to capture table + footnotes.

Worked example: 中国血脂管理指南2023 表3 TG 分层 found by grepping
`边缘升高` in the saved extract. See `references/triglyceride-evidence-bank.md`.

## Lab-Expectation Communication Pattern ("我觉得已经正常了")

1. Give the precise band from the guideline table (e.g. 2.20 = 边缘升高:
   0.1 from 升高, 0.5 from 合适) — neither amplify nor endorse the user's guess.
2. Affirm the legitimate half of their optimism: TG responds fastest to diet
   (dietary intervention −20–50%, NLA 2022) — weeks of control can work.
3. "Feeling normal" ≠ measured value: single-measurement biological variability
   23–40%; TG is acutely sensitive to the last 1–2 days of food/alcohol — a
   splurge day can make the next morning's TG HIGHER than baseline.
4. Land on action: fasting 8–12 h recheck (no alcohol the day before), per the
   clinician's 定期复查 plan; never declare "normal" or "abnormal" ourselves.

Full cited numbers in `references/triglyceride-evidence-bank.md`.

## Restaurant / Branded Cooked Food Estimation: Bracket, Don't Average

Branded 烤/煎 entries include marinade and added oil and run high vs
USDA plain-cooked values. For a restaurant dish:

- Lower bound: USDA dry-heat plain-cooked value (e.g. Pacific mackerel cooked
  201 kcal/100g, FDC 171994).
- Upper bound: branded/restaurant grilled entries (e.g. 煎烤秋刀鱼 297,
  盐烤鲭鱼 302 kcal/100g).
- Best estimate: midpoint; report a wide plausible range and both source trails.
- Photo shows oil sheen (fish skin, glistening rice) → add ~4–8g cooking oil
  to mixed-dish estimates and note it as an image observation.
- Species unidentifiable from photo → record BOTH candidates' trails and ask
  the user (鲭鱼 vs 秋刀鱼) before finalizing.

## Combo / Multi-Person Set Promo Images

A promo screenshot of a 双人餐/套餐/随心选 set lists every included item but
never says how much is the user's. Settle attribution before doing arithmetic:

- State the assumed attribution and ask: whole set to one person, split across
the meals the user mentioned, or shared 1/N? Compute both readings when the
difference changes the verdict.
- Give PER-MEAL subtotals, not only the set total — daily budgets are checked
meal by meal, and the per-meal number is what tells the user what is left for
dinner.
- Official per-item values are high confidence; portion attribution and
completion are the dominant uncertainty. Say which is which.
- Judge the MENU, not only the chosen item: rank the same-category alternatives
by the user's binding constraint (for a ≤15 g sat budget, name the lowest-sat
breakfast sandwich and its sat value). "Is this one OK" is a weaker answer than
"here is the better pick on the same menu".
- Swappable sets: name ONE substitution with the largest sat-fat/fiber gain
(fried side → corn cup / apple slices) and mark it conditional on the set
allowing swaps.
- Items the chain omits from its own calculator (coffee, condiment packets) are
estimates: black brewed coffee ~0–5 kcal, one ketchup packet ~10 kcal / ~100 mg
Na. Ask about default sugar/syrup instead of assuming zero.
- A promo image is not a label: with no nutrition table in the image, every
number must come from the chain's official database or a cited source — never
from reading the picture.

## Takeout Recommendation Checklist (lipid context)

1. Search the wiki for past 外卖 meal records first — recommend repeatable,
   already-verified options with their recorded numbers.
2. Offer one "satisfy the craving" option (e.g. 白米饭套餐) with the pairing
   rule (protein + veg + moderate portion) rather than banning the food.
3. Short generic ordering rules: 酱汁分装; 无糖饮料、不配酒 (alcohol is a TG
   lever); 蒸/煮/烤 > 炸/糖醋/红烧/干锅; 加一份青菜.
4. Never create a meal record until consumption is confirmed (plan ≠ consumed).

## Fiber and Lipid Goals (evidence-based goal setting)

- Fiber lowers LDL by a REAL but MODEST amount: per +5 g/day soluble fiber
  LDL −8.28 mg/dL (Ghavami 2023, 181 RCTs, PMID 36796439); psyllium TC −0.28 /
  LDL −0.35 mmol/L (Zhu 2024, 29 RCTs, PMID 38688104). For LDL 4.33 that's
  roughly −5–8% — supporting lever, not the main one.
- Fiber does NOT meaningfully lower TG (Zhu 2024: TG ns). For TG-elevated
  users the levers are weight loss, sugar/fructose, alcohol, omega-3 — never
  sell fiber as a TG fix.
- Global reality: China ~10 g, Japan ~14 g, US ~16 g mean fiber/day — nobody
  hits 25 g. Set PROGRESSIVE targets (≥15 → 20 → 25), frame 15 g as above
  average, not a compromise. Set the progressive target with the user
  explicitly; never silently write it into `nutrition-goals.md`.
- Non-grain fiber strategy (culturally adapted): 车前子壳粉 5 g ≈ 4.5 g,
  豆类 100 g ≈ 4–7 g, 蔬菜/菌菇 300 g ≈ 6–8 g, 浆果 100 g ≈ 2–3 g. Do NOT
  push whole-grain staple swaps (米饭/面条/白面包 are cultural staples).
- Communication: never call fiber the "最大缺口/唯一硬伤" — when sat fat,
  weight, or added sugar dominate the risk picture, lead with those. Track added sugar (WHO <25 g) separately
  from total/natural sugar (fructose still matters for TG).
- Full citations: `references/fiber-lipid-evidence.md`.

## 挑战处理 + 约束归一化（user challenges a number or a food's value, 2026-09-20）

Two distinct user messages, two different procedures. Answer shape for both:
conclusion first, then ONE table sorted by the user's binding constraint, then
1–2 executable swaps, then the list of files changed.

### A. 「这个数字不可能」（challenge to an aggregate）

1. Re-verify against ≥2 independent sources (package label / CFCT /
   USDA / official source) before replying — neither accept nor dismiss on feel.
2. **Check what the number actually IS first.** The dominant misreading is a
   DAY total read as one item's contribution (a fruit appearing to carry the
   whole day's saturated fat). Recompute the item's own share and show both.
3. If it checks out, settle it with a **source-decomposition table**: every
   contributing item, its g of the disputed nutrient, and its % of the total.
   Nothing else ends a challenge.
4. If it is genuinely wrong, correct in place with the labelled-correction
   procedure and recompute every dependent aggregate.
5. **Never soften, average, or rewrite a correct record to appease a
   challenge.** Two databases disagreeing is a basis difference to be reported
   as a range with a named primary source — never split down the middle.
6. Say plainly which outcome it was ("未发现错误，无需更正" vs "你的算术成立").

### B. 「X 性价比低，我还不如吃 Y」（value-for-constraint question）

1. **Normalize to the unit the user is actually buying.** Under a ≤15 g sat
   budget that is **g SFA per gram of protein** (also useful: per 100 kcal, per
   g fiber). Rank all candidates in one table rather than arguing the pair.
2. **Compute the swap against the user's ACTUAL logged record**, not in the
   abstract: replace one logged item with an iso-protein alternative and quote
   the SFA/energy/protein deltas. Values + worked swaps:
   `references/protein-source-sfa-cost.md`.
3. **Always report the side-effect on the second constraint.** Cutting sat fat
   normally cuts energy too (skin-on→skinless poultry plus a dairy reduction
   removed ~190 kcal alongside ~5.7 g SFA). For a user who is chronically
   UNDER-eating, prescribe the replacement (whole grains/veg/fruit, which also
   recover fiber) — never a bare deletion that deepens the other gap.
4. **Never propose a sat-fat swap that pushes protein or fiber below target**,
   and state whether the swap is energy-neutral.
5. **Concede the arithmetic, keep the budget.** Dairy-matrix evidence (乳制品
   作为一类食物与 CVD 风险无关) lowers *food-level* risk; it does not exempt
   saturated fat from the budget. Both sentences belong in the same answer.
6. Flag the counter-intuitive orderings that change the plan — e.g. **eggs cost
   more SFA per gram of protein than low-fat milk**, so the dairy is not the
   worst line item; the cheapest cut is usually 带皮→去皮禽肉 (same protein, no
   loss) before any quantity reduction.
7. Evidence anchors for "this budget is worth optimizing": **Cochrane 2020,
   PMID 32827219** — lowering SFA intake reduced combined CV events, RR 0.83
   (15 RCTs, 56,675 participants, NNTB ≈ 56, GRADE moderate), with greater
   reduction → greater benefit; protein-source substitution lowers atherogenic
   lipoproteins, plant sources slightly more (**PMID 42451207**).

## Boundaries

- Cited sources only; state uncertainty. Numbers are for education and meal
  guidance, not personalized clinical conclusions.
- Do not set diet targets or interpret new lab panels without the clinician.
