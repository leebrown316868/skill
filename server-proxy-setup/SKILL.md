---
name: server-proxy-setup
description: "国内服务器配置 mihomo(Clash Meta)代理，解决 GitHub/PyPI 等外网访问问题。当用户说'服务器没梯子'、'GitHub 连不上'、'装代理'、'配 clash/mihomo'、'hermes update 连不上 GitHub'时触发。面向运维新手，所有命令直接可执行。"

---

# 国内服务器 mihomo 代理配置

## 适用场景

- 国内 Ubuntu/CentOS 服务器需要访问 GitHub、PyPI 等外网
- hermes update / git clone / pip install 因网络问题失败
- 有机场订阅但不知道怎么在服务器上用

## 前置条件

- 一个有效的机场订阅链接（在本地电脑能正常用）
- 服务器能 SSH 登录
- 服务器架构为 x86_64（arm64 需换对应二进制）

## 完整流程

### 1. 安装 mihomo

```bash
# 方式A：在有梯子的本机下载后 scp 传到服务器（推荐）
# 下载地址：https://github.com/MetaCubeX/mihomo/releases
# 选 mihomo-linux-amd64-版本号.gz
scp mihomo-linux-amd64-*.gz user@server:~/mihomo.gz

# 方式B：用 GitHub 镜像加速（不需要梯子）
curl -L -o ~/mihomo.gz "https://ghfast.top/https://github.com/MetaCubeX/mihomo/releases/latest/download/mihomo-linux-amd64-v1.19.10.gz"

# 解压安装
gunzip ~/mihomo.gz
chmod +x ~/mihomo
mkdir -p ~/.local/bin
mv ~/mihomo ~/.local/bin/mihomo

# 验证
~/.local/bin/mihomo -v
```

### 2. 拉取机场订阅配置

**关键坑：必须用 `clash-verge-rev` 作为 User-Agent，其他 UA（如 ClashforWindows、clash）可能返回空节点。**

```bash
mkdir -p ~/.config/mihomo

# 替换下面的 URL 为你的机场订阅链接
curl --noproxy '*' -L -A 'clash-verge-rev' -o ~/.config/mihomo/config.yaml "你的订阅链接"

# 验证有节点（应该看到 server: 行，不是 nameserver）
grep 'server:' ~/.config/mihomo/config.yaml | head -3
```

如果 `grep` 只返回 DNS nameserver 而没有代理节点 server，说明 UA 不对。依次尝试：`ClashforWindows`、`clash`、`v2rayN`、`FlClash`。

如果返回 403，同上换 UA。

### 3. 修复配置（如果启动报错）

如果 mihomo 启动报 `'自动选择' not found` 之类的错误：

```bash
# 检查代理组引用了不存在的节点
grep 'proxies:' ~/.config/mihomo/config.yaml

# 临时修复：把引用改成 DIRECT
sed -i 's/proxies: \[自动选择\]/proxies: [DIRECT]/' ~/.config/mihomo/config.yaml
```

### 4. 手动下载 geodata 文件

mihomo 启动时需要 GeoIP.dat 和 GeoSite.dat，国内下载可能超时。

```bash
# 手动下载（加长超时）
wget --timeout=120 -O ~/.config/mihomo/GeoIP.dat "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat"
wget --timeout=120 -O ~/.config/mihomo/GeoSite.dat "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat"
```

如果 jsdelivr 也超时，在本地电脑下载后用 scp 传上去：

```bash
# 本地电脑执行
scp GeoIP.dat GeoSite.dat user@server:~/.config/mihomo/
```

### 5. 启动 mihomo

```bash
# 用绝对路径启动（nohup 时 PATH 可能不包含 ~/.local/bin）
nohup ~/.local/bin/mihomo -d ~/.config/mihomo > /tmp/mihomo.log 2>&1 &

# 等 5 秒后验证
sleep 5
tail -5 /tmp/mihomo.log
ss -tlnp | grep 7890
```

应该看到 `Mixed(http+socks) proxy listening at: [::]:7890`。

### 6. 创建快捷命令

创建 `~/bin/` 目录下的管理脚本，实现一键启动/停止/状态查看：

```bash
mkdir -p ~/bin

# proxy-start
cat > ~/bin/proxy-start << 'SCRIPT'
#!/bin/bash
nohup ~/.local/bin/mihomo -d ~/.config/mihomo > /tmp/mihomo.log 2>&1 &
sleep 2
ss -tlnp | grep 7890 && echo 'mihomo started' || echo 'mihomo failed to start'
SCRIPT
chmod +x ~/bin/proxy-start

# proxy-stop
cat > ~/bin/proxy-stop << 'SCRIPT'
#!/bin/bash
if pkill mihomo; then echo 'mihomo stopped'; else echo 'mihomo not running'; fi
SCRIPT
chmod +x ~/bin/proxy-stop

# proxy-status
cat > ~/bin/proxy-status << 'SCRIPT'
#!/bin/bash
if pgrep mihomo > /dev/null; then
  ps aux | grep mihomo | grep -v grep
  ss -tlnp | grep 7890
else
  echo 'mihomo not running'
fi
SCRIPT
chmod +x ~/bin/proxy-status
```

### 7. 设置环境变量（PATH + 代理）

```bash
# 写入 ~/.bashrc
cat >> ~/.bashrc << 'EOF'

# PATH for local bin and scripts
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"

# mihomo proxy
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
EOF

# 当前终端立即生效
source ~/.bashrc
```

**验证**：

```bash
which proxy-start   # 应输出 /home/你的用户名/bin/proxy-start
which hermes        # 如果装了 hermes 也应能找到
```

### 8. 验证连通性

```bash
curl -s -o /dev/null -w '%{http_code}' -x http://127.0.0.1:7890 https://github.com
# 返回 200 就成功了
```

### 9. 清理干扰配置

代理通了之后，检查并清理以下干扰项：

```bash
# 检查全局 git 是否有 insteadOf 劫持（把 github.com 重定向到 ghproxy）
git config --global --list 2>/dev/null | grep insteadOf
# 如果有，删掉：
git config --global --unset url.https://ghproxy.com/https://github.com/.insteadOf

# 检查 pip 镜像源，如果有国内镜像导致缺包，改成官方源
cat ~/.pip/pip.conf 2>/dev/null
# 如果指向国内镜像，备份并改：
# mv ~/.pip/pip.conf ~/.pip/pip.conf.bak
# echo -e '[global]\nindex-url = https://pypi.org/simple' > ~/.pip/pip.conf
```

## 开机自启（可选）

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/mihomo.service << 'EOF'
[Unit]
Description=Mihomo Proxy

[Service]
ExecStart=%h/.local/bin/mihomo -d %h/.config/mihomo
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now mihomo
loginctl enable-linger $USER
```

## 常见问题速查

| 现象                                                   | 原因                         | 解决                                                         |
| ------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ |
| 订阅返回 403                                           | UA 不对                      | 换 `-A 'clash-verge-rev'`                                    |
| 订阅 proxies: [] 空（只有 DNS nameserver）             | UA 不匹配客户端              | 同上，依次试 clash-verge-rev → ClashforWindows → FlClash     |
| `curl: Failed to connect to 127.0.0.1:7890`            | 系统有代理变量但 mihomo 没跑 | `unset http_proxy https_proxy` 或加 `--noproxy '*'`          |
| `'自动选择' not found`                                 | 配置引用了不存在的代理组     | `sed` 改成 DIRECT                                            |
| `can't download GeoIP.dat: context deadline exceeded`  | geodata 下载超时             | 手动 wget 或 scp 传文件                                      |
| `hermes update` 仍走 ghproxy                           | 全局 git insteadOf 规则      | `git config --global --unset` 删掉                           |
| pip install 找不到 setuptools                          | 国内镜像缺新版包             | 改 pip.conf 为 pypi.org                                      |
| nohup 报 `command not found`                           | PATH 不含 ~/.local/bin       | 用绝对路径 `~/.local/bin/mihomo`                             |
| `proxy-start` 输入后出现 `>` 提示符卡住                | 旧 alias 残留（引号嵌套）    | `unalias proxy-start proxy-stop proxy-status` 然后 `source ~/.bashrc` |
| 从 Windows SSH 写 .bashrc 时 `$HOME` 变成 Windows 路径 | PowerShell 本地展开变量      | 用反引号 `` `$HOME `` 或写脚本文件管道到 SSH                 |

