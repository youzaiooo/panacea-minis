---
name: chain-restaurant-nutrition
description: >
  连锁餐厅菜品的官方营养数据查询（寿司郎/麦当劳/肯德基等）与外卖餐食估算。
  用户吃连锁餐厅、点外卖，或需要具体菜品数字时加载。
---

# Chain Restaurant Nutrition Lookup

Use when the user logs a meal from a restaurant chain (回转寿司/快餐/连锁餐饮)
and the meal needs numeric nutrition data. The chain's official per-item
nutrition is the primary source; food-composition databases and archived
snapshots serve as ingredient-level cross-checks. Complements `health-coach`
(which owns the meal record).

## Trigger

- Meal at 寿司郎/SUSHIRO, 藏寿司, 争鲜, or any chain that publishes nutrition
- User names specific menu items and wants kcal / protein / carbs / fat / sodium
- User asks about 食其家/麦当劳/肯德基/汉堡王 or any China fast-food chain — see the official source map in `references/china-chains-official-nutrition.md` (Sukiya Japan nutrition PDF via `pdftotext -layout`; McDonald's raw_data embedded in page JS incl. hidden sat-fat field, the 早餐 McMuffin/薯饼 table, and which items the calculator omits; KFC/BK publish nothing → principles only)
- Re-verify an archived McDonald's China value live before quoting it: `python3 scripts/extract_mcdonalds_cn_calc.py --keyword 板烧` (also 薯饼/麦满分/咖啡) fetches and parses the calculator directly — one call, no separate curl step.
- 萨莉亚/Saizeriya — China menu is image-only, no calories; Japan official allergen+calorie+salt table exists. See the 萨莉亚 section in `references/china-chains-official-nutrition.md` (GZ menu flipbook OSS Referer trick; Japan table via headless Chromium `--dump-dom`).

## Workflow

1. Try the chain's official site for per-item nutrition:
   - **Sushiro Japan publishes kcal per item on ANY store menu page**:
     `https://www.akindo-sushiro.co.jp/menu/menu_detail/?s_id=<any store id>`
     (e.g. `s_id=434`) — no store-selection interaction needed. Values are per
     贯/piece for nigiri; a 盘/plate is 2 pieces.
   - Sushiro China (`sushiro.com.cn`) and Taiwan (`sushiro.com.tw/Menu`) publish
     prices only — no nutrition. Use Japan values as the official proxy for
     standard nigiri, and say so in the meal record.
   - Nutrition PDFs may live under `www3.<domain>/pdf/menu/` (the allergy PDF
     pattern); guessing filenames (nutrition.pdf etc.) mostly 404s — don't burn
     time guessing. Go straight to a store menu page.
2. Extract the item→kcal table from the cached extracted markdown. Item name
   and kcal land on separate lines; also the page embeds literal `\n` sequences
   in some runs. Run `scripts/extract_sushiro_menu.py <cached-md>` (handles both
   forms) instead of hand-grepping.
3. Map user dishes missing from the menu to the closest official proxy item and
   mark confidence **low** in the meal record:
   - 鳗鱼天妇罗 → えび天にぎり (142 kcal/贯)
   - 鲷鱼头味噌汤 → 魚のアラの赤だし (136 kcal/碗, official fish-bone red-miso soup)
4. Third-party calorie sites are corroboration only, never primary evidence:
   - kalori.jp / letasu.com transcribe official data but fill gaps with AI
     estimates (badge 推定). A value that matches the official page exactly is
     good corroboration.
   - Blog tables (e.g. baliman.tw Sushiro calorie table) are self-media —
     secondary at best; they can help locate the official source.
5. Cross-check ingredients with CFCT/USDA. Known pitfalls:
   - Database hits can be a different product form than the name suggests:
     鲭鱼 413 kcal/100g is dried/fried — use 鲐鱼 (~155) for fresh mackerel.
   - fiber / saturated-fat fields are often 0 in search summaries; pull
     `detail` or patch from USDA before concluding a food has none.
   - 味噌汤 search returns only packaged dry mixes. Use the standard reference
     instead: ~40 kcal and 400–900 mg sodium per 240 ml bowl (wider for a big
     restaurant bowl with fish).
   - USDA FDC detail parsing traps (kJ vs kcal duplicate Energy, search omits
     nutrients, never trust an assumed fdcId): `references/usda-fdc-parsing-pitfalls.md`
6. Report official per-piece kcal as high-confidence for the item itself, but
   treat portion count (plates/pieces) as the DOMINANT uncertainty — always ask
   the user for the actual plate count before finalizing the daily record.
7. Sodium reality check for sushi meals: miso soup + soy sauce + shimesaba
   (salt/vinegar-marinated mackerel) dominate; give a range and mark low
   confidence rather than a precise number.

## Official values snapshot (Sushiro Japan menu, accessed 2026-08-13)

| Item (official name) | kcal/贯 | | Item | kcal/份 |
| --- | ---: | --- | --- | ---: |
| 厳選まぐろ赤身 (lean tuna) | 78 | | えび天にぎり (shrimp tempura) | 142 |
| 生サーモン (salmon) | 67 | | うなぎの蒲焼き (grilled eel) | 102 |
| 〆さば (marinated mackerel) | 111 | | 魚のアラの赤だし (fish-bone soup) | 136 |
| えび (shrimp) | 72 | | あさりの赤だし (clam soup) | 69 |
| たまご (egg) | 122 | | 茶碗蒸し | 77 |

The full official menu extract is archived in the private Wiki at
`raw/sources/sushiro-japan-menu-2026-08-13.md`.

## Evidence note

- ω-3 / triglyceride claim for fatty-fish meals: AHA scientific statement,
  Skulas-Ray et al., *Circulation* 2019, doi:10.1161/CIR.0000000000000709 —
  EPA+DHA 2–4 g/day lowers TG dose-dependently; the dietary recommendation is
  fatty fish ~2×/week. 2 pieces each of salmon+mackerel nigiri ≈ 0.5–0.8 g
  EPA+DHA.

## Pitfalls

- Don't treat kalori.jp 推定 values as official — verify against the official
  store menu page first.
- Nigiri official kcal is per piece (贯); a plate is 2 pieces. Halving or
  double-counting ruins the total.
- China store menus differ from Japan; state the proxy basis explicitly in the
  meal record and ask for the actual plate count.
