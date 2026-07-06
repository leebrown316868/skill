# LEARNING_MAP.md 模板

机器可读的主知识地图。AI 必须同步维护此文件。

## 原则

- **机器可读优先** — AI 能解析、能检查进度
- **XMind 是可选视图** — 用户可以用 XMind 画图，但 AI 必须维护 LEARNING_MAP.md
- **模块粒度** — 每个模块 30-60 分钟可完成
- **完成一个模块标记一个 [x]**

## 模板

```markdown
# Learning Map: {topic}

## Version

Target version: {v1.x / latest}
Environment: {OS / runtime version}

## Core modules

### M01 - {模块名称}
- [ ] Setup and environment
  - Why it matters: {为什么先学这个}
  - Project task: {项目中的对应任务}
  - Wiki page: `ai/wiki/{topic}/setup.md`
  - Evidence required: {能运行并输出什么}
- [ ] {子模块}
  - Project task: Txxx
  - Wiki page: `ai/wiki/{topic}/xxx.md`

### M02 - {模块名称}
- [ ] ...

### M03 - {模块名称}
- [ ] ...

### M04 - Debugging and failure modes
- [ ] Common failure scenarios
  - Project task: Txxx
  - Wiki page: `ai/wiki/{topic}/troubleshooting.md`

### M05 - Production patterns
- [ ] {生产级用法}
  - Project task: Txxx
  - Wiki page: `ai/wiki/{topic}/reference.md`

## Out of scope for this mission

{明确不学的模块，避免 scope creep}

## Later projects

{规划的下一个项目或后续模块}
```

## 使用规则

- Phase 1 必须创建 LEARNING_MAP.md
- 用户可以用 XMind 辅助思考，但 AI 必须确保 LEARNING_MAP.md 是权威版本
- 完成一个 todo 后，在对应模块打 [x]
- 如果学习过程中发现遗漏模块，补充进去并告知用户
