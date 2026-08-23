# Money OS Project Contract v0.1

**契约版本:** `0.1` · **稳定性承诺:** 见 §7
**这份文件是权威文本。** `schemas/*.json` 是它的机器可读形式，两者冲突以本文为准。

---

## 0. 契约的一句话定义

> **一个项目通过在自己仓库的 `.moneyos/` 目录下追加写入若干 NDJSON 文件来遵守本契约。
> 除此之外，Money OS 对该项目不作任何要求。**

不要求语言、框架、数据库、在线状态、API、网络可达性。
**手写这些文件是完全合规的接入方式。**

## 1. 通用规则

| 规则 | 说明 |
|---|---|
| **格式** | NDJSON——每行一个 JSON 对象，UTF-8，换行分隔。`project.json` 例外，是单个 JSON 对象 |
| **追加写入** | 文件只追加，不改写历史行。状态变更**发一条新记录**，不是改旧的 |
| **后写为准** | 同一 `id` 多条记录时，`recorded_at` 最新的一条为当前状态 |
| **必填字段** | 见各对象。**未知值写 `null` 或省略，禁止编造** |
| **时间** | RFC3339 UTC，例 `2026-08-16T14:30:00Z` |
| **货币** | 金额一律 **USD**，字段名以 `_usd` 结尾。非美元本币另记 `native_amount` 与 `native_currency` |
| **ID** | 项目内唯一即可。Money OS 侧以 `project_id` 作前缀消歧 |
| **向前兼容** | 消费方**必须忽略不认识的字段**。这是新增字段不构成破坏性变更的前提 |

## 2. 六个对象

### 2.1 `project.json` — 项目自述（单对象）

```json
{
  "contract_version": "0.1",
  "project_id": "m1-autopublishing",
  "name": "M1 Digital Asset & Publishing Factory",
  "integration_level": "L2",
  "status": "ACTIVE",
  "owner_contact": null,
  "repo_url": "https://github.com/fcubeve-alt/project-m1-autopublishing",
  "base_currency": "USD",
  "recorded_at": "2026-08-16T00:00:00Z"
}
```

`integration_level`: `L0` 仅被观察 · `L1` 上报财务与事件 · `L2` 完整治理
`status`: `ACTIVE` · `PAUSED` · `BLOCKED` · `CLOSED`

### 2.2 `work_items.ndjson` — 工作与状态

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

`status` **封闭枚举**：`PROPOSED` · `ACTIVE` · `BLOCKED` · `DONE` · `ABANDONED`

`blocked_by` **封闭枚举**（`status=BLOCKED` 时必填）：

| 值 | 含义 |
|---|---|
| `HUMAN_APPROVAL` | 等人批准 |
| `HUMAN_ACTION` | 等人做只有人能做的事（开户、KYC、签字、发邮件） |
| `EXTERNAL_PARTY` | 等外部方（平台审核、客户回复） |
| `POLICY_UNKNOWN` | 政策未知，按默认拒绝 |
| `ELIGIBILITY` | 不满足准入资格 |
| `PREREQUISITE` | 依赖另一件事先完成 |
| `CAPABILITY` | 缺能力/工具 |
| `FUNDS` | 缺钱 |

> **为什么 `blocked_by` 是封闭枚举而不是自由文本：** M1 一周的实践显示，
> 真正的状态几乎总是"卡在什么上"，而**卡点的类型决定谁能解开它**。
> 自由文本无法聚合，`blocked_by` 可以直接回答组合层最重要的问题：
> **"有多少价值卡在等人身上？"**

### 2.3 `approvals.ndjson` — 审批门

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

**Approval Gate 只治理 Money OS 管辖的动作。**
**业务交易不进这张表**——Pearl Bridal 接订单不需要审批。这条边界是"停机不阻业务"的根据。

### 2.4 `ledger.ndjson` — 财务

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

**两个字段是有意为之，来自 M1 的实践：**
- **`net_usd` 与 `cash_received_usd` 必须分开。** 已确认收入 ≠ 已到账现金。
  M1 的账本从第一天就区分这两者，因为平台账期普遍是数周到数月
  （Adobe 首笔销售需满 45 天、Freepik 约 2 个月账期）。
- **`human_minutes` 是必填。** 没有它就无法判断一条业务线是否值得自动化，
  而这正是 Money OS 存在的主要理由之一。

### 2.5 `decisions.ndjson` — 决策与经济记忆

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
只记录选了什么，学不到任何东西；记录**否决了什么**以及**结果如何**，才能事后检验判断力。
`outcome` 允许长期为 `null`——**留空是诚实的，编造不是。**

### 2.6 `events.ndjson` — 事件流

```json
{
  "id": "EV-0001",
  "type": "SUBMISSION_SENT",
  "work_item_id": "OPP-001",
  "payload": {"platform": "Cracked", "channel": "email"},
  "recorded_at": "2026-08-16T14:00:00Z"
}
```

`type` **开放**（项目可自定义），但以下为保留类型，Supervisor 会特殊处理：
`WORK_STARTED` · `WORK_BLOCKED` · `WORK_UNBLOCKED` · `SUBMISSION_SENT` ·
`SUBMISSION_ACCEPTED` · `SUBMISSION_REJECTED` · `REVENUE_RECOGNISED` ·
`CASH_RECEIVED` · `APPROVAL_REQUESTED` · `APPROVAL_GRANTED`

**这是审计日志，不是消息队列。** 无订阅、无投递保证、无排序保证。

## 3. Money OS 不会做的事（契约保证）

| 保证 | 含义 |
|---|---|
| **只读** | Money OS 永不写入项目仓库 |
| **无运行时依赖** | 项目不调用 Money OS 即可完整运行 |
| **无停机影响** | Money OS 不可用时，项目照常写本地文件，事后聚合 |
| **不进业务代码** | Money OS 不 import 任何项目代码 |
| **可随时退出** | 删除 `.moneyos/` 即完全脱离，业务系统零改动 |
| **未知字段被忽略** | 项目可自由扩展而不破坏契约 |

## 4. 最小合规接入（L1）

一个项目**只需两个文件**即可获得财务汇总与 Supervisor 报告：

```
.moneyos/project.json     ← 一个对象，八个字段
.moneyos/ledger.ndjson    ← 每笔收支一行
```

**没有 SDK 要求，没有网络调用，没有注册流程。** Money OS 侧登记一行仓库地址即可。

## 5. Tax 与 Pearl Bridal Jewelry 的接入路径

我对这两个系统一无所知（见 `00_AS_IS_AUDIT.md` §0.1），因此不为它们预设任何结构。
它们的路径是：

1. **L0 起步** —— 什么都不做，Money OS 侧登记一行，先出现在组合视图里。
2. **需要财务汇总时升 L1** —— 从各自现有系统导出收支为 `ledger.ndjson`。
   那层导出属于它们，几十行，可随时删。
3. **仅当需要跨项目治理时才升 L2**。

**永远停在 L0 或 L1 是完全合法的终态。**

## 6. 版本与演进

`contract_version` 随每条记录走。Money OS 必须能同时消费多个版本。

## 7. 稳定性承诺

**v0.1 → v1.0 期间：**
- ✅ 允许：新增可选字段、新增枚举值、新增对象类型
- ⛔ 禁止：删除字段、重命名字段、改变字段含义、收紧枚举
- **破坏性变更必须递增主版本号，且旧版本至少再支持一个次版本周期。**

**六个对象的名字与 `.moneyos/` 的路径布局，在 v1.0 前不变。**
这是 Tax 与 Pearl Bridal 可以放心写适配的前提。
