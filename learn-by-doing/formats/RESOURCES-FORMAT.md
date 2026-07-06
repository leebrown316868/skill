# RESOURCES.md 模板

## 原则

在教授任何版本敏感的技术内容前，先填充 RESOURCES.md。
**不信任参数知识** — 优先用官方来源验证。

## 模板

```markdown
# RESOURCES.md

## Official

| Title | URL | Applies to version | Why trusted | Last checked |
|-------|-----|-------------------|-------------|-------------|
| {官方文档} | {url} | {v1.x} | 官方维护 | {YYYY-MM-DD} |
| {安装指南} | {url} | {v1.x} | 官方来源 | {YYYY-MM-DD} |

## High-quality tutorials

| Title | URL | Level | Why useful | Caveats |
|-------|-----|-------|-----------|---------|
| {教程名} | {url} | beginner/intermediate/advanced | {为什么有价值} | {有什么限制或过时部分} |

## Community / wisdom

| Community | URL | Best for | Risk |
|-----------|-----|----------|------|
| {社区名} | {url} | {什么场景下查这个} | {信息可能过时 / 权威性不足等} |

## Deprecated / avoid

| Resource | Reason |
|----------|--------|
| {资源名} | {为什么不再推荐} |
```

## 使用规则

**创建 MISSION.md 和 TO_DO.md 前，必须完成 RESOURCES.md 的初步填充：**
- 至少 1 个官方文档来源
- 至少 1 个安装/环境搭建来源
- 至少 1 个排障/社区来源（如有）

**版本固定：** 如果技术是版本敏感的，在首次填充时锁定版本号。
**标记不确定性：** 如果某个资源未经亲自验证，注明 "unverified"。
