# ai/wiki/ 条目模板

## 原则

- 每条 Markdown 都可直接喂给 AI 做上下文
- 踩坑记录比官方文档更有价值
- 不必一次性写全，每完成一个模块补一条
- **用轻模板统一结构**，保证长期沉淀质量稳定

## 模板

```markdown
---
topic: {技术名称}
module: {M01 / M02 ...}
source_version: {v1.x}
last_verified: {YYYY-MM-DD}
confidence: high | medium | low
related_todos: {T001, T002}
related_learning_records: {0001, 0002}
---

# {标题}

## What this is for

{这个模块解决什么问题，在什么场景下使用}

## Minimal mental model

{最重要的 3-5 个概念，不需要面面俱到。目标是让人/AI 快速理解核心。}

## Commands / API / config

{关键命令、API 调用、配置文件示例}

```bash
# 示例命令
```

Expected result:

```text
...
```

## Verification

如何验证这个模块工作正常：

```bash
# 验证命令
```

Expected result:

```text
...
```

## Common failure modes

| Symptom | Likely cause | Check | Fix |
| ------- | ------------ | ----- | --- |

## Notes for future AI context

{下次加载时 AI 应该知道什么？}

## Sources

- {官方文档链接}
- {教程链接}
```

## 建议的文件结构

```
ai/wiki/{topic}/
├── setup.md                # 安装/环境搭建
├── core-concepts.md        # 核心概念
├── operation.md            # 常用操作
├── troubleshooting.md      # 排障记录（踩过的坑）
├── cheatsheet.md           # 速查表
├── reference.md            # 完整参考
└── ...                     # 按需增加
```
