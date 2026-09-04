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


---

# ⚡ 修订 2026-08-27 — 第二通道搜索结束,优先级反转

## 发生了什么

Cracked 已投出(2026-08-17),静默 10 天。为避免单线程押在一个收件箱上,
去开第二条稿费通道 —— **两次尝试都失败,且失败方式不同**,合起来暴露一个
此前分析漏掉的结构性约束。详见 `docs/PER_PIECE_MARKET_STRUCTURE.md`。

**稿费市场分三型,只有一型适配我们:**

| 型 | 买什么 | 例 | 判定 |
|---|---|---|---|
| A 亲身经历型 | 作者的真实人生 | Narratively | ⛔ 无法诚实生产 |
| B 岗位型 | 履历与产能 | Motley Fool(月产 20 篇+履历要求) | ⛔ 超出范围 |
| **C 选题型** | **一个可研究的角度** | **Cracked · Listverse** | ✅ 唯一适配 |

**已知 C 型只有两个,其中 Listverse 被 H1 卡死。**
覆盖审计已扫过 45+ 候选,继续找第三个的边际价值已明显下降(R17 停止条件),**停止搜索。**

## 优先级反转

我此前把视觉线称为"更慢的第二选择"。**按结构适配度看,它可能是更好的那条:**

- 视觉资产**既不需要作者的人生,也不需要作者的履历**
- **四个平台全部已验证接受 AI 内容**(写作线上 Cracked 的 AI 政策至今 UNKNOWN)
- **三个可直接开户**(Adobe / Freepik / Vecteezy),对比写作线只有 2 个通道且 1 个被卡
- 一个 Master Asset 可跨四平台再产品化,写作线一篇就是一篇

## 现在的真实状态:两条路都只差 Owner 一个动作

| 优先 | 动作 | 谁 | 解锁 |
|---|---|---|---|
| **1** | **告知税务居住国(H1)** | 🔴 Owner | Listverse:$100/篇 · 30 天付清 · 无起付线。**一句话的事** |
| **2** | **注册 Adobe Stock** | 🔴 Owner | 视觉线首个通道。政策已验证接受 AI,$25 最低提现,无前置网店要求 |
| 3 | 等 Cracked 判断点 | — | 2026-09-16,规则已预设 |

**Agent 侧目前没有能直接产生真实收入的动作。**
这不是"没事做",是诚实的状态:**该做的研究已经做完,剩下的是人的动作。**
继续搜索平台、继续完善系统,都只会制造 v1.0 §15 明确禁止的"没有商业价值的忙碌"。
