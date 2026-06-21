---
name: learn-by-doing
description: 项目驱动学习工作流 — 整合 teach skill 的工作区结构（MISSION.md / RESOURCES.md / GLOSSARY.md / learning-records / NOTES.md）+ 7 阶段学习流程 + ai/wiki/ 知识库。学任何新技术时触发。加载后自动推进，无需等待指令。
---

# learn-by-doing：项目驱动学习

## 概述

这个 skill 薄薄一层，整合三样东西：

| 来源 | 用它的什么 |
|------|-----------|
| **teach skill** | 工作区结构：MISSION.md / RESOURCES.md / GLOSSARY.md / learning-records/ / NOTES.md |
| **学习新技术方法建议** | 7 阶段流程：骨架 → 项目 → 动手 → 费曼 → 排障 → 巩固 → 归档 |
| **ai/wiki/** | 代替 teach 的 HTML lessons，产出可喂 AI 的 Markdown |

**核心原则**：做中学，产出即沉淀。不是先学再做，而是做着学着，做完东西自然留下。

---

## 工作区结构

当这个 skill 在某个目录下加载时，它管理以下文件：

```
workspace/
├── MISSION.md                  # 项目目标（使用 teach 的 MISSION-FORMAT.md）
├── RESOURCES.md                # 高质量资源索引（使用 teach 的 RESOURCES-FORMAT.md）
├── GLOSSARY.md                 # 术语表（使用 teach 的 GLOSSARY-FORMAT.md）
├── NOTES.md                    # 学习偏好 / 随手记
├── learning-records/           # 学习记录（使用 teach 的 LEARNING-RECORD-FORMAT.md）
│   ├── 0001-xxx.md
│   └── ...
└── ai/wiki/{topic}/            # ← 代替 teach 的 lessons/ 和 reference/
    ├── setup.md                # 安装/环境搭建
    ├── core-concepts.md        # 核心概念
    ├── operation.md            # 常用操作
    ├── troubleshooting.md      # 排障记录（踩过的坑）
    ├── cheatsheet.md           # 速查表
    └── reference.md            # 完整参考
```

**ai/wiki/ 的规则**：
- 每条 Markdown 都可直接喂给 AI 做上下文
- 踩坑记录比官方文档更有价值
- 不必一次性写全，每完成一个模块补一条
- 格式自由，重点是**你写得清楚、AI 读得懂**

---

## 加载即启动：自动流程

加载后不要等用户提问，立即检查状态并推进。

### 状态检查

```
读取 MISSION.md → 是否存在？
  ├── 不存在 → 进入 Phase 0：初始化
  └── 存在 → 读取 learning-records/ 和 NOTES/
       ├── 所有 learning-records 标记 superseded 且 MISSION 标记完成？
       │     → 询问是否学完了，引导复盘
       └── 否则 → 从中断处继续

继续时判断：
  learning-records/ 为空且 MISSION 刚创建 → Phase 2-3
  learning-records 有记录但 ai/wiki/{topic} 条目不全 → Phase 3-4
  最近一条记录是"讲不清/卡壳了" → 先补薄弱点
  所有 wiki 条目都有且费曼已通过 → Phase 5-7
```

### Phase 0：初始化

问用户三个问题：
1. **学什么？**（哪个技术/工具/框架）
2. **为什么学？**（工作要用 / 想转方向 / 兴趣）
3. **当前基础？**（用过类似的吗 / 听说过多少）

→ 进入 Phase 1

### Phase 1：画骨架

**用户做**：去翻官方文档目录，用 XMind 画出知识骨架
**AI 做**：
- 初始化 `RESOURCES.md`：录入官方文档、高质量教程、社区链接
- 初始化 `GLOSSARY.md`：填入该技术的核心术语（空定义结构，后续填充）
- 用户画完 XMind 后，AI 帮忙补充遗漏的核心模块

**退出条件**：XMind 骨架确认无遗漏，核心模块已标记
→ 进入 Phase 2

### Phase 2：定项目

基于骨架设计一个**真实项目目标**，写成 `MISSION.md`。

```
格式（来自 teach 的 MISSION-FORMAT）：
- Why：一句话说清学这个能做什么
- Success looks like：3-5 条可验证的验收标准
- Constraints：时间、环境、前提条件
- Out of scope：这轮不碰什么
```

引导用户确认。

**退出条件**：项目目标明确 + 每条有可验证的验收标准
→ 进入 Phase 3

### Phase 3：拆任务 + 动手干

1. 把项目拆成 todo，输出 TO_DO.md
2. **逐条执行**：

```
做一条 todo
  ↓ 做通了
  ↓ 更新 ai/wiki/{topic}/xxx.md（把关键命令、配置、验证方法写进去）
  ↓ XMind 打勾 ✅
  → 下一条
```

3. **卡住时**：
   - 先自己查 5 分钟
   - 再问 AI（给完整上下文）
   - 解决了 → 把踩坑过程写进 troubleshooting.md

**产出**：每完成一个模块，ai/wiki/ 里多一条对应的 Markdown

**退出条件**：项目跑通，所有验收标准满足
→ 进入 Phase 4

### Phase 4：费曼检验

每个核心模块完成后，主动触发：

> "给我讲一遍这个模块，我装不懂追问。"

**讲清了** → 写入 learning-records：
```markdown
# {概念名} 理解通过

{1-3 句总结关键理解}

Evidence: 能解释给 AI 并答追问
Implications: 可以学下一个模块了
```

**卡壳了** → 写入 learning-records，标记待补：
```markdown
# {概念名} 理解模糊 → 需要补

{具体哪里说不清}

Status: 待补
```

**退出条件**：所有核心模块的费曼检验通过
→ 进入 Phase 5

### Phase 5：排障练习

基于学完的内容设计排障题：

1. AI 描述故障现象（不说根因）
2. 用户去真实环境排查
3. 用户汇报结论，AI 评判对错
4. 做错/做漏了 → 记入 learning-records 作为薄弱点
5. 排查过程写入 `ai/wiki/{topic}/troubleshooting.md`

**退出条件**：核心故障场景能独立排查
→ 进入 Phase 6

### Phase 6：定时巩固（跨会话）

告诉用户可以设置定时任务：

- **每天/每周** → AI 基于薄弱点出小题
- **间隔复习** → 旧知识回顾

巩固记录同步到 learning-records。

### Phase 7：复盘归档

项目完成后：

1. 更新 XMind：已掌握 ✅ / 未掌握（规划下个项目）
2. 产出 `ai/wiki/{topic}/cheatsheet.md`
3. 产出 `ai/wiki/{topic}/reference.md`
4. 更新 `MISSION.md`：标记完成
5. 规划下一个项目覆盖剩余模块

---

## 跨会话恢复

新对话中用户说"继续学习"时：

1. 读取 `MISSION.md` → 确认上下文
2. 读取 `learning-records/` → 了解掌握情况和卡壳点
3. 读取 `NOTES.md` → 了解偏好
4. 读取 `TO_DO.md` → 列出未完事项
5. 报出当前进度，问："从哪开始？"
6. 继续对应阶段

---

## 与 teach skill 的协作关系

| 组件 | 来源 | 本 skill 用法 |
|------|------|---------------|
| MISSION.md | teach MISSION-FORMAT.md | 原样使用格式 |
| RESOURCES.md | teach RESOURCES-FORMAT.md | 原样使用格式 |
| GLOSSARY.md | teach GLOSSARY-FORMAT.md | 原样使用格式 |
| NOTES.md | teach（概念） | 原样使用 |
| learning-records/ | teach LEARNING-RECORD-FORMAT.md | 原样使用格式 + 增加"待补"状态 |
| lessons/*.html | teach | **替换为** ai/wiki/ Markdown |
| reference/*.html | teach | **替换为** ai/wiki/ Markdown |
| 7 阶段流程 | 学习新技术方法建议 | 整合为自动推进流程 |

---

## 与 ops-learning 的关系

- `ops-learning` 是**运维技术专用**，含大量运维场景应对（Zabbix/K8s/Ansible）
- `learn-by-doing` 是**通用版本**，不绑定任何技术领域
- 如果你在学运维技术，两个 skill 可以叠加加载

---

## 禁止事项

- 不要让用户先看完所有视频/文档再动手
- 不要让用户背诵命令、参数、默认值
- 不要直接给故障答案（引导排查思路）
- 不要跳过一个阶段的退出条件
- 不要一次给太多信息（保持每条 todo 在 30 分钟内可完成）
