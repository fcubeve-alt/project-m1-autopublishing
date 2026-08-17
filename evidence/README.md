# EVIDENCE STORE

**建立:** 2026-08-16 · **数据:** `evidence/EVIDENCE_STORE.csv` · **当前 35 条 claim**

Brain、Auditor、以及任何新 Session **先读本 Store，再决定是否新增搜索**。

---

## 1. 为什么按 claim 管理而不是按平台

这是 R15a 的直接落地：**证据等级属于 claim，不属于行。**

A-001 的根因就是「验证了某平台的一个属性，就对该平台其他属性产生了虚假信心」。同一平台的
不同断言可以处在完全不同的可信度上——Vocal 的支付轨是 `P` 已验证，它的阅读费率现在是
`CONFLICTED`，而它的「发布是否需要 Stripe」是 `PARTIAL`。按行管理会把这三者压成一个等级，
那正是要避免的错误。

## 2. 字段

| 字段 | 含义 |
|---|---|
| `claim_id` | `EV-NNN`，永久不复用。撤回的 claim 保留并标 `WITHDRAWN`，不删除 |
| `platform` | 平台名 |
| `claim` | **单一可证伪的断言。** 一条 claim 只讲一件事——复合句要拆开 |
| `source` | 具体来源（URL 或来源描述），不写"搜索结果" |
| `source_tier` | 见 §3 |
| `verified_date` | 该 claim 最后一次被核实的日期，非写入日期 |
| `status` | 见 §4 |
| `scope` | **该 claim 覆盖什么、不覆盖什么。** 最重要的字段，见 §5 |
| `conflict_state` | 与哪条 claim 冲突、是否已解决；无冲突写 `none` |
| `notes` | 决策含义、来源出处、后续动作 |

## 3. source_tier

| Tier | 含义 |
|---|---|
| `P` | 平台官方页面（help/ToS/官方资源页），已取到内容 |
| `S` | 可信二手来源，或对官方内容的二手转述 |
| `R` | 报道／行业传闻／单一实践者叙述 |
| `U` | 有说法但来源不可信或无法定位 |
| `-` | 无来源（用于 `UNKNOWN` 行） |

**域名不等于权威。** `vocal.media/journal/…`、`vocal.media/writers/…`、`simily.co/all-stories/…`
是**用户投稿内容**，托管在官方域名上但不是官方声明。只有 `vocal.media/resources/…`、
`help.vocal.media/…` 这类才算 `P`。按域名限制搜索只约束了"谁托管"，没约束"谁写的"。

## 4. status

| Status | 含义 | 可否作决策依据 |
|---|---|---|
| `VERIFIED` | 已核实 | ✅ |
| `PARTIAL` | 方向明确但细节未定（如只取到片段） | ⚠️ 可作方向性依据，不可作数值依据 |
| `CONFLICTED` | **两条证据互相矛盾，未解决** | ⛔ **任何一侧都不得单独引用** |
| `UNKNOWN` | 查过，无结论 | ⛔ 且 **不得作为淘汰依据**（R1） |
| `WITHDRAWN` | 曾被采信、后被推翻 | ⛔ 保留仅供追溯 |

**`UNKNOWN` 与 `CONFLICTED` 的区别很重要：** `UNKNOWN` 是没找到；`CONFLICTED` 是找到了两个
互斥的答案。后者比前者更危险，因为任一侧单看都像已验证。

## 5. scope 字段 —— 本 Store 存在的主要理由

**scope 记录一条 claim 覆盖到哪里为止。** 本项目已经犯过两次同形错误，都是 scope 越界：

1. **EV-005（Vocal 走 Stripe）** 的 scope 是**提款**。它一度被当成「Vocal 不可用」，但
   EV-003 证明任何国家都能注册、EV-006 证明收入可以先挂在钱包里。*提款受限 ≠ 不能参与。*
2. **EV-019（Listverse 走 PayPal/Bitcoin）** 的 scope 是**支付轨**。我据此宣称 Listverse
   不受 H1 约束——错的，因为 EV-020 显示**投稿准入**被限制在 7 国。*能收款 ≠ 允许投稿。*

**所以：一个平台的 Human Gate 必须写清它卡在哪一环——注册 / 发布 / 参赛 / 提款——不能整体
标注为"被 H1 阻塞"。** 也不能把单个平台的门槛升级成整个 M-A 的门槛。

## 6. 使用协议

**新增搜索前：**
1. 先查本 Store。已是 `VERIFIED` 的事实**不得重复研究**。
2. `CONFLICTED` 与 `UNKNOWN` 才是搜索的合法目标，且按决策影响排序。
3. 新证据写回 Store，而不是只写进某份报告——报告会过期，Store 是单一真相源。

**写回时：**
- 一条 claim 一件事。
- 明确写 scope，包括它**不**覆盖什么。
- 发现矛盾时**双方都标 `CONFLICTED` 并互相引用**，不要私自选边。
- 推翻旧 claim 时标 `WITHDRAWN` 并在新 claim 的 `conflict_state` 里写明 supersedes。

## 7. 当前未决项（按决策影响排序）

| 优先 | 项 | 影响 |
|---|---|---|
| 🔴 1 | **EV-001 vs EV-002** — Vocal 免费档究竟还能否靠阅读赚钱 | 直接决定 Vocal 的经济性是否成立 |
| 🔴 2 | **EV-004** — Vocal「发布所需的验证」是否等于绑定 Stripe | 决定 Vocal 实验能否在 H1 未答时启动 |
| 🟡 3 | **EV-027** — Pratilipi AI 政策 | 决定 #3 能否进入发布 |
| 🟡 4 | **EV-020** — Listverse 七国限制需升级到 `P` | 该条正在承担排名权重，却只是 `S` |
| 🟢 5 | **EV-017** — Simily AI 政策 | Simily 已因流量降级，优先级随之下降 |
| 🟢 6 | **EV-016** — Simily 存活状态 | 同上 |

## 8. 迁移来源

由 `audit/V1-V7_VERIFICATION.md`、`docs/PLATFORM_RULES_MATRIX.csv`、
`docs/PLATFORM_LANDSCAPE_V2.md` 迁入，**未重复任何已验证事实的研究**。
本轮仅新增一次搜索（Vocal 发布前置条件），该搜索直接产出 EV-002/EV-003/EV-004。

那三份文件继续保留：矩阵作平台横向视图，V1-V7 作 A-001 审计的追溯记录，landscape 作历史。
**发生分歧时以本 Store 为准。**
