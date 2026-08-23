# Money OS Shared Core v0.1 — 架构

---

## 1. 由约束反推架构

你给了一条硬约束，它单独决定了整个架构：

> **Tax 与 Pearl Bridal Jewelry 必须保持独立可运行；Money OS 停机不得阻碍其核心业务。**

**任何「Money OS 是一个服务，项目调用它」的设计都无法满足这条。** 服务一停，
调用方要么阻塞、要么必须实现降级路径——降级路径本身就是第二套实现，且几乎不会被测试。

**因此 v0.1 没有运行时。**

## 2. 核心决定：v0.1 是 schema + 库 + CLI，不是服务

```
每个项目在自己的仓库里，追加写入本地 .moneyos/ 目录
        │  （纯本地文件写入，无网络，无依赖）
        ▼
   git（既有的传输层，无需新建）
        │
        ▼
Money OS Supervisor —— 只读聚合，产出组合视图与建议
```

| 属性 | 结果 |
|---|---|
| Money OS 停机 | **不存在停机概念**——没有常驻进程 |
| 项目对 Money OS 的运行时依赖 | **零** |
| 项目不装 Money OS 库能否合规 | **能**——契约是文件格式，手写 CSV/NDJSON 亦可 |
| 传输 | git（三个项目已经在用） |
| 一致性模型 | **追加写入 + 后写为准**，无分布式事务 |

**这不是权宜之计。** 在三个项目共 $0 收入、无并发、无实时需求的阶段，
引入服务、数据库或消息队列，是为不存在的规模付出确定的复杂度成本。
**v0.2 若真需要服务，从只读聚合器升级即可，契约不变。**

## 3. 八大组件

### 3.1 Project Registry
Money OS 侧唯一的**权威列表**：`projects/registry.yaml`。
记录 `project_id` · 名称 · 仓库地址 · 契约版本 · 集成级别 · 状态。
**项目不需要知道注册表存在。**

### 3.2 Project Contract
见 `03_PROJECT_CONTRACT_v0.1.md`。六个对象、三个集成级别。

### 3.3 Work / Task Status
从 M1 已在跑的状态机抽象。**核心洞察：M1 的状态值几乎全是"卡在什么上"**，
而不是"进行到哪一步"——`BLOCKED_BY_AUTHOR_ELIGIBILITY`、`POLICY_VERIFIED_ACCOUNT_GATE`。
v0.1 的 WorkItem 因此**把阻塞原因作为一等公民**，而不是塞进 notes。

### 3.4 Approval Gate
**只治理 Money OS 管辖的动作**（资本配置、跨项目决策、不可逆外部动作），
**不治理业务交易**。Pearl Bridal 接一个订单不需要 Money OS 批准——
这是边界，也是"停机不阻碍业务"能成立的原因。

### 3.5 Financial Ledger
直接沿用 M1 已验证的收入/成本字段，向上抽象为 `LedgerEntry`。
**保留 `human_minutes`**——这是 M1 实践中最有价值的字段之一，
因为它让"自动化是否经济上值得"可计算。

### 3.6 Decision / Economic Memory
`Decision` 复用 M1 的 `DECISION_LOG` 语义（含被否方案与理由）。
**Economic Memory v0.1 只定 schema，不实现聚合**——零销售数据时它是空壳。

### 3.7 Events / Metrics / Status
单一追加流 `events.ndjson`。**不是消息队列**，是审计日志。
Supervisor 读它产出指标；没有订阅者、没有投递保证。

### 3.8 Supervisor（轻量）
一条 CLI：读所有已注册项目 → 产出组合状态 + 阻塞清单 + 下一步建议。
**它不执行任何东西**，不调度、不派活。**建议是给人看的。**

## 4. 三个集成级别 —— 让 Tax / Pearl 可选接入

| 级别 | 项目需要做什么 | 得到什么 |
|---|---|---|
| **L0 — Observed** | **什么都不做。** Money OS 侧手工登记一行 | 出现在组合视图里 |
| **L1 — Reporting** | 在自己仓库写 `.moneyos/ledger.ndjson` 与 `events.ndjson`（可手写、可 CSV 导出） | 财务汇总、指标、Supervisor 建议 |
| **L2 — Governed** | 额外写 `approvals.ndjson` 与 `work_items.ndjson` | 完整治理：审批追踪、阻塞分析、经济记忆 |

**Tax 与 Pearl Bridal 可以永远停在 L0 或 L1。** 升级是它们的选择，不是 Money OS 的要求。
**M1 直接上 L2**——它是验证架构的第一个客户，必须走完整路径。

## 5. Adapter 边界

```
项目核心业务系统  ←── 绝不修改
        │
        │  项目自己写的一层薄适配（几十行，非框架）
        ▼
   .moneyos/*.ndjson    ←── 契约面在这里
        │
        ▼
   Money OS（只读）
```

**Adapter 属于项目，不属于 Money OS。** Money OS 永远不进项目的业务代码。
一个项目要退出，删掉 `.moneyos/` 目录即可，业务系统零改动。

## 6. Money OS 里绝不能出现的东西

图像生成 · 文章写作 · Adobe Stock 投稿 · 任何平台 Adapter · 任何 marketplace 工作流 ·
珠宝库存 · 税务计算 · 任何客户业务规则。

**判定标准：若一段逻辑只对一个项目有意义，它不属于 Money OS。**
第二个项目提出同样需求之前，共享是投机。
