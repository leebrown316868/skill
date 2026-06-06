---
name: text-to-todo
description: Convert user input into actionable todo steps with linked docs. Outputs TO_DO.md with [[]] links. Supports /text-to-todo sync for archiving.
---

# Text to Todo

## Quick Start

### 创建: `/text-to-todo <文本>`
解析输入 → 写入 TO_DO.md + docs/ → report（默认放入「长期to do」）

### 归档: `/text-to-todo sync`
扫描 `- [x]` → 归档到 `todo/archive/YYYY-MM.md` → 清理 TO_DO.md → 处理 todo/docs/（知识型→ai/raw/，任务型→删除）→ report

### 索引: `/text-to-todo index`
扫描 todo/docs/ → AI 主题归类 → 写入 `todo/KNOWLEDGE_INDEX.md`（覆盖）

## Step 1: Parse
- Max 5 top-level，太多则合并
- 保留用户原始措辞，不改写

## Step 2: Setup
```bash
mkdir -p todo/docs
```

## Step 3: Integrate into TO_DO.md
1. 读取现有 TO_DO.md，识别 `##` 分类
2. 新任务默认放入「长期to do」（不存在则创建），NEVER 放入「即刻to do」
3. 用 **4空格缩进** 展示层级拆解，深度不限直到最小可执行单位
4. 叶子节点可用 `[[]]` 链接到 `docs/` 详细说明

**执行节奏建议：** 拆完后询问用户每日投入/截止日期/难点 → AI 判断粒度（天/周/阶段），识别依赖关系，只展开近期计划（远期标"待展开"）。

## Step 4: Output docs
`todo/docs/<label>.md`：
```markdown
# <Label>
<说明，只基于用户输入>

## Details
<用户原始文本，逐字保留>

## 学习检查
- [ ] 模式归类：涉及什么设计模式/架构模式？
- [ ] 权衡对比：为什么选这个方案？
- [ ] 判断标准：下次依据什么决策？
- [ ] 自检：能描述给 AI 吗？能判断对错吗？能复用吗？
```
Rules：文件名从 `[[]]` 提取；只使用用户已提供的内容，不编造

## Step 5: Sync & Archive
`/text-to-todo sync`

1. 扫描 TO_DO.md 中 `- [x]` 项
2. 完成日期：从 `✅ YYYY-MM-DD` 获取，无则用当天
3. **父子检查：** 子 `[x]` 的父任务未 `[x]` 则跳过归档该子任务（跨层级同样适用）
4. 按完成月份归档到 `todo/archive/YYYY-MM.md`，保留原始分类标签
5. 从 TO_DO.md 移除已归档行，清理空行
6. **处理 todo/docs/：**
   - 从清理后的 TO_DO.md 提取未完成任务引用的 `[[]]` 集合
   - 遍历每个 `.md` 文件：
     - 被引用 → **保留不动**
     - 未被引用 → AI 判断：
       - **知识型**（可复用：技术原理/架构方案/方法论）→ 移除 `## 学习检查` 及 HTML 注释，保留标题和 Details → 移入 `ai/raw/<描述性文件名>.md`
       - **任务型**（一次性操作/签约流程）→ **直接删除**
7. 当月归档文件已存在则追加；无 `[x]` 则输出"没有待归档项"

**父子规则速览：**
```
- [ ] 父任务               → 子 [x] 不归档，留在TO_DO.md
  - [x] 子任务 ✅ 05-08
- [x] 父任务 ✅ 05-11      → 子 [x] 归档到 05 月
  - [x] 子任务 ✅ 05-11
```

**归档后结构：**
```
todo/
├── TO_DO.md       # 未完成 + 未到归档条件的已完成任务
├── archive/
│   └── 2026-04.md
└── docs/          # 仅保留被未完成任务引用的文件
ai/
└── raw/           # 从 todo/docs/ 移入的知识型文档
```

**Rules：**
- sync 时先 `mkdir -p todo/archive && mkdir -p ai/raw`
- 输出摘要：归档 N 条 + docs 处理（移入 N / 删除 N / 保留 N 条）
- 跳过的任务保留在 TO_DO.md 并说明原因

## Important Rules
- NEVER ask for confirmation; NEVER fabricate content
- NEVER put under "即刻to do" — 用户自行移动
- ALWAYS preserve user's original wording
- 拆解深度 AI 自主判断，4空格缩进，不用 `###`
- `[[]]` = Obsidian wikilink（无 `.md` 后缀）
