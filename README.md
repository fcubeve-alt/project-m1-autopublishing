# M1 Autonomous Publishing Business

An AI-operated publishing business. The AI owns research, strategy, platform selection, content, compliance, measurement and iteration. The Owner supplies only what is genuinely human-bound: identity, payment authority, and editorial approval.

**Cycle C1 opened:** 2026-08-15 · **Revenue to date:** $0.00 · **Committed cost to date:** $0.00

---

## Start here

| If you want to... | Read |
|---|---|
| Understand what changed vs. the original brief | **[`STRATEGIC_REVIEW.md`](STRATEGIC_REVIEW.md)** ← start here |
| See the decision rules learned so far | **[`OPERATING_RULES.md`](OPERATING_RULES.md)** |
| Know what the Owner must actually do | [`docs/HUMAN_GATES.md`](docs/HUMAN_GATES.md) |
| Check why KDP beat the alternatives | [`docs/OPPORTUNITY_COMPARISON.md`](docs/OPPORTUNITY_COMPARISON.md) |
| See the honest case *against* the first product | [`docs/A0001_BUYER_INTENT.md`](docs/A0001_BUYER_INTENT.md) |
| See the 30-day test | [`docs/EXPERIMENT_PLAN_30D.md`](docs/EXPERIMENT_PLAN_30D.md) |
| See the product | [`assets/A0001-ai-disclosure-handbook/`](assets/A0001-ai-disclosure-handbook/) |

## The one-paragraph version

Live research invalidated the brief's core assumption. The creator/per-read platforms it centred on have specifically banned or de-monetised AI-assisted publishing: Medium forbids paywalling AI-generated writing whether disclosed or not, paying literary magazines refuse AI-assisted work, HubPages is winding down, Quora's partner program is closed, Kindle Vella is dead, and Vocal — the brief's own template candidate — could not be verified at all. The route was replaced. The Mission was not.

The corrected strategy competes on **recency instead of volume**: publish into topics whose governing rules changed within the last 30 days, where no back catalogue can exist, sold through the one channel that gives an unknown publisher free access to buyers with purchase intent on day one — Amazon's search box, which expressly permits AI-generated content subject to disclosure.

First asset: a cross-platform AI-disclosure compliance handbook, built on the EU AI Act Article 50 obligations that became binding **2026-08-02** and the Etsy rule change effective **2026-08-11**.

## Repository map

```
STRATEGIC_REVIEW.md          Independent assessment; corrections to the brief
docs/                        Phase-0 deliverables
  PLATFORM_LONG_LIST.md        43 platforms, evidence-graded
  PLATFORM_TOP5.md             Ranked selection + rejections
  PLATFORM_RULES_MATRIX.csv    Machine-readable rules matrix
  CONTENT_INTELLIGENCE_REPORT.md  Where demand outruns supply
  PAYMENT_FEASIBILITY.md       Payout mechanics; no nationality guesswork
  COMPLIANCE_POLICY.md         Binding on all assets
  EXPERIMENT_PLAN_30D.md       The test, and its kill rule
  HUMAN_GATES.md               The ~2-3 hours of Owner time required
  BUILD_VS_NO_BUILD.md         Why no software is being built
  DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md  Environment + capability review
ledger/                      REVENUE_LEDGER.csv · COST_LEDGER.csv · DECISION_LOG.md
jobs/                        Portable Writing Jobs (brief §16)
assets/                      Content assets
```

## Operating principles in force

- **Evidence over memory.** `UNKNOWN` is written as `UNKNOWN`, never filled from model memory.
- **Realised net profit**, not article count, is the measure.
- **M1-A** (first sale recorded) and **M1-B** (cash received) are tracked separately — a recorded sale is not realised cash, and reporting it as such would be false.
- **Prove the loop, then automate it.** No software is being built until revenue justifies it.
- **The Owner must never be required to invent the next task.**
- No fake identity, no CAPTCHA bypass, no deceptive AI disclosure, no policy evasion. Platforms that forbid what we are get excluded, not worked around.

## Current status

| Item | State |
|---|---|
| Phase 0 deliverables | ✅ Complete |
| Reviewer challenge round 1 | ✅ 5 corrections accepted, 1 conclusion defended with evidence |
| Operating rules v1.1 | ✅ Seven rules, each traced to a specific failure |
| **Opportunity portfolio** | ✅ **Open** — 10 candidates, states tracked |
| Channel (Amazon KDP, wide/non-exclusive) | ✅ **Decision** — survives quantified comparison and re-test |
| **P1 — profession-specific compliance workbook** | 🟢 **VALIDATING** — now leads. Niche selection pending |
| **A0001 — general handbook, $6.99 ebook** | 🟠 **HOLD** — failed the counterfactual test. No longer plan of record |
| Cover + manuscript (A0001) | ✅ Complete; research carries forward to P1 at $0 |
| Owner payout setup (H1) | 🔴 **Blocked — awaiting country of tax residence.** Product-independent; needed for any KDP route |
| M1-A first sale recorded | ⏳ Pending candidate selection |
| M1-B cash received | ⏳ ~60–90 days after first sale |

**Honest status:** the **channel** is decided on evidence and survived re-testing. The **product** did not. A0001 was demoted from the plan of record after failing the counterfactual test — it is an explanation priced for consumers, when the evidence says buyers pay premium for *tools* in professional niches they can expense. Its research transfers to P1 at zero marginal cost, which is a forward-looking reason, not a sunk-cost one.

See [`docs/OPPORTUNITY_PORTFOLIO.md`](docs/OPPORTUNITY_PORTFOLIO.md) for all candidates and the stopping rule.
