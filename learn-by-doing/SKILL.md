---
name: learn-by-doing
description: Use when the user explicitly wants to learn a technical skill through a hands-on project over multiple sessions, continue an existing learning workspace, create/update MISSION.md/TO_DO.md/LEARNING_MAP.md/learning-records/ai/wiki, or run Feynman checks/troubleshooting drills/spaced review. Do NOT trigger for one-off explanations, ordinary Q&A, unrelated debugging, or quick documentation lookup.
---

# learn-by-doing：项目驱动学习

## Purpose

管理多会话、项目驱动的学习工作区。**做中学，产出即沉淀** — 不是先学再做，而是做着学着，做完东西自然留下。

---

## Trigger 边界

**触发时：**
- 用户明确说"学习 X"、"继续学习"、"做个项目学 X"、"更新学习工作区"
- 用户在已有学习工作区中，需要推进 todo、写 learning record、更新 wiki
- 用户说"考考我"、"出个排障题"、"复习一下"

**不触发：**
- 用户问"解释一下 X 的概念"（一次性解释 → 不需要完整工作区）
- 用户在无关项目时顺带用了某个技术
- 普通 debug 或文档查询

---

## 工作区文件

| 文件 | 用途 | 必需 |
|------|------|------|
| `LEARNING_STATE.md` | 单一状态源：当前阶段、进度、薄弱点 | 运行时自动维护 |
| `MISSION.md` | 项目目标、验收标准、范围 | 是 |
| `LEARNING_MAP.md` | 模块化知识骨架，机器可读的主地图 | 是 |
| `TO_DO.md` | 任务列表，每条带验收命令 | 是 |
| `RESOURCES.md` | 可信资源索引，含版本和质量字段 | 是 |
| `GLOSSARY.md` | 术语表 | 推荐 |
| `NOTES.md` | 学习偏好 / 随手记 | 可选 |
| `REVIEW_QUEUE.md` | 间隔复习队列 | 推荐 |
| `learning-records/` | 学习记录（不是活动日志） | 是 |
| `ai/wiki/{topic}/` | 可喂 AI 的 Markdown 知识条目 | 是 |

---

## Operating Rules

1. **每条 todo ≤ 30 分钟** — 超时自动切分
2. **每条 todo 必须有验收方法** — 可验证才算完成
3. **learning record 不是活动日志** — 只在有证据时写
4. **资源优先用官方/最新版** — 标记不确定或过时的来源
5. **不直接给故障根因** — 引导排查，先让用户尝试
6. **不覆盖用户文件** — 修改前确认
7. **启动时做 retrieval warm-up** — 先回顾再教新内容
8. **每次修改文件后通读全文** — 检查矛盾/过时内容

---

## 流程参考

```
Phase 0: 初始化 → 问三个问题
Phase 1: 知识地图 → LEARNING_MAP.md（XMind 可选）
Phase 2: 定项目 → MISSION.md
Phase 3: 拆任务动手 → TO_DO.md → 逐条执行 → 更新 ai/wiki/
Phase 4: 费曼检验 → learning-records（有证据才写）
Phase 5: 排障练习 → 分层 drill（L1/L2/L3）
Phase 6: 间隔复习 → REVIEW_QUEUE.md → 每次启动检索
Phase 7: 复盘归档 → cheatsheet + 下个项目规划
```

每个阶段的详细协议见 `workflows/` 目录。

---

## 文件格式

所有文件模板见 `formats/` 目录。

---

## 安全约束

排障练习中的命令安全规则见 `safety/real-environment-commands.md`。

---

## 跨会话恢复

见 `workflows/startup.md`。
