# money-os-core

**Money OS Shared Core v0.1** — 组合层基础设施。
**不包含任何项目业务逻辑。**

> ⚠️ **暂存状态：** 本目录当前位于 `project-m1-autopublishing/staging/money-os-core/`。
> Owner 建好 `fcubeve-alt/money-os-core`（private）后，本目录整体迁出成为仓库根。
> GitHub 集成无建库权限（`403 Resource not accessible by integration`），故未代建。

## 是什么

六个契约对象 + 一个只读聚合器 + 一个轻量 Supervisor。
项目在**本地**记录，Money OS **只读**聚合。

## 核心保证

| 保证 | 如何做到 |
|---|---|
| **Money OS 停机不影响业务** | 记录是纯本地写入，**业务代码路径上没有网络调用**（`tests/test_offline.py` 强制检查） |
| **传输可插拔** | 契约只定义记录与 outbox 语义。**Git 不是架构依赖**，只是可选传输之一 |
| **不要求重构** | 接入 = 一层薄适配。永久停在 L0 / L1 是合法终态 |
| **可随时退出** | 删除本地 `.moneyos/` 即完全脱离 |

## 结构

```
CONTRACT.md              权威契约文本
schemas/                 六个 JSON Schema
projects/registry.yaml   唯一权威项目列表
moneyos/
  contract.py            记录校验 + 本地 outbox 读写（零网络）
  transport.py           可插拔传输（Filesystem / Null；REST、队列等可后加）
  aggregate.py           跨项目只读聚合
  supervisor.py          组合状态 + 阻塞分析 + 下一步建议
  cli.py                 moneyos validate / status
tests/test_offline.py    离线保证测试
docs/COMPATIBILITY_MONETOOLS.md   第二业务兼容性分析
```

**零第三方依赖。** Python 3.11+ 标准库。

## 用法

```bash
python3 -m moneyos.cli validate <项目的 .moneyos 目录>
python3 -m moneyos.cli status --registry projects/registry.yaml
```

## 状态

**契约版本 `0.1` — `PROVISIONAL`，尚未 STABLE。**

| 验收 | 状态 |
|---|---|
| L1 契约冻结、六 schema 可校验 | ✅ |
| L2 **M1 真实数据**通过校验 | ✅ 8 work_items / 5 ledger / 2 approvals / 17 decisions |
| L3 Supervisor 产出有意义的阻塞分析 | ✅ |
| L4 **第二项目不改业务代码即可接入** | ⚠️ **分析完成，真实接入未做** |
| L5 Money OS 不可用时项目照常运作 | ✅ 由构造保证 + 测试强制 |

**L4 才是架构真正被验证的时刻。** 在此之前，"共享核心"只是一个只有一个客户的库。

## 不做（v0.1）

服务 / API / 数据库 / 消息队列 / Web UI / 认证 / 实时同步 /
Model Router / Opportunity Router / Economic Memory 聚合逻辑 /
**任何项目业务逻辑**（图像生成、文章写作、平台投稿、税务计算、珠宝库存）。

**判定标准：只对一个项目有意义的逻辑，不属于 Money OS。**
