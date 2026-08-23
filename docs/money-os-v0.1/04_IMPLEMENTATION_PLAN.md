# Money OS Shared Core v0.1 — 实施计划

**方式：增量实施，每步可独立验证，M1 作为第一个真实客户。**

---

## Gate 0 — 建库（Owner，不可逆）

| | |
|---|---|
| **动作** | 创建 `money-os-core` 仓库，建议 private |
| **执行者** | 🔴 **Owner 确认名称与可见性后由我创建** |
| **理由** | 建库是不可逆外部动作，属 Approval Gate `IRREVERSIBLE` |
| **完成证据** | 仓库存在且可推送 |

**在此之前，本目录五份文档就是全部交付物，不写任何代码。**

---

## Step 1 — 契约先行（无代码）

| | |
|---|---|
| **产出** | `CONTRACT.md` + `schemas/*.json`（六个）+ `projects/registry.yaml` |
| **执行者** | Agent |
| **依赖** | Gate 0 |
| **完成证据** | 六个 schema 能校验 §2 中的示例记录 |

**先冻结契约再写代码**，否则实现会反过来定义契约——那正是"共享核心被第一个客户污染"的方式。

---

## Step 2 — M1 导出器（M1 侧，约 100 行）

| | |
|---|---|
| **产出** | M1 仓库新增 `tools/moneyos_export.py` 与 `.moneyos/` |
| **执行者** | Agent |
| **依赖** | Step 1 |
| **完成证据** | 用 M1 **真实数据**生成六个文件并通过 schema 校验 |

**映射（既有 → 契约）：**

| M1 现有 | → | 契约对象 |
|---|---|---|
| `OPPORTUNITIES.csv` | → | `work_items.ndjson`（`status` 与 `blocked_by` 从现有状态值推导） |
| `REVENUE_LEDGER.csv` + `COST_LEDGER.csv` | → | `ledger.ndjson`（`direction` 区分） |
| `PROJECT_STATE.md` §7 的 H1/H2 | → | `approvals.ndjson` |
| `DECISION_LOG.md` D0001–D0013 | → | `decisions.ndjson` |
| `SUBMISSIONS.csv` | → | `events.ndjson` |
| `ASSETS.csv` · `EVIDENCE_STORE.csv` | → | **不导出**——M1 专有 |

**M1 的 `ledger/*.csv` 仍是真相源。** `.moneyos/` 是导出物，可随时重跑或删除。

> **这一步就是架构的真实测试。** 若 M1 已有的真实状态**无法**干净映射到契约，
> **那是契约错了，不是 M1 错了** —— 回到 Step 1 修契约。
> M1 那些状态是一周真实运行的产物，比任何设计推演更可信。

---

## Step 3 — 校验器与聚合器

| | |
|---|---|
| **产出** | `moneyos/contract.py`（读写+校验）· `moneyos/aggregate.py`（跨项目只读） |
| **执行者** | Agent |
| **依赖** | Step 2 |
| **完成证据** | `tests/fixtures/m1/` 用 M1 真实数据做回归；`moneyos validate` 通过 |

---

## Step 4 — Supervisor

| | |
|---|---|
| **产出** | `moneyos/supervisor.py` + CLI `moneyos status` |
| **执行者** | Agent |
| **依赖** | Step 3 |
| **完成证据** | 对 M1 输出：组合状态 · 阻塞清单（按 `blocked_by` 聚合）· 下一步建议 |

**Supervisor v0.1 只回答三个问题：**
1. 每个项目现在卡在什么上？
2. **有多少预期价值卡在等人身上**（`blocked_by=HUMAN_*`）？
3. 现在最接近真实收入、且不依赖人的下一步是什么？

**它不调度、不派活、不执行。**

---

## Step 5 — 接入指南

| | |
|---|---|
| **产出** | `docs/INTEGRATION_GUIDE.md` |
| **执行者** | Agent |
| **依赖** | Step 4 |
| **完成证据** | 一个对 Money OS 一无所知的人，能只靠该文档完成 L1 接入 |

**验收标准就是给 Tax / Pearl Bridal 用的那份。**

---

## 验收：v0.1 什么时候算完成

| | 标准 |
|---|---|
| **L1** | 契约冻结，六个 schema 可校验 |
| **L2** | **M1 真实数据**通过校验（不是造的样例） |
| **L3** | Supervisor 能对 M1 产出有意义的阻塞分析 |
| **L4** | **第二个项目以 L0 或 L1 接入且未修改自身业务代码** |
| **L5** | Money OS 全程不可用时，M1 照常运作 —— 由构造验证（无运行时依赖） |

**L4 才是架构真正被验证的时刻。** 在此之前，"共享核心"只是一个只有一个客户的库。

---

## 明确不做（v0.1）

服务/API/数据库/消息队列 · Web UI · 认证 · 实时同步 · Model/Opportunity Router ·
Economic Memory 聚合逻辑（只留 schema）· 任何项目业务逻辑 · 自动化调度 ·
Evidence Store 的共享化（第二个项目提出同样需求前不动）。

---

## 风险与已知薄弱点

| 风险 | 处理 |
|---|---|
| **契约被 M1 形状污染** | Step 2 是压力测试；但真正的检验是 L4 第二个客户。**在 L4 之前不宣称契约稳定** |
| **Tax / Pearl 的真实结构未知** | 已在契约中承认（§5）。L0/L1 的存在就是为了让"未知"不阻塞接入 |
| **为零收入的组合建基础设施** | 已在 `00_AS_IS_AUDIT.md` §0.3 记录冲突。**缓解手段是把 v0.1 压到最小**：无服务、无数据库、无 UI |
| **三个项目实际不需要共享** | L4 会暴露这一点。**若第二个客户接入成本高于收益，正确动作是停止 Money OS，而不是加功能** |
