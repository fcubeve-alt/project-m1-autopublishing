# Money OS Project Contract v0.1

**权威文本。** `schemas/*.json` 是其机器可读形式；冲突以本文为准。
**契约版本:** `0.1` · **稳定性承诺:** §8

---

## 0. 一句话定义

> **一个项目通过在本地记录六类结构化记录来遵守本契约。
> 传输方式不属于契约。**

不要求语言、框架、数据库、在线状态、网络可达性，**也不要求使用 Git**。

## 1. 架构：Local-First + Outbox（v0.1 核心修正）

```
项目业务系统
     │  ① 同步、本地、绝不失败
     ▼
本地 Money OS Adapter / Outbox
     │  ② 异步、非阻塞、可重试
     ▼
Transport（可用时才发生）
     │
     ▼
  Money OS
```

**三条不可协商的性质：**

| 性质 | 含义 |
|---|---|
| **① 是同步的，但只写本地** | 记录一条 Money OS 记录 = 一次本地写入。不发网络请求，不等响应 |
| **② 是异步的，且允许永久失败** | 传输失败不回传给业务系统。业务不知道也不关心同步是否成功 |
| **Money OS 不可用时** | 项目照常运行 · 记录留在 outbox · 恢复后继续同步 · **业务执行不失败** |

**业务代码路径上不得出现任何 Money OS 的网络调用。** 这是可被审查的硬性要求。

## 2. Transport 是可插拔的，不是契约的一部分

契约只规定**记录长什么样**与**outbox 的语义**。传输可以是：

filesystem · Git · REST · 消息队列/事件总线 · 数据库同步 · CLI · 手工上传 · 其他

**v0.1 参考实现用本地 NDJSON 文件 + 文件系统读取**，因为它最容易调试、
零依赖、且天然满足"Money OS 不可用不影响业务"。

> ⚠️ **这是实现选择，不是架构决定。**
> **Git 不是 Money OS 的运行时传输层，也不是架构依赖。**
> 更换传输不得要求修改本契约或任何项目的业务代码。

### Transport 接口（实现者需满足，非项目需满足）

| 操作 | 语义 |
|---|---|
| `emit(record)` | 写入 outbox，**必须本地成功且立即返回** |
| `flush()` | 尽力上传未同步记录；**允许失败，允许无限期延后** |
| `read(project, kind)` | Money OS 侧只读拉取 |

**至少一次投递。** 消费方以 `id` 幂等处理。**不保证顺序**——顺序由 `recorded_at` 恢复。

## 3. Outbox 语义

| 规则 | 说明 |
|---|---|
| **追加写入** | 只追加，不改写历史。状态变更 = 新记录，不是改旧记录 |
| **后写为准** | 同 `id` 多条时，`recorded_at` 最新者为当前状态 |
| **本地即真相** | 项目的本地记录是权威。Money OS 是副本，不是源 |
| **同步状态不入契约** | 「已同步/未同步」是 outbox 的内部实现细节，不是记录字段 |
| **幂等** | 重复投递同一 `id` + `recorded_at` 必须无副作用 |

## 4. 通用字段规则

| 规则 | 说明 |
|---|---|
| 编码 | UTF-8。参考实现为 NDJSON（每行一个 JSON 对象） |
| 时间 | RFC3339 UTC，例 `2026-08-16T14:30:00Z` |
| 货币 | 金额一律 USD，字段以 `_usd` 结尾；本币另记 `native_amount` / `native_currency` |
| ID | 项目内唯一。Money OS 侧以 `project_id` 前缀消歧 |
| 未知值 | 写 `null` 或省略。**禁止编造** |
| 向前兼容 | 消费方**必须忽略不认识的字段** |

## 5. 六个对象

### 5.1 Project（单对象）

```json
{
  "contract_version": "0.1",
  "project_id": "m1-autopublishing",
  "name": "M1 Digital Asset & Publishing Factory",
  "integration_level": "L2",
  "status": "ACTIVE",
  "base_currency": "USD",
  "repo_url": null,
  "owner_contact": null,
  "recorded_at": "2026-08-16T00:00:00Z"
}
```

`integration_level`: `L0` 仅注册 · `L1` 轻量上报 · `L2` 深度治理
`status`: `ACTIVE` · `PAUSED` · `BLOCKED` · `CLOSED`

### 5.2 WorkItem

```json
{
  "id": "OPP-001",
  "kind": "opportunity",
  "title": "Cracked per-piece article",
  "status": "BLOCKED",
  "blocked_by": "HUMAN_APPROVAL",
  "blocked_detail": "H2 editorial gate; Owner must send from own mailbox",
  "expected_value_usd": 175.0,
  "expected_cost_usd": 0.0,
  "human_minutes_spent": 0,
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

`status`（封闭）: `PROPOSED` · `ACTIVE` · `BLOCKED` · `DONE` · `ABANDONED`

`blocked_by`（封闭，`status=BLOCKED` 时必填）:
`HUMAN_APPROVAL` · `HUMAN_ACTION` · `EXTERNAL_PARTY` · `POLICY_UNKNOWN` ·
`ELIGIBILITY` · `PREREQUISITE` · `CAPABILITY` · `FUNDS`

> **为何是封闭枚举：** M1 一周真实运行显示，状态几乎总是"卡在什么上"，
> 而**卡点类型决定谁能解开**。自由文本无法聚合；枚举能直接回答组合层最重要的问题：
> **有多少预期价值卡在等人身上。**

`kind` 开放：`opportunity` · `asset` · `submission` · `task` · `campaign` · 项目自定义。

### 5.3 Approval

```json
{
  "id": "APR-0001",
  "work_item_id": "OPP-001",
  "gate_type": "EXTERNAL_COMMUNICATION",
  "request": "Send Cracked pitch email from Owner mailbox",
  "risk_note": "Represents Owner identity externally; irreversible once sent",
  "amount_usd": 0.0,
  "decision": "PENDING",
  "decided_by": null,
  "decided_at": null,
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

`gate_type`: `SPEND` · `IRREVERSIBLE` · `IDENTITY_KYC` · `LEGAL_CONTRACT` ·
`EXTERNAL_COMMUNICATION` · `PUBLISH` · `POLICY_UNCLEAR` · `IP_RISK`
`decision`: `PENDING` · `APPROVED` · `REJECTED` · `WITHDRAWN`

**只治理 Money OS 管辖的动作（资本配置、跨项目决策、不可逆外部动作）。**
**业务交易不进此表** —— Monetools 服务一次计算、Pearl 接一个订单，都不需要审批。
这条边界正是"停机不阻业务"成立的根据。

### 5.4 LedgerEntry

```json
{
  "id": "R0002",
  "direction": "REVENUE",
  "date": "2026-08-16",
  "category": "article_fee",
  "counterparty": "Cracked",
  "work_item_id": "OPP-001",
  "gross_usd": 150.0,
  "fees_usd": 0.0,
  "net_usd": 150.0,
  "cash_received_usd": 0.0,
  "cash_received_at": null,
  "human_minutes": 45,
  "native_amount": null,
  "native_currency": null,
  "note": "",
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

`direction`: `REVENUE` · `COST`

**两个字段来自 M1 实践，非推演：**
- **`net_usd` 与 `cash_received_usd` 必须分开** —— 已确认收入 ≠ 已到账现金
  （Adobe 首笔销售需满 45 天；Freepik 约 2 个月账期）。
- **`human_minutes` 建议填写，允许 `null`** —— 对人工密集型业务（M1）它是判断自动化价值的
  关键输入；对已全自动业务（如 Monetools 的 Web 计算器）恒为 0 无意义，留 `null` 表示"不适用"。
  ⚠️ **本条由 Monetools 兼容性分析改出**：初稿写"必填"，那是把 M1 的特性误当共性。
  见 `docs/COMPATIBILITY_MONETOOLS.md` §4。

**聚合友好性说明（为 Monetools 类业务）：** 高频小额业务（如订阅、按次调用）
**不必逐笔上报**。允许按日/周/月聚合为单条 `LedgerEntry`，
`category` 标注聚合口径，`id` 用区间标识。契约不要求交易级粒度。

### 5.5 Decision

```json
{
  "id": "D0014",
  "title": "Sequence Adobe Stock before Creative Fabrica",
  "choice": "Open Adobe Stock account first",
  "rejected_alternatives": ["Creative Fabrica first", "All four in parallel"],
  "rationale": "CF only accepts designers who already run another online store",
  "evidence_refs": ["EV-094"],
  "reversible": true,
  "outcome": null,
  "outcome_recorded_at": null,
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

**`rejected_alternatives` 与 `outcome` 是 Economic Memory 的全部基础。**
只记录选了什么学不到东西；记录**否决了什么**及**结果**，才能事后检验判断力。
`outcome` 长期为 `null` 是诚实的，编造不是。

### 5.6 Event

```json
{
  "id": "EVT-0001",
  "type": "SUBMISSION_SENT",
  "work_item_id": "OPP-001",
  "payload": {"platform": "Cracked", "channel": "email"},
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

`type` 开放。保留类型（Supervisor 特殊处理）：
`WORK_STARTED` · `WORK_BLOCKED` · `WORK_UNBLOCKED` · `SUBMISSION_SENT` ·
`SUBMISSION_ACCEPTED` · `SUBMISSION_REJECTED` · `REVENUE_RECOGNISED` ·
`CASH_RECEIVED` · `APPROVAL_REQUESTED` · `APPROVAL_GRANTED`

**这是审计日志，不是消息队列。** 无订阅、无投递保证、无顺序保证。

## 6. 集成级别

| 级别 | 项目提供 | 得到 |
|---|---|---|
| **L0 — Registry only** | **无。** Money OS 侧登记一行 | 出现在组合视图 |
| **L1 — Reporting** | `Project` + `LedgerEntry` | 财务汇总、指标、Supervisor 建议 |
| **L2 — Governed** | 再加 `WorkItem` + `Approval` + `Decision` + `Event` | 完整治理：审批追踪、阻塞分析、经济记忆 |

**永久停在 L0 或 L1 是任何项目的合法终态。**
M1 是第一个 L2 客户。Monetools/Tax 初期保持独立，日后经薄适配接入。

## 7. Money OS 的反向承诺

| 承诺 | 含义 |
|---|---|
| **只读** | 永不写入项目系统 |
| **无运行时依赖** | 项目不调用 Money OS 即可完整运行 |
| **停机无影响** | 不可用时项目照常写本地 outbox |
| **不进业务代码** | 永不 import 任何项目代码 |
| **不要求重构** | 接入只需一层薄适配，不得要求改动业务核心 |
| **可随时退出** | 删除本地适配即完全脱离 |
| **忽略未知字段** | 项目可自由扩展 |

## 8. 稳定性承诺

**v0.1 → v1.0 期间：**
- ✅ 允许：新增可选字段、新增枚举值、新增对象类型、更换 transport
- ⛔ 禁止：删除/重命名字段、改变字段含义、收紧枚举、**新增任何运行时依赖**

**六个对象的名称在 v1.0 前不变。** 这是外部客户敢写适配的前提。

⚠️ **契约在通过第二个业务（Monetools）的兼容性验证前，不宣称稳定。**
若 Monetools 无法经薄适配映射，**修改的是契约，不是 Monetools。**
