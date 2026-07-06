# Startup Protocol

每次加载技能时执行，**不等用户提问**。

---

## 1. 读取 LEARNING_STATE.md

```
LEARNING_STATE.md 是否存在？
├── 存在 → 读取，获取当前阶段、进度、薄弱点、阻塞项
│   ├── Blocked by 非空 → 先问用户阻塞是否已解决
│   └── 否则 → 进入 step 2
└── 不存在 → 检查工作区现有文件
    ├── 有 MISSION.md → 读 MISSION.md + learning-records/ 推断状态
    ├── 有 TO_DO.md 且有空 todo → 继续 Phase 3
    ├── 有 learning-records/ 但 ai/wiki/ 不全 → Phase 3-4
    ├── 空目录 → 进入 Phase 0
    └── 创建 LEARNING_STATE.md
```

## 2. Retrieval Warm-up（复习前置）

**如果有前序学习记录：**

1. 从 `REVIEW_QUEUE.md` 或 `learning-records/` 选一个到期或临近到期的条目
2. 如果 REVIEW_QUEUE 为空，从 learning-records 中选一个 active 或 weak-spot 记录
3. 提一个 recall 问题（不要先给答案）
4. 等用户回答后，给出纠正性反馈
5. 如果回答暴露了薄弱或误解，更新 learning-records 和 LEARNING_STATE.md
6. 记录到 REVIEW_QUEUE.md

**如果没有任何前序记录，跳过 warm-up。**

## 3. 状态报告

用 5 行以内报告当前状态：

```
当前阶段：Phase 3
当前任务：T003 - 配置数据库连接
已完成：2/8 个模块
上次卡在：Docker 网络配置（已解决）
建议下一步：继续 T003
```

## 4. 提议下一个动作

**只提一个建议。** 不要列选项清单。

- Phase 0: "你想学什么？"
- Phase 1: "我先帮你初始化 LEARNING_MAP.md 和 RESOURCES.md"
- Phase 2: "我们来定项目目标"
- Phase 3: "继续做 T003 还是先处理阻塞项？"
- Phase 4: "做完了 T003，来给我讲一遍这个模块？"
- Phase 5: "出个排障题练练？"
- Phase 6: "来做个复习，然后继续推进"
- Phase 7: "项目快完成了，复盘归档？"

## 5. 不要修改 MISSION.md

**没有用户确认，不要修改 MISSION.md 的内容。**
如果启动时发现 MISSION.md 需要更新，先问用户。
