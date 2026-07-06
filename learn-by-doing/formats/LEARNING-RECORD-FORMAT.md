# learning-record 格式

## 核心原则

**learning record 不是活动日志。** 它不是 session-by-session 的记录，也不是"覆盖过的材料"清单。

只在以下情况写：
1. **理解确认** — 用户能正确解释或应用一个非平凡概念
2. **先验知识** — 用户揭示出已有知识，改变了教学路径
3. **纠正误解** — 一个错误概念被纠正
4. **任务变更** — 项目目标或范围发生重大变化
5. **耐久薄弱点** — 排查失败暴露了系统性弱点

**不写 learning record 的情况：**
- 仅仅是"覆盖过的内容"
- todo 完成但没有概念性证据
- 通用会话摘要

## 模板

```markdown
---
id: 0001
status: active | weak-spot | superseded
evidence_type: feynman | exercise | debugging | prior-knowledge | mission-shift
related_module: M01
---

# {简短标题——概念名 / 关键洞察}

{1-3 句：学到了什么、纠正了什么、为什么改变下一步教学}

## Evidence

{具体证据：能解释给 AI 并答追问 / 独立完成练习 X / 在真实环境中排查出故障 Y}

## Implications

{对后续教学的影响：可以继续 / 需要补什么 / 薄弱点需复查}

## Next review

{YYYY-MM-DD}
```

## 状态说明

| 状态 | 含义 |
|------|------|
| active | 当前有效的理解，需要定期复习 |
| weak-spot | 之前以为懂了但后来发现薄弱，需要优先复习 |
| superseded | 被新的 learning record 替代 |

## 文件命名

`{序号}-{简短英文slug}.md`，如：
- `0001-docker-network-basics.md`
- `0002-corrected-mount-type.md`
