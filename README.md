# Panacea for Minis 🩺

把 **Panacea —— 个人健康助手** 移植到 [Minis](https://github.com/OpenMinis/OpenMinis)（iOS 上的本地优先 AI Agent）的可分发技能包。

每位家人可以在自己的 iPhone / iPad 上拥有一个健康 AI：数据 100% 存在本机、彼此独立、不连任何服务器。
**本仓库不含任何个人数据** —— 所有人的档案从空白开始，只属于使用者本人。

## 能力

- **饮食记录与评估**：把吃了什么（文字或照片）发给 Minis，自动估算热量/营养（带范围与置信度）并归档
- **个人健康档案**：在设备本地维护 profile、餐食、体重、化验、症状、产品库（markdown wiki）
- **个性化标准**：只按你（或医生）写进档案的目标做对比；AI 不会擅自替你定目标
- **医疗健康问答**：术语、化验单、用药、血脂、减重、补剂——循证优先、引用真实来源、不做诊断
- **安全边界**：红旗症状立刻建议就医；只用现代循证医学

## 安装（3 步）

### 第 1 步：准备 Minis

App Store 安装 Minis，并在设置里配置你的模型 API Key（本包不含 Key）。

### 第 2 步：让 Minis 安装技能包

在 Minis 对话里发送：

> 帮我安装 Panacea 健康助手技能包。执行：
> `wget -qO- https://raw.githubusercontent.com/youzaiooo/panacea-minis/main/install.sh | sh`
> 如果 wget 报错就用 curl —— `curl -fsSL https://raw.githubusercontent.com/youzaiooo/panacea-minis/main/install.sh | sh`；
> 如果提示证书问题，先执行 `apk add ca-certificates`。

也可以只把仓库地址发过去：「读一下 https://github.com/youzaiooo/panacea-minis ，按 README 安装」。

装好后，`/var/minis/skills/` 下会有 16 个技能目录。如果 agent 需要手动安装，见文末「给 Minis Agent 的安装细则」。

### 第 3 步：初始化健康档案

在对话里说：

> 初始化我的健康 wiki

（或手动执行 `sh /var/minis/skills/health-coach/scripts/init.sh`）

然后说「带我填一下健康档案」，跟着问题录入基本信息。之后就可以正常使用了：
发饮食照片、体重、化验单、症状或任何健康问题，Panacea 会记录、查证并归档到本地。

## 仓库结构

```
install.sh          # Minis 内一键安装脚本（下载 tarball → 复制到 /var/minis/skills/）
skills/
  panacea/                             # 主技能：身份、边界、证据优先、总工作流
  health-coach/                        # 餐食/体重/补剂记录流程、init.sh、模板
  health-wiki-record-maintenance/      # 档案维护的机械步骤（表格/索引/计数/日志）
  health-coach-clinical-context/       # 无目标但有病史时的临床背景
  chinese-food-composition-sourcing/   # 中餐数值（中国食物成分表 CFCT）
  chain-restaurant-nutrition/          # 连锁餐厅/外卖
  authoritative-nutrition-sources/     # USDA / 官方来源与反爬替代路径
  food-label-transcription/            # 包装标签转录与产品库建档
  lipid-management-evidence/           # 血脂/甘油三酯循证口径
  weight-management-evidence/          # 热量赤字 / BMR / 耗能问答
  supplement-evidence/                 # 补剂（鱼油等）循证框架
  biomedical-literature-retrieval/     # 原始文献检索（Europe PMC）
  guideline-critical-appraisal/        # 指南可信度分层评估
  symptom-report-handling/             # 症状报告固定流程（红旗→建档→就诊指征）
  food-safety-storage/                 # 食品安全与储存
  wiki-write-verification/             # 写盘核对（链接/计数/截断）
```

## 数据与隐私

- **零个人数据**：仓库里没有任何健康数据；每个人从空白 wiki 起步。
- **本地优先**：健康档案在设备本地，使用minis的外部挂载文件夹（需用户配置），例： `/var/minis/memory/panacea-wiki`，不经过任何服务器。
- 联网仅用于查询公开来源（文献、官方营养数据），并会把来源存档到本地 `raw/sources/`。
- 数值来源优先级：你提供的包装标签 → 官方来源 → 权威食物成分库（CFCT / USDA）。

## 说明

- 本包不含模型 API Key（在 Minis 里自配）。
- 只提供健康教育信息与记录辅助，**不构成医疗建议**；用药与治疗请咨询医生/药师。

---

## 给 Minis Agent 的安装细则（手动方式）

如果一键脚本不可用，请按以下步骤安装：

1. 下载并解压仓库：

   ```sh
   cd /tmp
   wget -q -O pm.tar.gz https://github.com/youzaiooo/panacea-minis/archive/refs/heads/main.tar.gz
   tar -xzf pm.tar.gz
   ```

2. 把 16 个技能目录复制到 Minis 全局技能目录：

   ```sh
   mkdir -p /var/minis/skills
   cp -R /tmp/panacea-minis-main/skills/* /var/minis/skills/
   ls /var/minis/skills
   ```

   预期看到：`panacea health-coach health-wiki-record-maintenance ... wiki-write-verification`（共 16 个）。

3. 初始化空白健康档案：

   ```sh
   sh /var/minis/skills/health-coach/scripts/init.sh
   ```

   预期输出 `Health Wiki is ready at /var/minis/memory/panacea-wiki`，并在该目录下生成
   `profile.md`、`nutrition-goals.md`、`dietary-profile.md` 以及 `records/`、`raw/`、`concepts/` 子目录。

4. 验证技能可被读取：随机打开一个技能文件（如 `/var/minis/skills/panacea/SKILL.md`），
   确认开头有 `name:` 与 `description:` 的 frontmatter。

5. 告知用户：安装完成，可以对你说「初始化我的健康 wiki」「带我填一下健康档案」开始使用。
