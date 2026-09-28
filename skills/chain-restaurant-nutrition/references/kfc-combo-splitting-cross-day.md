# KFC Combo Splitting & Cross-Day Recording (learned 2026-08-21/22)

Complement to `kfc-china-nutrition-proxy.md` — how to record combo sets when the
user does NOT eat the whole set at once.

## Cross-day combo splitting

KFC combo sets (e.g. 我爱原味鸡套餐: 霸堡 + 吮指原味鸡×2, or 霸堡 + 原味鸡×1 + 可乐)
are often bought as a deal but eaten over multiple days ("原味鸡明天再吃").

Rules:
1. **Log only what was actually consumed today.** The deferred items (原味鸡 ×2)
   go into that date's `Planned` section in the daily record — never book the
   whole combo into one day's totals. One day's sat-fat budget (≤15g) would
   otherwise be blown by food eaten on a different day.
2. **The deferred items become a cross-day link.** Next session, check the prior
   day's daily/meal record (Planned / 待办 note) before assuming the food was
   never eaten — the user will say "今天不是都记录了吗" if you claim a gap that
   was actually logged from another chat surface (Telegram/WeCom/WebUI).
3. **Estimate the deferred portion when it is finally eaten** using the same
   proxy method (吮指原味鸡 ≈ 280 kcal / sat 3.5–4.5g per piece).

## Cross-session record check (general rule)

Meal logs can be written from ANY chat surface. Before telling the user a day is
unrecorded, check `records/daily/YYYY-MM-DD.md` AND `records/meals/YYYY-MM-DD-*`
AND `log.md` — use search_files by date pattern; `ls | tail` on one directory is
not enough. If the user corrects you ("都记录了啊"), search the Wiki again instead
of insisting.

## Example from 2026-08-21/22

- 8/21: user chose 套餐A + beer but deferred 原味鸡 ×2 to 8/22 → 8/21 daily logged
  霸堡+啤酒 only (sat 13.7g, at budget limit); 原味鸡 kept in Planned.
- 8/22: another session logged the deferred 原味鸡 240g (bone-in → edible ~70%)
  at lunch. The gap was real only in THIS session's context, not in the Wiki.
