# 兼容性验证 #2 — Monetools / Tax

**目的:** 契约在通过第二个**业务模型显著不同**的项目验证前不宣称稳定。
**结论先行:** 验证**部分完成**，并**已因此修改契约一处**。

---

## 1. 证据限度 —— 必须先说清

**我没有审计 Monetools 的代码。** 本会话尝试接入 `Monetools/Monetools` 失败：

```
add_repo: cross-tier adds are not supported in v1:
requested "monetools/monetools" but session already has repos from owner(s) [fcubeve-alt]
```

它属于不同 owner，本会话无法跨 owner 添加。

**全部可得证据是两行：**
1. `Project_M_AI_Development_Environment_Preflight_Skills_Spec_v1.1` — *"Project examples:
   **Monetools calculators**, LUVYMIA storefront, Money OS dashboard"*
2. `Project M Master v1.3.1` — *"M2-B 自主经营 Monetools"*
3. Owner 口述：Monetools / monetools.com 是**税务工具业务**

**因此本文是"业务形态兼容性分析"，不是"结构兼容性验证"。**
真正的验证需要：以 Monetools 为初始 source 开新会话，或 Owner 提供其数据结构。
**在那之前，契约标记为 `PROVISIONAL`，不是 `STABLE`。**

## 2. 两个业务的形态差异（这正是它作为第二参照点的价值）

| 维度 | **M1（第一客户）** | **Monetools / Tax（第二参照）** |
|---|---|---|
| 收入形态 | 少量大额、离散（$100–250/篇、版税） | 推测：**高频小额**（订阅/按次/广告/联盟） |
| 交易笔数 | 每月个位数 | 推测：每月数百至数千 |
| 工作单元 | 机会 → 资产 → 投稿 → 接受 | 推测：**无投稿概念**，持续运营 |
| 人工投入 | 高且决定性（每步都卡人） | 推测：**接近零**，自动化 Web 服务 |
| 审批门 | 频繁（开户、KYC、外发邮件） | 推测：**日常运营几乎没有** |
| 阻塞形态 | 几乎全是 `HUMAN_*` | 推测：多为技术/流量，非人工门 |

## 3. 逐对象兼容性判定

| 对象 | 判定 | 说明 |
|---|---|---|
| **Project** | ✅ 兼容 | 八个字段全部业务中立 |
| **LedgerEntry** | ⚠️ **发现问题 → 已改契约**，见 §4 | |
| **WorkItem** | ✅ 兼容 | `kind` 开放；Monetools 可用 `campaign`/`feature`/`experiment`。`status` 五值足够 |
| **Approval** | ✅ 兼容且**可完全不用** | 日常运营不产生审批。L1 不要求此对象 |
| **Decision** | ✅ 兼容 | 业务中立 |
| **Event** | ✅ 兼容 | `type` 开放 |
| **blocked_by 枚举** | ✅ 兼容 | 八个值中 `CAPABILITY`/`EXTERNAL_PARTY`/`FUNDS` 对 SaaS 同样成立 |

## 4. ⛔ 发现的真实不兼容 —— 已修改契约

### 问题

`CONTRACT.md` v0.1 初稿写：**"`human_minutes` 必填"**。

理由曾是：没有它就无法判断一条业务线是否值得自动化。**这个理由在 M1 成立，在 Monetools 不成立。**

一个**已经全自动**的 Web 计算器，其每一笔订阅收入的 `human_minutes` 恒等于 0。
强制填写会：
- 迫使 Monetools 在导出层写入无意义的常数 0；
- 或迫使它改动记账结构以产生一个它不需要的字段。

**两者都属于"让第二个业务迁就契约"，而你的指令明确禁止这一点。**

### 修改

**`human_minutes` 由「必填」降为「建议」，允许 `null`。**

- **人工密集型业务（M1）应当填写** —— 它仍是判断自动化价值的关键输入。
- **已自动化业务（Monetools）可留 `null`** —— 表示"不适用"，而非"未知"。
- 聚合器把 `null` 与 `0` 同等对待，不影响财务汇总。

> **这次修改就是本流程存在的意义。** 契约初稿是从 M1 一个业务的形状里长出来的，
> 第二个业务立刻暴露了一处把 M1 特性误当共性的地方。
> **修改的是契约，不是 Monetools。**

## 5. 已在契约中预留、无需再改的一处

`LedgerEntry` 已写明**允许聚合**：

> 高频小额业务不必逐笔上报。允许按日/周/月聚合为单条 `LedgerEntry`。
> 契约不要求交易级粒度。

Monetools 若有数千笔小额交易，可按月导出 12 行/年，而非数万行。
**这条是在写契约时就为它预留的，不是事后补救。**

## 6. Monetools 的接入路径（不要求改动其税务系统）

| 阶段 | 动作 | 对 Monetools 核心系统的改动 |
|---|---|---|
| **现在** | **L0 — 仅注册。** 已登记在 `projects/registry.yaml` | **零** |
| 需要组合财务视图时 | **L1** —— 导出 `project.json` + 按月聚合的 `ledger.ndjson` | **零**：一个只读导出脚本，几十行 |
| 仅当需要跨项目治理 | L2 | 可选，可能永不需要 |

**判定：Monetools 能否经薄适配映射契约而不重构税务系统？**
**→ 能（L1 层面）**，前提是 §4 的修改生效。**§4 之前的契约做不到。**

## 7. 遗留风险

| 风险 | 状态 |
|---|---|
| 未审计真实代码 | **公开承认。** 契约保持 `PROVISIONAL` |
| 可能还有未发现的不兼容 | 需真实接入才能知道 |
| Pearl Bridal 完全未知 | **不作任何推断。** 不映射到 LUVYMIA 或任何现有项目名 |

**契约何时可宣称 STABLE：** Monetools 完成一次真实 L1 导出并通过 `moneyos validate`。
**在此之前，`contract_version` 保持 `0.1`，且 §8 稳定性承诺尚未生效。**
