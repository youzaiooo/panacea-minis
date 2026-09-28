# Reusing Derived Numbers Across a Page Set

A derived number ("10 g of X ≈ +Y g of Z") is a *claim about a constant*. Copy it forward and you copy
the constant — including its error. Three failure modes, all seen in practice:

1. **A constant written too high** turns a comfortable budget into an apparent overrun, or the reverse;
   the direction of the conclusion flips on a number nobody re-derived.
2. **A ratio carried across categories.** "Saturated fat is ~30% of fat" is true for whole egg, not for
   dairy fat (~60–65%), fried noodle cake (~50%), or poultry skin. A ratio is valid only for the item
   it was measured in.
3. **A quantity copied with its unit basis changed** (per 100 g vs per piece, raw vs cooked, with or
   without peel/ice): the number survives, the meaning does not.

## Verified constants (re-derive before reuse; cite the id, not the page)

| Item | Value per 100 g | Source id |
| --- | --- | --- |
| Butter, salted | fat 81.11 g / **SFA 51.37 g** → 10 g butter ≈ **5.1 g SFA** | USDA FDC 173410 |
| Bread, whole-wheat, commercially prepared | 252 kcal / 12.45 P / 3.5 F / **SFA 0.722** / fiber 6.0 (SFA/fat ≈ 20.6%) | USDA FDC 172688 |

## Procedure before reusing a derived number

1. Find the underlying constant in an authoritative source (composition database item id, label, or
   guideline figure) — not in an earlier page of the same Wiki.
2. Recompute the derived value; if it differs from the earlier page, treat the earlier page as wrong.
3. Archive the verified constant under `raw/sources/` with the id it came from, so the next session
   inherits the source rather than an assertion.

## Correcting an earlier page that used the wrong constant

1. Patch that page **in place**: new value + the constant and its source + the old value quoted once
   (`原写 "≈7 g"`) and a labelled `Agent 更正`. Never delete or silently overwrite the old text.
2. **Recompute every dependent aggregate** — running daily totals, summary lines, index descriptions,
   and any hypothetical-scenario upper bound quoted from the old number.
3. Log the correction in the *current* entry (old value → new value → source). Append-only/historical
   entries keep their original text; do not retro-edit them.
4. Report the correction to the user explicitly; a silently fixed number teaches them nothing and
   makes the earlier report look like it was right.

## Validating an estimate you are about to restate

Re-deriving from the same constant only proves the arithmetic is repeatable — it cannot catch the
assumption baked into the original method. Before restating a Wiki estimate, re-derive it through a
**different method**: if the page scaled a nutrient ratio, blend the ingredient composition instead
(or the reverse). Agreement between two independent methods is a real confidence upgrade and deserves
one line in the record (`independent re-derivation agrees ✅`); disagreement means one method is wrong,
so keep the published range wide and say which method produced which end rather than silently picking one.
