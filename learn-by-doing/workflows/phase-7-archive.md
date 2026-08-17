# Phase 7：复盘归档

## 触发条件

MISSION.md 的所有验收标准已满足，所有核心模块已完成。

## 流程

### 1. 产出最终文档

- 更新 `ai/wiki/{topic}/cheatsheet.md` — 把最常用的命令/配置/API 整理为速查表
- 更新 `ai/wiki/{topic}/reference.md` — 完整参考（可包含命令列表、配置选项、架构图）

### 2. 更新 MISSION.md

在底部追加完成状态：

```markdown
## Completion

Completed: {YYYY-MM-DD}
Verified by: {验收标准逐一打勾}
Status: ✅ Done | ⚠️ Partial | ❌ Failed
Lessons learned: {1-3 句核心体会}
```

**修改 MISSION.md 前确认用户。**

### 3. 更新 LEARNING_MAP.md

- 逐项更新能力维度的掌握等级（L0-L4）
- 打勾所有已掌握模块
- 标记未掌握模块（规划下个项目）
- 新增"Later projects"部分

### 3.5 产出能力迁移映射

按 `references/python-skeleton.md` 的 Haven 迁移表，标注哪些能力已达到 L3、可进入迁移任务，以及哪些已有新场景证据、可标记 L4。把这些能力作为下个项目（含 Haven）的起点；工程训练项目是手段，不永久维护已经完成使命的练习项目。

### 4. 规划后续

```markdown
## 下一阶段建议

{基于当前完成情况和未覆盖模块，建议下一个项目}
```

### 5. 归档 LEARNING_STATE.md

- phase: 7
- 标记 project completed
- 保留文件作为未来参考

### 6. 更新 REVIEW_QUEUE.md

加入月度复习计划，确保长期保持。

## 退出条件

- [ ] cheatsheet.md 和 reference.md 已产出
- [ ] MISSION.md 标记完成
- [ ] LEARNING_MAP.md 更新（已掌握 vs 待学）
- [ ] LEARNING_STATE.md 标记 phase 7
- [ ] 下个阶段建议已给出
