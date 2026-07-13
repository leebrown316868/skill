---
name: deep-review
description: 复习已学内容——闭卷走链路、场景决策题、产出判断框架。Use when user says 复习, 吃透, 深挖, or wants to review learned material.
---

# deep-review

## 共享原则

> 四步法回答框架、自检4问、费曼检验协议、间隔复习队列 — 以上概念的**唯一权威定义**见 `_shared/core-principles.md`。
>
> **执行本技能前，先 Read `_shared/core-principles.md`。** 本文件仅记录 deep-review 的特化规则。

---

## 技能边界：何时用本技能 vs 其他技能

| 场景 | 用谁 | 交接条件 |
|------|------|----------|
| 自学全新技术领域 | learn-by-doing | 用户说"我想学 X" + 需要长期项目管理 |
| 引导式学习（含为什么/架构问题） | ai-era-learning | 用户问"为什么用X"/"这段代码什么意思" |
| 公司实训快速过关 | ops-training | 用户发"实训一 nginx"等大纲任务 |
| **复习已学内容** | **deep-review（本技能）** | 用户说"复习"/"吃透"/"深挖" |
| 复习发现知识缺口 | deep-review → learn-by-doing 或 ai-era-learning | 薄弱点需要重新系统学习时 |

---

## 核心理念

**学判断，不学语法。** AI 能秒出的不考，AI 不能替的往死里挖。

| AI 能做（跳过） | 你不能外包（深挖） |
|---|---|
| 参数含义、命令语法 | 场景选 PITR 还是 immediate？ |
| 完整配置步骤 | AI 给的配置哪里危险？ |
| 排查命令 | 先查哪一层、为什么？ |

---

## 路径约定

- **复习输入**：从 `ai/wiki/{技术名}/` 读取 setup.md / commands.md / troubleshooting.md
- **复习输出**：写到 `ai/wiki/{技术名}/场景判断.md`
- **复习队列**：`REVIEW_QUEUE.md`（项目根目录，格式见 `_shared/core-principles.md` §7）
- **如果没有 ai/wiki/ 笔记**：见下方 Step 0 fallback

---

## 执行流程

### Step 0：载入骨架

读取用户已有的笔记（`ai/wiki/{技术名}/` 下的 setup.md / commands.md / troubleshooting.md）。从笔记定位每一步，不另起炉灶。

**无笔记 fallback**：如果 `ai/wiki/{技术名}/` 不存在或为空：
1. 问用户："这个技术/项目你做过哪些事？从头到尾给我讲一下你记得的步骤。"
2. 根据用户口述，AI 生成初始笔记（setup.md + commands.md）存到 `ai/wiki/{技术名}/`
3. 用生成的笔记作为后续复习骨架

**Completion:** 笔记路径确认存在，模块结构列出。

### Step 1：Active Recall 链路过关

用户闭卷讲完整链路。AI 追问，不打断。每条追问只问：

- "这步在干什么？"
- "这个值为什么是这个？改成别的会怎样？"
- "这一步和下一步的关系是什么？"

**Hint gradient（逐级提示）：**

```
卡住
  → L1：提示方向（"看看笔记里 lag 那段"）
  → L2：缩小范围（"pg_stat_replication 有四个 lag 字段"）
  → L3：标记薄弱点，直接讲，讲完要求用户重新完整讲一遍
```

**概念首次出现必须拆解。** 用户问"XX 什么意思"时，用四步法（见 `_shared/core-principles.md` §2）。

**Completion:** 链路从头到尾讲通，无 L3 卡顿。

### Step 2：场景决策

AI 根据笔记内容出 3 道生产场景题。用户说方案和理由，不说命令。

```
答错 → 不给答案，提示看笔记 → 再答
答对 → 追问"如果条件变了呢？"
```

**Completion:** 3 题全部给出正确方案和判断理由。

### Step 3：产出判断框架

AI 整理暴露的薄弱点和场景决策，写到 `ai/wiki/{技术名}/场景判断.md`。

格式：场景 → 方案 → 为什么 → 常见错误。
不记命令、不记参数。

**Completion:** 文件写入，用户确认内容。

### Step 4：调度间隔复习

更新 `REVIEW_QUEUE.md`（格式和间隔规则见 `_shared/core-principles.md` §7）。

---

## 退出条件

复习结束前逐条确认自检清单（4 项，见 `_shared/core-principles.md` §4）。4 项全过 → 标记"熟练"。

---

## AI 硬约束

- 不自发解释参数含义（等用户问"这个词是什么意思"）
- 用 hint gradient，不直接给答案
- 不脱离用户笔记另起话题
- 每一步定位到笔记的具体位置
- 概念首次出现时用四步法拆解
