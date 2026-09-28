# McDonald's China — 麦辣系列官方数值与存档 JSON 本地查法（2026-08-30 验证）

Verified from the archived official calculator JSON
(`raw/sources/mcdonalds/mcdonalds-cn-raw-data-2026-08-25.json` in the private
health Wiki), 2026-08-30. 存档值已同步补入 `references/china-chains-official-nutrition.md` 的 Key values 行。

## 官方数值（存档 raw_data，primary）

| Item | ProductType | 重量 g | kcal | 蛋白 g | 脂肪 g | 碳水 g | 饱和脂肪 g | 钠 mg | 糖 g |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 麦辣鸡腿汉堡 | 26 | 208 | ~485 | 24 | 24 | 42 | 5.0 | 1,208 | 6 |
| 麦辣鸡翅（2块） | 19 | 73 | ~224 | 13 | 15 | 9 | 3.0 | 537 | 0 |

- 两样都是油炸（葵花卡诺拉油，饱和约占脂肪 21%）。对照：板烧鸡腿堡 sat 4.0 / Na 1,041（0油煎制）。
- 血脂管理用户点餐对照：日饱和预算 15g 时，麦辣鸡腿堡 5.0g 通常可容纳（余 ~1.8g/天）；再加 2 块翅（+3.0g）即超线（全天 ~16.2g），1 块翅（+1.5g）刚好。

## 存档 JSON 导航模式（本地优先，勿重复抓取计算器）

1. `search_files` 在 JSON 中搜商品标题（如 麦辣鸡腿汉堡）→ 目录条目在 `Product` 区，含 `ProductType: ["26"]`，但**目录条目没有营养数组**。
2. 营养数组在独立分区，按 type id 作键：`search_files` 搜 `"26": {`，读其 `nutrition` 14 元素数组。
3. 字段顺序：idx0 重量 g / idx1 kJ（÷4.184=kcal）/ idx2 蛋白 / idx3 脂肪 / idx4 碳水 / idx5 钠 / idx6 饱和脂肪 / idx7 反式 / idx10 胆固醇 / idx11 糖 / idx13 钙；idx8、9、12 未识别不可引用（详见 china-chains-official-nutrition.md）。
4. 用 `esearch` 无果时也可直接搜 `"title": "麦辣"` 这类片段定位；一次 grep 标题、一次 grep type id，两次即可取全。
