# TO_DO.md 模板

## 原则

- 每条 todo 在 **30 分钟内可完成**
- 每条 todo 必须有 **可机器验证的验收方法**
- 完成一条后更新状态，不要批量标记

## 模板

```markdown
# TO_DO.md

## Current project

{项目名称}

## Tasks

### T001 - {任务名称}

Estimated time: 30 min
Module: {M01 / M02 ...}
Prerequisites: {T000}
User action: {用户需要做什么}
AI action: {AI 需要做什么}
Output files: {会创建/修改什么文件}
Verification command:
```bash
{能验证是否做对的命令}
```
Expected result:
```text
{命令预期输出}
```
Wiki update: {完成后要更新哪条 ai/wiki/ 条目}
Learning check: {完成后要做什么费曼检验}
Status: todo | doing | blocked | done
```

## 状态规则

| 状态 | 含义 | 下一步 |
|------|------|--------|
| todo | 待开始 | 确认前提条件后开始 |
| doing | 进行中 | 用户正在做 |
| blocked | 卡住了 | 记录阻塞原因，解决后再继续 |
| done | 已完成 | 已验收 + 已更新 wiki + 已做费曼检验 |

**不创建 todo 的规则：**
- 没有估计时间 → 先拆小
- 没有验收方法 → 先定义"怎样算对"
- 没有 wiki 条目要更新 → 说明这步不需要沉淀
