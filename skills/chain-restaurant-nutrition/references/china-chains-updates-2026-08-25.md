# China Chains: 2026-08-25 Session Updates — McDonald's fries/new items + 食野

Session-derived additions to `china-chains-official-nutrition.md` (2026-08-25,
full raw_data extraction + new-item hunt for 马来咖喱风味薄皮肉骨鸡).

## McDonald's China — fries & verified extras (official raw_data, accessed 2026-08-25)

- **Fries official China values**: 小 210 / 中 289 / 大 379 kcal. 大薯 379 is
  ~100 kcal BELOW the US-official proxy (480) used in the 2026-08-23 meal
  record — always prefer China raw_data over US proxies, and offer to correct
  older records when the discrepancy surfaces.
- Verified extras (same extraction): 板烧鸡腿堡 sat 4.0g official (8/23 record
  used 3.2g estimate — official wins) · 麦乐鸡5块 213 kcal/12P/12F/13C/Na 422/sat 2.0 ·
  玉米杯小 72g/53 kcal/sat 0 · 玉米杯大 118g/87 kcal · 无糖可乐 小326g Na25 /
  中443g Na35 / 大642g Na53 (all 0 kcal) · 薄皮焦香V翅 85g/192 kcal/17P/11F/sat 2.0/Na 594 ·
  双层深海鳕鱼堡 209g/485 kcal/28P/21F/sat 5.0 · 麦香鸡 370/15P/17F · 猪柳麦满分 308/16P ·
  麦乐鸡4块 (~160 kcal/12P class).
- Full JSON archived: `raw/sources/mcdonalds/mcdonalds-cn-raw-data-2026-08-25.json`
  (private Wiki) — search locally by product title before re-fetching.

## New / limited-time items (launched after the calculator's 2025-04 freeze)

- NOT in `raw_data`; product pages are JS-rendered (web_extract → news list +
  footer only, no nutrition table); App product pages usually show NO nutrition
  label (user-verified 2026-08-25 for 马来咖喱风味薄皮肉骨鸡 3块 ¥17).
- Third-party calorie sites have nothing for items < ~1 week old — only taste
  reviews. Skip the search, go straight to same-工艺 proxy estimation, label
  low confidence, and ask for an App screenshot in case a label exists.
- Verified proxy map (2026-08-25):
  - 马来咖喱风味薄皮肉骨鸡 (3块) → 薄皮焦香V翅 per-piece (~200–260 kcal/块;
    3块 ~600–780 kcal / P 36–48 / sat ~7.5–10.5g / Na ~1,500–2,100mg).
    Fried + curry-marinated = high sat + high Na: swapping it into a normal
    dinner typically blows the ≤15g/day sat budget — flag the trade-off.
  - 新加坡蟹酱风味海鲜堡 → 麦香鱼 325 kcal.
  - 泰式炭烤风味猪猪堡 → 猪柳麦满分 308 / 麦香鸡 370 kcal.
- Same batch of seasonal items (8/24–9/15, Yuy玉联动/随心配/大堡口福):
  美禄可可雪冰 (+3元换购), all without published nutrition.

## 食野 (SAY YEAH) — health-brand 荞麦面/沙拉 bowls (健康轻食类外卖选项)

- No public nutrition site; store product pages publish only **kcal/100g
  claims**, no per-portion weight. Treat the claim as primary energy density
  (user-reported, mark it); weight is the dominant uncertainty.
- **Bowl convention: ~420 g/份** — established 8/19 (store-confirmed 420g),
  reused 8/21 & 8/25 with the same bowl shape; energy = kcal/100g × 4.2,
  ±60 kcal sensitivity (380–500g).
- Store kcal/100g ladder: 鸡胸肉荞麦面+牛肉酱 106 (8/19) → 傣味打抛鸡肉荞麦面 90.1
  (8/21) → 黑椒牛柳荞麦面 84.2 (8/25). Macro split is always component-estimated
  (store gives energy density only) — 牛柳版 ~30P/50C/10F/7 fiber/3.2 sat/800Na per 420g.
- Evidence format: user often sends the **product-page screenshot** (price +
  kcal/100g claim), not the food photo — acceptable as the store-claim source;
  note "商品页截图，非实物" and keep bowl-size inference at medium confidence.
- Variants: 魔芋鸡肉燕麦饺蔬菜沙拉 (~355 kcal, 8/24) — salad class, 8-veg mix;
  bowls carry mixed 彩椒/南瓜/玉米/杏鲍菇/花椰菜 — credit ~5–9g fiber.
