# ops-triage：按层命令速查

> **说明：** 这个文件是参考手册，不是执行清单。
> AI 会根据 Phase 0 定下的目标，从这个池子里选出具体命令。
> 不需要全跑，只跑跟当前目标相关的。

---

## 第1层：谁在这台机器上？（进程/服务）

```bash
# 容器服务
docker ps                        # 所有运行中的容器
docker ps -a                     # 所有容器（含已停止）
docker stats --no-stream         # 容器资源占用（CPU/内存）

# 系统服务
systemctl list-units --type=service --state=running  # 运行中的系统服务

# 所有进程（按内存排序）
ps aux --sort=-%mem | head -30

# 谁在占端口
ss -tnlp                         # 所有监听端口 + 进程
```

## 第2层：谁跟谁说话？（网络）

```bash
# 连接关系
ss -tnp                          # 所有 TCP 连接 + 进程（含外部）

# 防火墙
iptables -L -n                   # 防火墙规则
firewall-cmd --list-all          # firewalld 规则（如果有）

# 容器网络
docker network ls                # 所有 Docker 网络
docker network inspect <name>    # 某个网络的详情（子网、连了哪些容器）

# DNS / 路由
cat /etc/resolv.conf             # DNS 配置
ip route                         # 路由表
```

## 第3层：数据存哪？（存储）

```bash
# 磁盘
df -h                            # 磁盘分区使用率
lsblk                            # 块设备结构
mount | grep /data               # 挂载点

# 目录结构
ls -la /data/                    # 先看一级目录
du -sh /data/*/                  # 各目录占用（别跑全盘 du）

# 容器数据挂载
docker inspect <容器> | grep -A 10 Mounts  # 容器的 bind mount
```

## 第4层：数据怎么保命？（备份/高可用）

```bash
# 定时任务
crontab -l                       # 本机定时任务
ls /etc/cron*                    # 系统级定时任务

# 远程连接痕迹
ls -la /root/.ssh/               # SSH key
cat /root/.ssh/known_hosts       # 连过哪些机器

# 备份脚本
find / -name "*backup*" -o -name "*rsync*" -o -name "*wal*" 2>/dev/null

# 数据库特定
# PG:
docker exec pg-uc psql -U postgres -c "SELECT pg_is_in_recovery();"
docker exec pg-uc psql -U postgres -c "\l"
docker exec pg-uc psql -U postgres -c "\du"

# MySQL:
docker exec mysql mysql -e "SHOW SLAVE STATUS\G"
docker exec mysql mysql -e "SHOW DATABASES;"

# MongoDB:
docker exec mongo mongosh --eval "rs.status()"
docker exec mongo mongosh --eval "show dbs"
```

## 第5层：日志和监控

```bash
# 系统日志
journalctl -xe -n 50             # 最近的系统日志
dmesg | tail -30                 # 内核日志

# Docker 日志
docker logs --tail 50 <容器>     # 某个容器的日志尾巴

# 监控组件
docker ps | grep exporter        # 有哪些 exporter 在跑
curl -s localhost:9100/metrics | head -20  # node exporter 是否响应

# 应用日志位置（常见）
ls /data/share/logs/             # 共享日志目录（视项目而定）
```

## 注意事项

- **不要全跑** — 根据 Phase 0 的目标选相关的层
- **不要跨层跳** — 第1层没查完就急着查第4层，容易漏关键信息
- **异常要停** — 如果某条命令报错/返回空/权限拒绝，停下来问 AI "这正常吗？"
