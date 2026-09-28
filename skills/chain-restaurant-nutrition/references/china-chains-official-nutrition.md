# China Chains: Official Nutrition Data Workflows

Verified 2026-08-16; Saizeriya section verified 2026-09-10. Chain scope: 食其家(Sukiya), 麦当劳中国(McDonald's), 肯德基中国(KFC), 汉堡王中国(Burger King), 萨莉亚(Saizeriya).

## 萨莉亚 Saizeriya — China menu images (no calories) + Japan official calorie table

- **China**: 官网（如广州 gz-saizeriya.com.cn「主菜单」flipbook，https://gz-saizeriya.com.cn/portal/list/index/id/19.html；上海 saizeriya.com.cn 更简）只发**菜单整页 JPG**，无任何营养数据。图片托管在 OSS 且带防盗链：curl 下载必须带 `-H "Referer: https://www.gz-saizeriya.com.cn/"`（注意 www 前缀，其他 referer 一律 403 AccessDenied）。拿到整页图后用读图方式识别菜名/价格/配菜构成。
- **Japan (official)**: `https://allergy.saizeriya.co.jp/allergy` = アレルゲン・カロリー塩分情報一覧（约 129 品：商品名 / エネルギー kcal / 食塩相当量 g / 过敏原标记）。页面是 React SPA，直接 fetch HTML 只有壳、网页阅读 拿不到表格；**用本机 headless Chromium 渲染后 dump DOM 再解析**：
  `chromium --headless=new --disable-gpu --no-sandbox --user-data-dir=/tmp/x --virtual-time-budget=25000 --dump-dom "https://allergy.saizeriya.co.jp/allergy" > dom.html` → 正则解析 `<tr>/<td>` 成 TSV。
- **口径**：中国菜单 ≠ 日本菜单。例：中国「香烤鳕鱼排」日本无对应品（日本 タラ 系列只有タラコ=鳕鱼籽制品）；日本「ほうれん草のソテー ≈ 223 kcal」是黄油系做法，与中国「烤菠菜（橄榄油+蒜）」不同，仅作交叉参考。中国菜品营养标记为**组分估算**（聚合库/USDA + 克重假设），说明中国菜单不公开热量。
- 2026-06 广州版常见单品参考：香烤鳕鱼排 1222·15元（图示裹面包糠烤制，配玉米粒/菠菜/双酱碗）；烤菠菜 7元（小份）；芝士烤菠菜 9元；QQ薯角 7元；芝士烤玉米 9元。

## 食其家 Sukiya — Japan official nutrition PDF (primary)

- China site `sukiya.jp/cn` publishes menu+prices only, NO nutrition. China has no dedicated menu page (homepage anchor `#menu` is the whole menu).
- **Official nutrition total table (Japan)**: `https://images.zensho.co.jp/materials/sukiya/allergen/nutrition.pdf` (Zensho = parent). Header carries 更新日 (e.g. 2026-08-04). Link lives on every Japan menu page under 栄養成分一覧.
- **Parsing pitfall**: 网页阅读 scrambles the PDF tables (numbers and item names in mismatched order). Fix: `curl` the PDF → `pdftotext -layout` → clean columnar text. Columns: サイズ | カロリー | たんぱく質 | 脂質 | 炭水化物 | 食塩相当量.
- Size mapping: China S/M/M-extra/L/XL/MEGA vs Japan ミニ/並盛/中盛/大盛/特盛/メガ — proxy only, mark medium confidence. 定食 have ミニ/並盛/大盛.
- Key official values (PDF 2026-08-04), kcal / protein / fat:
  - 牛丼: ミニ 464/14.8/16.0 · 並盛 695/21.7/23.4 · 大盛 908 · メガ 1365
  - 牛丼ライト (少饭多肉): ミニ 311/18.5/19.9 · 並盛 399/22.8/26.8 — lower kcal but HIGHER fat than plain 牛丼ミニ (16.0) — the "低卡" trap for lipid-conscious users
  - 鮭定食 並盛 572/23.4/10.6 (China 三文鱼套餐) — best lipid pick (salmon ω-3, sat ~2.5g)
  - 納豆定食 並盛 620/24.6/13.5 (China 纳豆套餐)
  - さば定食 並盛 687/24.3/23.0
  - 牛皿定食 並盛 831/31.7/30.8 (China 牛肉套餐 proxy)
  - 牛カルビ焼肉丼 variants 並盛 929–1075, fat 39–52g — fattiest menu class, sat ≈ fat×0.45–0.5, exceeds a full day's ≤15g sat budget in one bowl
  - 一品: おんたま/たまご 84/6.9/5.7 · 冷やっこ 88/7.4/4.7 · サラダ(无酱) 28 · オクラサラダ 37 · みそ汁 38 (盐 2.2g) · とん汁 114/7.9/5.6
- China menu extras: 低卡豆腐沙拉牛丼 (牛肉少量¥530/普通¥580/多量¥730) — Japan proxy 牛・お食事サラダ 並盛 359/15.5/22.1 (salad+rice+beef). **中国限定 SKU 例：温泉蛋日式烧鸟丼 / 时蔬单品 / 各种"日式 X 丼"——日本官方营养表均不收录**。如用户报告这类品项：
  1. 不要把"连锁酱汁标准化"等同于"有官方营养数据"——后者只对表内品项成立
  2. 标准化配方可作为固定参数收敛估算区间（例如焼鳥のタレ ≈ 酱油:味醂:酒:糖=2:2:1:1）
  3. 该 SKU 的宏量营养估算置信度应标 **lower**，并明确说明"非官方表覆盖"
  4. 用日本表内同类近似品（如 チキン・お食事サラダ 247 kcal）作为参考底线，加酱汁 / 加蛋调整

## 麦当劳中国 — official nutrition calculator (primary)

- `https://www.mcdonalds.com.cn/nutrition_calculator` — data updated 2025-04. **Data is embedded inline in the page HTML** as `al_nutrition_calculator.raw_data = {...}` (JS assignment). Extract: curl page → regex `raw_data\s*=\s*(\{.*?\});` → JSON.
- JSON shape: `ProductType.{id}.nutrition` = 14-element array; `Product.{id}` = title + ProductType id list. Field order (calibrated against product pages AND US-official sat-fat ratios — CORRECTED 2026-08-16, earlier draft had idx8 as sat fat which is WRONG):
  - idx0 = weight g · idx1 = energy kJ (÷4.184 = kcal) · idx2 protein · idx3 fat · idx4 carbs · idx5 sodium
  - **idx6 = saturated fat g** — verified by cross-checking sat/total-fat ratios vs US McDonald's official values: 麦乐鸡 17% (US ~17%), 薯条小 11% (US ~14%), 板烧鸡腿堡 24% (US ~24%), 麦辣鸡腿堡 21% (US ~17%). All match → idx6 is saturated fat.
  - idx7 = trans fat g (0 for all; 1g on cheese items 双层吉士/安格斯 = ruminant trans) · idx10 = cholesterol mg (板烧炒双蛋 448 = 2 eggs; 安格斯 113–116; 板烧 80) · idx11 = total sugar g (苹果汁 19, 优品豆浆 14, 无糖可乐 0) · idx13 = calcium mg (板烧 93 matches product page)
  - idx8, idx9, idx12 = UNIDENTIFIED — never cite. (idx8 looks sat-fat-like but ratios run 42–67% — implausible; do not use.)
- Sat fat verification method (reusable): compute sat/total-fat ratio for the item, compare with the same product type's US official ratio. Fried-in-low-sat-oil items ~11–21%; beef/cheese burgers 30–50%. Works because sat ratio is oil/ingredient-driven.
- Frying oil (official disclosure, mcdonalds.com.cn news 2025-07-21): "葵花卡诺拉油" (sunflower + canola blend; some stores add rice bran oil). USDA FDC 172336 canola = 7.4g sat/100g; sunflower ~10%, rice bran ~20%. This explains 薯条 11% sat ratio. DO NOT generalize "fried food is low-sat" to other chains — many use palm oil (40–50% sat).
- Product detail pages (`mcdonalds.com.cn/product/<slug>`) also show per-item tables (kJ/P/F/C/Na/Ca) — good cross-check.
- Key values (per item): 板烧鸡腿堡 391/23P/17F/1041Na (0油煎制, the diet pick) · 汉堡包 248/13P · 麦香鱼 325/16P (fried) · 吉士汉堡包 294 · 麦乐鸡5块 213/12P · 玉米杯小 53 · 苹果片 32 · 无糖可口可乐 0 kcal · 原味板烧鸡腿麦满分 246/15P (breakfast best) · 500大卡套餐 "苹板"支撑Pro 476/25P · 安格斯厚牛堡 696–707/44F (avoid) · 巨无霸 513 · 麦辣鸡腿堡 485 (fried).
- **早餐品项官方值**（同一 raw_data；官网页面不展示饱和脂肪，sat 取 idx6）— 重量 g / kcal / 蛋白 g / 脂肪 g / 碳水 g / 饱和脂肪 g / 钠 mg：
  - 原味板烧鸡腿麦满分 121 / 246 / 15 / 9 / 25 / **2.0** / 611
  - 脆薯饼 54 / 146 / 1 / 9 / 14 / **1.0** / 311
  - 脆香油条 49 / 202 / 5 / 12 / 19 / 2.0 / 230
  - 大脆鸡扒麦满分 136 / 361 / 16 / 17 / 35 / 3.0 / 804
  - 火腿扒麦满分 116 / 261 / 14 / 12 / 24 / 4.0 / 608
  - 双层原味板烧鸡腿麦满分 172 / 355 / 23 / 17 / 27 / 4.0 / 984
  - 猪柳麦满分 107 / 308 / 16 / 16 / 24 / 7.0 / 781
  - 原味板烧鸡腿炒双蛋堡 201 / 419 / 27 / 21 / 30 / 7.0 / 715
  - 猪柳蛋麦满分 155 / 387 / 23 / 21 / 25 / 9.0 / 846
  - 双层猪柳蛋麦满分 193 / 513 / 29 / 32 / 26 / 13.0 / 1,210
- **早餐排序口径**：原味板烧鸡腿麦满分（sat 2.0，0 油煎制）是早餐汉堡里最低的一款，其次脆香油条 2.0 / 大脆鸡扒 3.0 / 火腿扒 4.0；猪柳系 7–13 一次吃掉近全天饱和预算。给早餐建议时先给这一款并说明为什么，而不是只评价用户已点的那款。
- **咖啡缺口（勿重复找）**：鲜萃咖啡/鲜萃冰咖等现萃系列**不在营养计算器收录内**——官网有产品页但无营养表，饮品品类只有 12 项且无任何咖啡，sitemap 也只覆盖部分产品。按无糖黑咖啡 ≈ 0–5 kcal/份估算并标 low confidence；若默认加糖浆或用户自行加糖包，每包 +15–20 kcal（记得问，别默认）。

## 新品/限时品无官方数据时的处理（learned 2026-08-25，麦当劳马来咖喱薄皮肉骨鸡案例）

- 营养计算器数据滞后于新品（麦当劳中国计算器 2025-04 版，2026-08 新品未收录）；App 商品页通常也无热量标注
- 直连小红书搜索被登录墙/自动化检测卡死（CDP 渲染挂起）；360/搜狗/必应/百度公开索引基本扒不到新笔记
- **有效路径：** 用户在小红书/抖音刷到博主实测（如 186 kcal/69g/份）→ 截图存档 → **用户实测称重换算**（3块 81g → 186×81/69 ≈ 218 kcal）→ 标注 medium-low 置信度，明确「社区数据，非官方」
- 判断口径技巧：69g 带骨 = 单块合理重量；若「1份」拆成 3 块后每块仅 23g 则不现实——用物理合理性筛选解读
- 官方新品新闻页（mcdonalds.com.cn/news/）可确认品名、规格、价格、活动期，但无营养值

## 肯德基中国 — NO official web nutrition

- kfc.com.cn has no nutrition page (common paths 404). Circulating "官方热量表" (baidu health, fatsecret, 99健康网) are self-media/crowdsourced and CONFLICT (新奥尔良烤鸡腿堡 405 vs 578 kcal) — never fabricate or average. Give ordering principles (烤类 > 炸类, 去酱, 玉米沙拉/小份土豆泥 > 薯条) and offer image-based estimation for meal logging.

## 汉堡王中国 — NO official web nutrition

- bkchina.cn has product pages but no nutrition section. US bk.com data is a low-confidence proxy (different recipes/portions) — mark it clearly or give principles only (火烤牛肉排 fine; 去芝士去酱; avoid fried chicken burgers, onion rings, fries).
