# Phase 3：拆任务 + 动手干

## 触发条件

Phase 2 完成。

## 流程

### 1. 拆任务为 TO_DO.md

按 `formats/TODO-FORMAT.md` 格式拆分：

- 每条 todo ≤ 30 分钟
- 每条必须有验收命令和预期结果
- 每条必须关联一个 ai/wiki/ 条目
- 标注依赖关系（prerequisites）
- 确保覆盖 MISSION.md 中的所有验收标准

### 2. 逐条执行

```
做一条 todo
  ↓ 用户动手（AI 提供 just-in-time 帮助）
  ↓ 做通了
  ↓ 运行验收命令 → 确认结果匹配预期
  ↓ 更新 ai/wiki/{topic}/xxx.md（关键命令、配置、验证方法、踩坑记录）
  ↓ 更新 LEARNING_MAP.md → 对应模块打 [x]
  ↓ 运行短费曼检验（见 Phase 4 简化版）
  ↓ 更新 LEARNING_STATE.md
  ↓ 更新 REVIEW_QUEUE.md（如适用）
  → 下一条
```

### 3. 卡住时

```
用户卡住
  ├── 先自己查 5 分钟（带着问题查文档/搜索）
  ├── 再来问 AI → 提供完整上下文：
  │   - 想做什么
  │   - 试了什么
  │   - 看到了什么错误
  │   - 在哪个模块/todo
  └── 解决了 → 把踩坑过程写进 troubleshooting.md + ai/wiki/
```

### 4. 完成一个模块后

运行完整费曼检验（Phase 4）→ 写入 learning-record

## 退出条件

- [ ] 所有 todo 已完成并验收
- [ ] MISSION.md 的所有验收标准满足
- [ ] ai/wiki/ 已更新对应条目
- [ ] 核心模块的费曼检验已通过
