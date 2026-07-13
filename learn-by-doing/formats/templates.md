# Templates（合并版）

> 所有文件格式模板的权威定义。各 workflow 文件引用此处，不重复定义。

---

## LEARNING_STATE.md

```markdown
# Learning State
Topic: {技术/工具/框架名称}
Current phase: 0-7
Current project: {一句话}
Current todo: {T001 - 任务名 / none}
Last completed todo: {Txxx - 任务名}
Known weak spots: {逗号分隔}
Next review due: {YYYY-MM-DD}
Last session summary: {1-3句}
Blocked by: {阻塞原因 / none}
```

---

## MISSION.md

```markdown
# Mission
## 目标
{一句话说清要做什么}
## 验收标准
- [ ] {可验证的标准}
## 范围
- 包含: {范围}
- 不包含: {边界}
```

---

## LEARNING_MAP.md

```markdown
# Learning Map: {主题}
## 核心模块
- {模块名}: {一句话} → 前置依赖: {无 / 其他模块}
## 模块关系
{依赖图或文字描述}
```

---

## TO_DO.md

```markdown
# To Do
## {阶段/模块}
- [ ] T001 {任务名} — 验收: {命令或检查方法} (预估: {分钟}min)
```

---

## RESOURCES.md

```markdown
# Resources
| 资源 | 类型 | 版本 | 质量 | 备注 |
|------|------|------|------|------|
| {URL/书名} | {官方文档/教程/书} | {版本} | {可信/有坑/过时} | {说明} |
```

---

## GLOSSARY.md

```markdown
# Glossary
| 术语 | 一句话定义 | 相关概念 |
|------|-----------|----------|
| {术语} | {定义} | [[相关wiki]] |
```

---

## NOTES.md

```markdown
# Notes
## 学习偏好
- {偏好}
## 随手记
- {笔记} (YYYY-MM-DD)
```

---

## learning-records/

```markdown
# {标题}
Date: YYYY-MM-DD
Evidence type: feynman | drill | review | debug
Status: active | weak-spot | resolved
Evidence: {具体证据}
Weak spots: {模糊点 / 无}
```

---

## REVIEW_QUEUE.md

见 `_shared/core-principles.md` §7。

---

## XMind 对比表

> 规则见 `SKILL.md` §教学原则 > 输出格式约定。
> 输出对比表时优先用此格式，不用 markdown 表格。

### 格式规则

- 第一行：标题（根节点）
- 每个选项用 tab 缩进
- 每个属性用双 tab 缩进
- 属性值写在冒号后

### 模板

```
{主题/标题}
	{选项1}
		{属性A}：{值}
		{属性B}：{值}
	{选项2}
		{属性A}：{值}
		{属性B}：{值}
```

### 示例

```
SSL 证书类型对比
	DV（域名验证）
		验证内容：域名归属
		签发速度：实时
		价格：免费（Let's Encrypt 等）
		适用场景：个人博客、小型网站
	OV（组织验证）
		验证内容：企业注册信息
		签发速度：几天
		价格：中等
		适用场景：企业官网
	EV（扩展验证）
		验证内容：严格企业审核
		签发速度：更久
		价格：最贵
		适用场景：金融、电商（浏览器地址栏显示公司名）
```

### 何时用表格 vs XMind

- 命令速查 / 简单键值对 → markdown 表格
- 分类对比 / 多属性比较 / 层级结构 → XMind tab 缩进
- 有嵌套子属性 → 必须用 XMind

---

## ai/wiki/{topic}/ 下的文件

### setup.md

```markdown
# {技术名} 搭建步骤
## 环境
- OS: {版本}
- 工具版本: {具体版本号}
## 步骤
### 1. {步骤名}
{命令 + 说明}
## 验证
{验证命令 + 预期输出}
```

### commands.md

```markdown
# {技术名} 常用命令
| 命令 | 作用 | 场景 |
|------|------|------|
| `{命令}` | {一句话说明} | {什么时候用} |
```

### troubleshooting.md

```markdown
# {技术名} 踩坑记录
## {问题简述}
- **现象**: {看到了什么}
- **根因**: {为什么会这样}
- **解决**: {怎么修的}
- **预防**: {下次怎么避免}
```
