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

## Core Workflow

### Step 1: Parse User Input

Extract distinct actionable items from user text. Rules:
- Maximum 5 todos
- Each todo = smallest executable unit user can perform
- Preserve user's original wording — do NOT rewrite or reinterpret
- If input has more than 5 logical steps, merge related items

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

Structure:
```
todo/TO_DO.md (long-term section):
- [ ] 换微服务 [[mini_todo/换微服务]]

todo/mini_todo/换微服务.md:
# 换微服务
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
```

#### For long-term todos → `todo/mini_todo/<long-term-name>.md`

One file per long-term todo, containing all mini-todos:

Content format:
```markdown
# <Long-term Todo Name>

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
- **NEVER** exceed 5 todos at top level — merge if needed
- **ALWAYS** preserve user's original wording in todo items
- File paths are relative to working directory: `todo/TO_DO`, `todo/docs/`, `todo/mini_todo/`
- `[[]]` uses Obsidian-style internal links (no `.md` extension)
- Long-term todos: one `[[]]` link → `mini_todo/` (one file, multiple mini-todos inside)
- Immediate todos: `[[]]` link → `docs/` directly
