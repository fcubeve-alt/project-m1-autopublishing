# NEXT_REAL_REVENUE_PLAN

**唯一问题：从当前状态到第一笔真实收入，最短路径是什么？**
**日期:** 2026-08-16 · 当前收入 **$0.00**

---

## 现实判断

三条线各自卡在哪：

| 线 | 卡点 | 能否绕过 |
|---|---|---|
| **Cracked（写作）** | 稿件质量不达标 + 通道现行性未验证 | ✅ **两者都由 Agent 解决，不需 Owner** |
| **Visual（图库）** | 零账号、零资产、四平台政策未验证 | 🟡 政策验证不需 Owner；**开户必须 Owner** |
| **Wirestock（主动任务）** | 零账号 | ❌ 必须 Owner |

**→ 最短路径是 Cracked。** 它是唯一一条 Agent 可以独立推进到「只差 Owner 按发送键」的线。

---

## 执行队列（按优先级）

### P0-1 · 验证 Cracked 现行招稿通道
| | |
|---|---|
| **Action** | 一次搜索，确认现行招稿页/邮箱/表单是否仍运作 |
| **Owner / Agent** | **Agent** |
| **Dependency** | 无 |
| **Cost** | 1 次搜索 |
| **Expected Value** | **极高** —— 决定后续所有 Cracked 工作是否有意义 |
| **Gate** | 无 |
| **Evidence of Completion** | Evidence Store 新增 claim，状态 ≠ UNKNOWN |

### P0-2 · 按 QA 裁决重写 Pitch
| | |
|---|---|
| **Action** | 砍到 2–3 个（主推 #4 诉讼产物）；改为 Cracked 语域与编号清单式标题；打散重复句式；#4 预先落实 2–3 个具体判例；保留并复查 AI 披露 |
| **Owner / Agent** | **Agent** |
| **Dependency** | P0-1（若通道已废则改投他处） |
| **Cost** | 2–3 次搜索（判例查证） |
| **Expected Value** | 高 —— 当前版本我自己判定 REVISE，不值得发 |
| **Gate** | 无 |
| **Evidence of Completion** | `PITCH_PACKAGE.md` v2，且自审裁决为 PASS |

### P1-1 · Owner 审阅并发送
| | |
|---|---|
| **Action** | 审阅 v2 → 用 Owner 本人邮箱发出 |
| **Owner / Agent** | 🔴 **Owner** |
| **Dependency** | P0-2 |
| **Cost** | 约 10 分钟 Owner 时间 |
| **Expected Value** | **这是唯一能产生真实市场反馈的动作** |
| **Gate** | **H2 编辑审批 + 外发邮件 Gate** |
| **Evidence of Completion** | `ledger/SUBMISSIONS.csv` 出现第一条记录 |

### P1-2 · 建 Submission / Opportunity / Asset 三张 CSV
| | |
|---|---|
| **Action** | 建表并回填已有资产（A0001、A0002）与机会（26 候选中的 Top） |
| **Owner / Agent** | **Agent** |
| **Dependency** | 无（可与 P0 并行） |
| **Cost** | 0 搜索 |
| **Expected Value** | 中 —— 没有 Submission 表就无法追踪第一笔收入来源 |
| **Gate** | 无 |
| **Evidence of Completion** | 三张 CSV 存在且非空 |

### P2-1 · 四个视觉平台 AI 政策验证
| | |
|---|---|
| **Action** | Adobe Stock / Freepik / Vecteezy / Creative Fabrica **各自独立**验证当前 AI 投稿政策与披露要求 |
| **Owner / Agent** | **Agent** |
| **Dependency** | 无 |
| **Cost** | 4 次搜索 |
| **Expected Value** | 高 —— `Unknown → BLOCK`，不验证则一张图都不能传 |
| **Gate** | 无 |
| **Evidence of Completion** | Evidence Store 四条 claim，各自独立取证，**禁止互相推断** |

### P2-2 · Owner 开视觉平台账号
| | |
|---|---|
| **Action** | 注册 + 身份 + 税务 + 支付 |
| **Owner / Agent** | 🔴 **Owner** |
| **Dependency** | P2-1 通过 |
| **Cost** | Owner 时间，各平台不等 |
| **Expected Value** | 高，但**慢于 Cracked** |
| **Gate** | **Account / KYC / Tax Gate** |
| **Evidence of Completion** | 账号可上传 |

### P3 · 暂不启动
Wirestock 主动任务线 · Economic Memory · 任何代码 · Phase 2 渠道。

---

## 分工总结

**Agent 现在就做（无需 Owner）：** P0-1 · P0-2 · P1-2 · P2-1
**Owner 必须做（无可替代）：** P1-1 发送邮件 · P2-2 开户

**最快的一笔钱：** Cracked 单篇 $100–250，接受后进入其付款流程。
**第二快：** 视觉平台，但要先过开户 Gate，且首笔下载收入通常远慢于一次约稿。

---

## 成功阶梯（对齐任务书 §20）

| Level | 内容 | 当前 |
|---|---|---|
| L1 | 资产通过 QA | ⚠️ **未达** —— 自审裁决 REVISE |
| L2 | 真实提交到外部市场 | ❌ |
| L3 | 获得真实市场反馈 | ❌ |
| L4 | **$1+ 可验证外部收入** | ❌ |
| L5 | 重复第二、三次 | ❌ |
| L6 | Economic Memory 找到正 ROI 可重复模式 | ❌ |

**我们连 L1 都还没过。** 这是本轮审计最该记住的一句话。
