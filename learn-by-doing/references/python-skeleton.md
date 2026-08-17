# Python 学习骨架与项目路线

> 供 learn-by-doing 使用。Phase 1 绘制能力地图时，Python 主题直接采用本文件的十项能力树；Phase 7 归档时对照 Haven 迁移表。

## 一、第一阶段能力树（十项）

学习按"解决工程问题所需能力"组织，不照抄教材目录。教材目录只作参考索引。

```text
Python工程能力
├── 数据与控制
├── 函数与模块
├── 文件与配置
├── HTTP与API
├── 错误与调试
├── 数据模型与状态
├── 测试
├── 数据库
├── Web开发
└── 部署与工程化
```

### 每项能力的范围

**数据与控制**
- 字符串、数字、布尔值、None；list、dict、tuple、set
- if、for、while；enumerate、zip；基础条件判断

**函数与模块**
- 函数定义、参数与返回值、默认参数、关键字参数
- 作用域、类型标注、import、main 入口

**文件与配置**
- pathlib、文本、JSON、CSV
- 环境变量、配置校验

**HTTP与API**
- GET、POST、Header、JSON、状态码
- timeout、connection error、Bearer Token

**错误与调试**
- Traceback、try/except/finally、raise、logging
- 输入校验、超时/重试/降级

**数据模型与状态**
- dataclass、Pydantic、类和实例、时间、序列化

**测试**
- pytest、assert、fixture、参数化、mock

**工程化**
- 虚拟环境、依赖管理、项目目录、Git、Docker、配置隔离、README

### 暂缓进阶索引（第一阶段不学，放进阶）

- 仅位置参数、仅关键字参数
- 复杂 `*args` 和 `**kwargs`
- Lambda、闭包、装饰器底层
- 元类、复杂继承
- `match` 高级模式
- Python 内部实现细节

## 二、连续项目路线

不做五个互不相关的浅项目，维护一个逐步演进的项目：

```text
Service Checker CLI
        ↓
Service Check API
        ↓
定时检查和告警
        ↓
Runbook知识库
        ↓
AI故障摘要
        ↓
受控运维Agent
```

### 第一阶段只做 Service Checker CLI

```text
读取配置 → 请求URL → 记录状态码与耗时 → 分类超时/连接失败/HTTP错误 → 输出汇总 → 编写测试
```

完成后改变一项真实约束，借助 AI 再次交付核心版本；学习者重新确认需求、审查关键决策并提供独立证据（L3 交付验证，跨场景后可作为 L4 迁移证据）。

### 进入 FastAPI 的门槛条件（全部满足才推进）

- [ ] 能借助 AI 读取配置并验证解析结果
- [ ] 能判断函数边界是否合理
- [ ] 能处理异常并验证失败路径
- [ ] 能借助 AI 阅读 Traceback，组织并验证根因假设
- [ ] 能设计和运行基本测试
- [ ] 能解释主要数据流、关键决策和验收证据
- [ ] 允许 AI 整文件生成，但能审查关键改动，且不只依赖 AI 同时生成的测试

## 三、能力 → Haven 迁移表

工程训练项目不是终身目标，作用是培养可迁移能力。能力达到 L3 后进入长期虚拟世界项目 Haven 做迁移任务；在新约束下再次可靠交付后标记 L4：

| 工程训练能力 | Haven 用途 |
|--------------|-----------|
| FastAPI | AI 角色和世界状态后端 |
| PostgreSQL | 用户、世界、记忆 |
| HTTP API | 游戏客户端与后端通信 |
| LLM API | AI 角色 |
| RAG | 世界观和角色知识 |
| Docker | 部署后端 |
| 日志和测试 | 保证世界状态稳定 |

## 四、标准学习循环的迁移示例

同一知识换三个场景应用，能迁移才说明进入长期能力：

```text
读取 servers.json → 读取 runbooks.json → 读取 Haven 世界配置
```
