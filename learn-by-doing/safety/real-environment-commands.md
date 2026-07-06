# Real Environment Command Safety

用于 Phase 5 排障练习中的命令安全约束。

---

## 硬规则

**永远不要建议用户在真实环境运行以下命令，除非所有安全条件都满足：**

- `rm -rf` / `rm -r` / `del /f /s`
- `DROP TABLE` / `DROP DATABASE`
- `diskpart` / `fdisk` / `mkfs`
- `chmod 777` / 批量权限修改
- 任何形式的 `> /dev/sda` 或直接磁盘写入
- 生产环境的 `kubectl delete`（非测试 namespace）
- 生产环境的 `systemctl restart` 关键服务
- `kill -9` 非用户进程

---

## 安全条件的三个检查

只能在以下三条全部满足时执行有风险操作：

1. **用户明确确认环境安全**
   - "这是测试环境" 或 "我做了快照/备份"
   - 不是：用户没说话，AI 默认安全

2. **存在可验证的回滚路径**
   - 有备份可恢复
   - 有版本管理（git commit / config backup）
   - 有 undo 命令

3. **命令和影响已提前解释**
   - AI 在用户执行前说明："这条命令会 XXX，影响是 YYY"
   - 用户确认后再执行

---

## Drill 中的命令限制

| Level | 允许的命令 | 禁止 |
|-------|-----------|------|
| L1 模拟 | 无需真实命令 | — |
| L2 引导 | 只读命令：`cat` / `tail` / `grep` / `curl` / `describe` / `get` / `list` / `status` / `--help` | 任何写入操作 |
| L3 独立 | 不限（但受上面三条约束） | 同上 |

---

## 违规处理

如果在排障 drill 中发现 AI 无意中建议了不安全命令，立即：
1. 撤回建议
2. 向用户道歉
3. 记录到 LEARNING_STATE.md 作为 AI 行为改进点
