# Phase 1：绘制知识地图

## 触发条件

Phase 0 完成。

## 流程

### AI 初始化 RESOURCES.md

按 `formats/templates.md` 中 RESOURCES.md 格式填充：
- 至少 1 个官方文档来源
- 至少 1 个安装/环境搭建来源
- 至少 1 个排障/社区来源
- 固定版本号（如适用）

### AI 初始化 LEARNING_MAP.md

按 `formats/templates.md` 中 LEARNING_MAP.md 格式创建骨架：
- 参考官方文档目录结构和 RESOURCES.md
- 按模块划分，每个模块 ≤ 60 分钟
- 标注哪些 in scope、哪些 out of scope

### AI 初始化 GLOSSARY.md

填入核心术语及其空结构（后续逐步填充定义）。

### 用户可选：用 XMind 画图

- 用户可以在 XMind 里画知识骨架帮助思考
- **但 LEARNING_MAP.md 是机器可读的权威版本**
- AI 根据用户 XMind 同步更新 LEARNING_MAP.md（如有遗漏模块则补充）

### 检查完整性

与用户确认：
- 核心模块是否有遗漏
- 模块划分是否合理
- Out of scope 是否正确

## 退出条件

- [ ] RESOURCES.md 已初始化（含版本信息）
- [ ] LEARNING_MAP.md 已创建，模块清单确认无遗漏
- [ ] GLOSSARY.md 已初始化
- [ ] 用户确认地图完整
