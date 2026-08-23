# Money OS Shared Core v0.1 — As-Is Audit

**日期:** 2026-08-16 · **状态:** 设计阶段，尚未实现
**位置说明:** 本目录是**暂存区**。Money OS 建库后整体迁出，M1 只保留一个指针。

---

## 0. 三条必须先讲清的事实

### 0.1 Tax 与 Pearl Bridal Jewelry：我没有任何资料

全库检索 + 四份上传架构文档检索，**"Tax" 与 "Pearl Bridal Jewelry" 均无任何出现**。
文档中的三个业务是 **M2-A LUVYMIA · M2-B Monetools · M2-C Cubewithin**（后者标注 DESIGNED / NOT ACTIVE）。
账号下 5 个仓库为 `photomanage` · `bulesky` · `Monetools/Monetools` · 本项目 · `literary-perspectives`。

**因此我不会虚构这两个系统的架构。** 契约按「对我一无所知的客户也必须成立」来设计——
这反而是正确的约束：一个需要知道客户内部结构才能用的契约，本来就不叫契约。

### 0.2 没有 Money OS 代码库可复用

上一轮已验证：账号下无 kernel 仓库。任务书里要复用的 Opportunity Router / Model Router /
Agent Orchestrator / Tool Layer 全部**不存在**。**v0.1 是从零建，不是迁移。**

### 0.3 本次方向与两周前提交的原则冲突

`MASTER_PLAN.md` 写着 *Build only what the business proves it needs*，且 Money OS 项目书自己
明令「不要先建立一座庞大的 Money OS，再寻找赚钱方法」。M1 当前收入 $0、从未提交过任何东西。

**若依据是 M1 的验证结果 → 不该现在建。若依据是投资组合（多个真实业务并行）→ 站得住。**
我按后者执行，并把这条冲突记录在案，不再重复。

---

## 1. M1 现有资产逐项映射到 v0.1 八大组件

**原则：已存在的直接复用，不重建。**

| v0.1 组件 | M1 现状 | 复用判定 |
|---|---|---|
| **Project Registry** | ❌ 不存在（M1 是单项目，无需注册表） | **新建**（Money OS 侧） |
| **Project Contract** | ❌ 不存在 | **新建**（Money OS 侧，本轮核心产出） |
| **Work / Task Status** | 🟡 **概念存在但无结构** —— `OPPORTUNITIES.csv` 的 `status` 列已在跑真实状态机（`ASSET_READY_PENDING_H2` / `BLOCKED_BY_AUTHOR_ELIGIBILITY` / `POLICY_VERIFIED_ACCOUNT_GATE` / `BLOCKED_BY_STORE_PREREQUISITE`） | **提炼其状态语义**，不重造 |
| **Approval Gate** | ✅ **已存在且在运行** —— `PROJECT_STATE.md` §7 的 H1/H2 人工门；Cracked pitch 真实卡在 H2 | **直接提炼为契约对象**，M1 已验证它有效 |
| **Financial Ledger** | ✅ **已存在** —— `REVENUE_LEDGER.csv`（13 列）+ `COST_LEDGER.csv`（8 列），含 `human_minutes` | **作为 v0.1 ledger schema 的直接来源** |
| **Decision / Economic Memory** | 🟡 **Decision 已存在**（`ledger/DECISION_LOG.md`，D0001–D0013 含理由与被否方案）<br>❌ **Economic Memory 不存在**，且**当前零销售数据** | Decision **复用**；Economic Memory **v0.1 只定 schema，不填数据** |
| **Events / Metrics / Status** | 🟡 以 `SESSION_HANDOFF.md` + 提交记录形式存在，非结构化 | **新建轻量事件流** |
| **Supervisor** | 🟡 以 `NEXT_REAL_REVENUE_PLAN.md` 的优先级队列形式存在（人读） | **提炼为机器可读队列** |
| *（额外）* **Evidence Store** | ✅ **已存在** —— `evidence/EVIDENCE_STORE.csv`，88 条 claim，按 claim 分级、含 scope 与 conflict_state | ⚠️ **不列入 v0.1**——见 §3 |

## 2. M1 现有 CSV 表头（v0.1 schema 的真实来源）

```
REVENUE_LEDGER  entry_id,date,platform,asset_id,event_type,units,gross_revenue_usd,
                platform_fee_usd,net_royalty_usd,payout_received_usd,payout_date,
                human_minutes,notes
COST_LEDGER     entry_id,date,category,description,amount_usd,human_minutes,asset_id,notes
OPPORTUNITIES   opportunity_id,platform,opportunity_type,producer_line,expected_revenue_usd,
                expected_cost_usd,eligibility,policy_status,roi_note,evidence,status
SUBMISSIONS     submission_id,platform,asset_id,submitted_at,channel,status,
                rejection_reason,accepted_at,revenue_usd,notes
ASSETS          asset_id,asset_family_id,producer_type,title,format,cost_usd,human_minutes,
                rights_status,qa_status,platform_status,created,notes
```

**这些不是设计草稿，是已在真实项目里跑了一周的表。** v0.1 的 ledger 与 work-item schema
应当从它们**向上抽象**，而不是另起一套再要求 M1 迁移。

## 3. 明确不进 v0.1 的东西

| 不进 | 原因 |
|---|---|
| **Evidence Store** | 它是**研究方法论组件**，不是多项目共享核心。Tax 与 Pearl Bridal 未必做平台政策研究。**留在 M1**；若第二个项目也需要，再提升为共享 |
| Opportunity Router · Model Router · Agent Orchestrator · Tool Layer | 三个项目都还没有跑通一次真实闭环，路由无对象可路由 |
| 数据库 | 见 `01_ARCHITECTURE` §2——v0.1 无运行时，用不上 |
| Dashboard / Web UI | 零数据 |
| **Economic Memory 的实际数据层** | 零销售数据。**只定 schema，留空表** |
| 任何 M1 业务逻辑 | 图像生成、文章写作、Adobe 投稿、平台 Adapter —— 全部留在 M1 |

## 4. 审计结论

**八个 v0.1 组件里，两个已在 M1 真实运行（Approval Gate、Financial Ledger），
两个部分存在（Work Status、Decision），四个需新建（Registry、Contract、Events、Supervisor）。**

**最大的复用价值不是代码——是 M1 已经验证过的状态语义与账本字段。**
Money OS v0.1 的正确做法是把它们**标准化**，而不是发明新的。
