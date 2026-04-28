---
name: text-to-todo
description: Convert user input text into minimal actionable todo steps with linked docs. Use when user wants to break down text into steps, create todos from requirements, or structure a plan from a paragraph. Outputs TO_DO.md with [[]] links to individual doc files. Fully automatic — no confirmation needed. Supports /text-to-todo sync to archive completed todos.
---

# Text to Todo

Break user input into minimal executable todos (max 5), output to `todo/TO_DO` with internal links to detail docs. **Fully automatic — parse, categorize, write, done.**

## Quick Start

### 模式一：创建 todo
1. `/text-to-todo <文本>` — 解析输入，写入 TO_DO.md + docs/mini_todo
2. Report summary to user

### 模式二：归档已完成的 todo
1. `/text-to-todo sync` — 扫描 TO_DO.md 中 `- [x]` 项
2. 归档到 `todo/archive/YYYY-MM.md`
3. 清理 TO_DO.md 和 mini_todo/
4. Report summary to user

### 模式三：生成知识索引
1. `/text-to-todo index` — 扫描 `todo/docs/` 下所有 .md 文件
2. 读取每个文件的标题和内容，由 AI 根据内容语义进行主题归类（不要硬编码分类，根据实际内容决定）
3. 输出到 `todo/KNOWLEDGE_INDEX.md`

**索引格式**（分类由 AI 自主判断，以下为示例）：
```markdown
# 知识索引

## 容器与镜像
- [[docs/Kaniko构建镜像]] — CI 环境无 daemon 构建镜像
- [[docs/skopeo基本原理]] — OCI Distribution Spec 直连仓库

## 搜索与检索
- [[docs/向量检索迁移]] — 从关键词匹配升级语义检索

## 安全
- [[docs/skopeo安全审查]] — 凭证权限、TLS、流量审查

## 待归类
- [[docs/xxx]] — 内容摘要
```

**规则**：
- 同一主题下按学习顺序排列
- 无法归类的放入"待归类"
- 如果某个 doc 文件内容为空或只有模板占位符，标注为"未填写"
- 每次运行覆盖 `todo/KNOWLEDGE_INDEX.md`，不追加

## Core Workflow

### Step 1: Parse User Input

Extract distinct actionable items from user text. Rules:
- Upper bound on todo count: enough to cover the scope without overwhelming, merge related items when there are too many independent steps
- Each todo = smallest executable unit user can perform, but don't over-split a coherent task into fragments
- Preserve user's original wording — do NOT rewrite or reinterpret

### Step 2: Create Directory Structure

```bash
mkdir -p todo/docs todo/mini_todo
```

### Step 3: Integrate into `todo/TO_DO`

**First, read existing `todo/TO_DO` and analyze its structure.**

1. If file does not exist → create new with standard format
2. If file exists → identify existing categories (sections separated by `##`)
3. Determine which existing category each todo belongs to based on semantic match
4. Insert todos under the most relevant existing category
5. **NEVER** create a new category — always fit into existing ones
6. If no existing category fits → ask user which category to use, or confirm creating a new one before doing so

#### Long-term Todo → Mini Todo Breakdown

When a todo is placed into a long-term category (e.g. "长期to do", "规划中", etc.):

1. Break the long-term todo into **smallest executable mini-todos** (no quantity limit)
2. One long-term todo = **one md file** in `todo/mini_todo/`, containing all its mini-todos
3. The `[[]]` link in `TO_DO.md` points to `todo/mini_todo/<long-term-name>.md`
4. Each mini-todo inside that file has its own `[[]]` link pointing to `todo/docs/` for explanation
5. The long-term todo itself gets no `[[]]` link to `docs/` — its detail lives in the mini-todos
6. **生成执行节奏建议**：拆完 mini-todos 后，先问学习者再给建议

**执行节奏引导提示词**（拆完 mini-todos 后自动触发）：

> 已拆完 X 条 mini-todo。在排每日计划之前，我需要了解你的情况：
> 1. 你每天能投入多少时间？
> 2. 有没有截止日期？
> 3. 这些 mini-todo 里有没有你觉得特别难/特别容易的？
>
> 基于你的回答，我会给出执行节奏建议（按天/按周/按阶段），你确认后再生成计划表。

**生成计划时 AI 应自主判断**：
- 计划粒度（天/周/阶段）：根据总工作量 + 学习者每日可用时间 + 截止日期综合判断，不硬编码规则
- 排列顺序：识别 mini-todo 之间的依赖关系，有依赖的串行，无依赖的可并行或自由安排
- 只展开近期计划：远期计划会因实际进度偏离，只详细排近期可执行的范围，其余标为"待展开"，等当前阶段完成后再规划下一阶段
- 预估时间应基于 mini-todo 的实际难度，不是一刀切

Structure（由 AI 根据上述判断动态生成，以下为示例）：
```
todo/TO_DO.md (long-term section):
- [ ] 换微服务 [[mini_todo/换微服务]]

todo/mini_todo/换微服务.md:
# 换微服务

## 执行计划
| 天数 | mini-todo | 预估时间 |
|:----:|:---------|:--------|
| Day 1 | 调研gRPC与REST适用场景 | 30min |
| Day 2 | 技术选型对比文档 | 45min |
| Day 3 | 搭建原型验证可行性 | 60min |

## Mini Todos
- [ ] 调研gRPC与REST适用场景 [[docs/换微服务-调研]]
- [ ] 技术选型对比文档 [[docs/换微服务-选型]]
- [ ] 搭建原型验证可行性 [[docs/换微服务-原型]]

todo/docs/换微服务-调研.md:
# 换微服务 - 调研
<explanation from user input>

todo/docs/换微服务-选型.md:
# 换微服务 - 选型
<explanation from user input>
```

#### Immediate / Short-term Todo (non-long-term category)

When a todo is placed into an immediate category (e.g. "即刻to do"), use the standard flow:
- `[[]]` link directly points to `todo/docs/`

Format:
```markdown
## 即刻to do
- [ ] 打印证书 [[docs/打印证书]]

## 长期to do
- [ ] 换微服务 [[mini_todo/换微服务]]
```

Rules:
- Each todo is a checkbox item `- [ ]`
- Todo text: concise, user's original wording
- `[[]]` link appended after each todo, containing a short label
- Label matches the corresponding doc filename (without `.md`)
- When appending to existing file, match the existing section's formatting style

### Step 4: Generate Output Files

#### For immediate todos → `todo/docs/<label>.md`

Content format:
```markdown
# <Label>

<Explain the todo based on user input content>

## Details
<User's original relevant text, preserved verbatim>

## 学习检查
<!-- 执行此 todo 时，由 ai-era-learning skill 引导填充 -->
<!-- 以下为默认检查项，AI 应根据任务特征灵活调整，不必死守这四条 -->
- [ ] 模式归类：这个任务涉及什么设计模式/架构模式？
- [ ] 权衡对比：为什么选这个方案而不是其他？
- [ ] 判断标准：下次遇到类似情况，依据什么条件做决策？
- [ ] 自检：能描述给 AI 生成吗？能判断 AI 生成对错吗？能换场景复用吗？
```

#### For long-term todos → `todo/mini_todo/<long-term-name>.md`

One file per long-term todo, containing all mini-todos. Structure 由 AI 根据执行节奏引导的结果动态生成：

```markdown
# <Long-term Todo Name>

## 执行计划
<!-- 由 AI 根据学习者情况和 mini-todo 特征自主生成 -->
<!-- 粒度（天/周/阶段）、排列顺序、展开范围均由 AI 判断 -->

## Mini Todos
- [ ] <mini todo 1 action text> [[docs/<mini-label-1>]]
- [ ] <mini todo 2 action text> [[docs/<mini-label-2>]]
- [ ] <mini todo 3 action text> [[docs/<mini-label-3>]]
```

And corresponding `todo/docs/<mini-label-N>.md` files for each mini-todo.

Rules:
- Filename derived from the `[[]]` label
- One long-term todo = one file in `mini_todo/` (NOT one file per mini-todo)
- Explanation drawn from user's input text only
- Do NOT fabricate or add information not in user input
- If user input lacks detail, say so honestly rather than guessing
- Mini-todo count: no limit (unlike the 5-todo max for top-level todos)
- Mini-todos can be synthesized from the long-term todo — they don't need to come from user input verbatim

### Step 5: Sync & Archive

**触发方式：** `/text-to-todo sync`（无参数）

**执行步骤：**

1. 读取 `todo/TO_DO.md`，扫描所有 `- [x]` 项
2. 解析完成日期：
   - 从 `- [x]` 后面的 `✅ YYYY-MM-DD` 标记获取
   - 无标记则用当天日期（`YYYY-MM-DD`）
3. 按**完成月份**归档到 `todo/archive/YYYY-MM.md`
4. 归档记录保留原始分类标签，格式：

```markdown
# YYYY-MM 完成记录

## 即刻to do
- [x] metrics server ✅ 2026-04-22

## 长期to do
- [x] ChatOps - Slack/钉钉集成AI Bot ✅ 2026-04-25
```

5. 从 `todo/TO_DO.md` 移除已归档的 `- [x]` 行
6. 已完成的长期todo（有 `[[mini_todo/xxx]]` 链接的），将其 mini_todo 文件移到 `todo/archive/mini_todo/`
7. `todo/docs/` 文件**保留不移动**（知识沉淀）
8. 如果当月归档文件已存在，追加而非覆盖
9. 如果当月没有任何 `- [x]`，输出"没有待归档项"，不创建文件

**归档后目录结构：**
```
todo/
├── TO_DO.md                # 只留未完成的
├── archive/
│   ├── 2026-04.md          # 按月的完成记录
│   └── mini_todo/          # 已完成长期todo的mini-todo归档
├── docs/                   # 保留不动
└── mini_todo/              # 只留未完成的
```

**Rules：**
- sync 时需先 `mkdir -p todo/archive/mini_todo`
- 归档文件按月份命名，跨月不合并
- 如果某个月归档文件为空（所有项已移走），不删除文件
- 输出归档摘要：归档了N条（长期M条，即刻K条），目标文件路径

## Important Rules

- **NEVER** ask for confirmation before writing — fully automatic
- **NEVER** fabricate content — only use what user provided
- **NEVER** let top-level todo count overwhelm — merge related items when there are too many
- **ALWAYS** preserve user's original wording in todo items
- File paths are relative to working directory: `todo/TO_DO`, `todo/docs/`, `todo/mini_todo/`
- `[[]]` uses Obsidian-style internal links (no `.md` extension)
- Long-term todos: one `[[]]` link → `mini_todo/` (one file, multiple mini-todos inside)
- Immediate todos: `[[]]` link → `docs/` directly
