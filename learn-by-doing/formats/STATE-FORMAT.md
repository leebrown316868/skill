# LEARNING_STATE.md 模板

单一状态源。由 AI 在每次操作后自动维护，不依赖人工更新。

```markdown
# Learning State

Topic: {技术/工具/框架名称}
Current phase: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
Current project: {当前项目一句话}
Current todo: {T001 - 任务名 / none}
Last completed todo: {Txxx - 任务名}
Known weak spots: {逗号分隔的薄弱概念}
Next review due: {YYYY-MM-DD}
Last session summary: {1-3 句上次会话做了什么、卡在哪}
Blocked by: {阻塞原因 / none}
```

## 维护规则

- **每次操作后更新**：完成 todo、写 learning record、切换阶段时
- **不要等用户要求**：AI 自动维护
- **保持简洁**：Last session summary 不超过 3 句
- **Blocked by 非空时**：启动时优先处理阻塞项
