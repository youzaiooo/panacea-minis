---
name: biomedical-literature-retrieval
description: >
  取医学与营养学原始文献：优先 Europe PMC REST API（而非网页抓取），失败时带退避重试。
  需要原始研究、试验或指南原文来支撑回答时加载。
---

# Biomedical Literature Retrieval

Panacea 的证据优先流程要求「真正读到原文」。本 Skill 只管**怎么把原始文献取到手并逐条转录**；
证据分级与话术在 `panacea-health`，数值与饮食结论在 `weight-management-evidence` /
`lipid-management-evidence`。

## 何时用

- 需要系统综述/RCT/指南原文的摘要或全文来支撑一个医学、营养、药物结论。
- 网页阅读 对出版商页失败（PMC 返回 `Cookies must be enabled`；BMJ/Nature 类返回
  `document_antibot` / retry 超限）——**这时不要去猜，换 API 通道**。
- 需要**逐条转录表格/公式**（如预测公式汇总表）而不能靠记忆或二手转述。

## 先搞清楚：网页版和 API 是两条路

出版商/PMC **网页**被反爬是常态，**API 通道稳定**。不要把「网页取不到」当成「文献取不到」，
也不要退而引用搜索结果的摘要文字——那是二手转述，不能当证据。

## 流程

1. **搜索**：`GET {BASE}/search?query=<q>&resultType=core&format=json&pageSize=N`
   - `BASE = https://www.ebi.ac.uk/europepmc/webservices/rest`
   - `resultType=core` 才会返回 `abstractText`；缺它只剩题录。
   - 查询语法：`TITLE:"..."` / `AUTH:"..."` / `PMCID:PMC1234567`；
     用 PMID 时加 `AND SRC:MED`（例：`EXT_ID:24847670 AND SRC:MED`）。
   - 一次拿多条时用 python `urllib` + 浏览器 UA；题录字段取
     `title` / `journalInfo.journal.title` / `pubYear` / `pmid` / `pmcid` / `abstractText`。
2. **取全文**（仅开放获取；从搜索结果里的 `pmcid` 判断）：
   `GET {BASE}/{PMCID}/fullTextXML`。Nutrients/MDPI、PLOS、多数 OA 期刊可拿到；
   无 `pmcid` 或付费墙 → 退回「只引用摘要」并**明确标注局限**。
3. **提取表格/公式**：去标签（`re.sub(r"<[^>]+>", " ", xml)`）→ 归一空白 → 按关键词
   （`"Table 1"` / `"kcal/d"` / `"= "`）打印 ±500 字符窗口。公式汇总表通常在 `Table N` 附近。
4. **落盘**：把摘要/公式表存到健康 Wiki 的 `raw/sources/<topic>-sources.md`，并在概念页
   的 Sources 表里逐条引用（组织/期刊 + 年 + PMID）。

## 转录纪律（这一节是最容易出错的地方）

- **逐条转录，标注出处位置**（如「取自原文 Table 1」）；**绝不凭记忆补系数**。
- **未取得系数的文献**：只引用它的结论方向，并写明「未取得其系数，故不列数值」。
- **检索无果也是结果**：若没有研究某个问题（例：某输入误差的敏感度），明确写「未检出该主题文献，
  改用模型计算」，并把计算**标注为 Panacea 模型计算、非文献结论**——不要装成文献结论。
- **记录未采用的命中及原因**（人群不匹配、设计不符等），便于复核。
- 摘要里的数值直接用；**自己要做的换算/代入要单独标为模型计算**。

## 陷阱

- **只读摘要就用**：系统综述的结论方向可用，但具体阈值/公式往往在表里，必须开全文。
- **人群不匹配**：西方人群的公式/阈值不自动适用于中国用户——先看研究对象，再决定能否引用。
- **把「我没找到」写成「不存在」**：换关键词与作者检索再下一次结论。
- **手上只有一个 PMID 时**：用 `EXT_ID:<pmid> AND SRC:MED` 验证题录，别把近似标题当成同一篇。
