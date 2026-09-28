---
name: food-safety-storage
description: >
  食品安全与储存问答：切开水果能放多久、开封调味品保质期、剩菜剩饭能否再吃。
  用户问"还能不能吃""能放多久"时加载；答案须来自官方来源并存档。
---

# Food Safety Storage

Use when the user asks "这个还能不能吃/能放多久" — cut fruit,
opened condiments (miso, sauces), leftovers, fridge items suspected of
spoiling. These are recurring consumer questions; answer from official
regulator/industry sources, not self-media, and save a source trail to the
health Wiki under `raw/sources/`.

## Evidence ladder for food-safety storage claims

1. **Chinese official regulators** (primary for China-relevant answers, and they scrape
   well): 省/市市场监管局 consumer alerts (消费提示) on `*.gov.cn`, e.g.
   济南高新区市场监管部、河南省市场监管局. Find via 联网搜索
   （query: "<食物> 消费提示 市场监管"；prefer `site:gov.cn`）.
2. **Industry associations** for fermented/processed foods: 全国味噌工業
   協同組合連合会 (zenmi) guidance pages, plus manufacturers' official
   pages (Marukome/マルコメ for miso, brand official sites for others).
3. **US FDA/USDA/CDC** for the 2-hour room-temperature rule etc. — but their
   pages (foodsafety.gov, CDC, FSIS) frequently return antibot 500s or have
   moved URLs. Don't burn calls; for China-relevant answers the CN regulator
   sources above are sufficient and stricter.

Reject baidu-health/wenku/self-media as evidence; they may only locate the
official source.

## Key reference numbers (worked examples, all source-trailed 2026-08)

| Question | Verdict & numbers | Source |
| --- | --- | --- |
| 切开西瓜保存 | 室温 ≤2h（夏季超 4h 风险显著）；保鲜膜密封冷藏最好 ≤12h、最长 ≤24h；再吃前削表层 ~1cm；发黏/异味/渗水→弃 | 济南高新区市场监管部《关于西瓜的食品安全消费提示》2026-05-14；河南省市监局夏季风险提示 2026-06-22 |
| 开封味噌放冰箱 | 赤味噌最耐存；开封冷藏目安 ~3 个月，冷冻 1–2 年（不结冰）；表面褐变=美拉德反应正常；薄白膜=产膜酵母无害（刮 5mm）；黑/绿/粉霉、异臭、拉丝→弃；减盐/だし入り版保存性更低（1–3 月） | 味噌工业会指南页 + マルコメ官方保存页 |

Common patterns to reuse:
- 开封后 ≠ 标称保质期：label shelf life assumes unopened; opened life is
  shorter and depends on food matrix (salt/ferment = durable, low-salt = short).
- 肉类/肉丸变质：user correctly discards — affirm, never suggest trimming
  mold off meat (unlike hard cheese). Suggest checking同批库存 and fridge
  hygiene.
- Save every researched verdict as `raw/sources/food-safety-<topic>-<date>.md`
  with URLs + access date + the user-scenario application.

## Cross-check numbers with the food-data workflow

When a spoilage question concerns a food also used in a meal record (miso,
meatballs), update the meal record + dietary-profile fridge stock after the
verdict: remove/correct the item, note the disposition (丢弃/挖除表层后食用),
and preserve the user's own words in the record.

## Boundaries

- Education and consumer-safety guidance only. No diagnosis: if someone
  reports symptoms after eating suspect food (vomiting, diarrhea, fever),
  route to medical care per the `panacea` skill's escalation rules.
- CN regulator guidance is deliberately conservative (24h fridge rule vs US
  3–4 days); present the CN number as primary for China-relevant questions and note the
  difference when asked.
