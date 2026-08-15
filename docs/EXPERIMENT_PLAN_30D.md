# 30-DAY EXPERIMENT PLAN

**Cycle:** C1 · **Start:** 2026-08-15 · **End:** 2026-09-14

## Hypothesis under test

> A single, rigorously sourced, edition-dated compliance reference, published to Amazon KDP (wide, non-exclusive) into a topic whose governing rules changed within the last 30 days, will produce **at least one attributable external sale within 30 days of listing**, at a total cash cost of **$0**.

This is deliberately the smallest test that can falsify the core strategic claim in `STRATEGIC_REVIEW.md` — that **recency beats volume** as a discovery strategy for an AI-native publisher. It does not test whether the business is profitable at scale. It tests whether the loop closes at all.

## Success criteria

| Level | Criterion | Meaning |
|---|---|---|
| **M1-A** | ≥1 attributable external sale recorded | Loop closes. Strategy validated at minimum viable scale |
| **M1-B** | Cash received in the Owner's account | Mission milestone. Expected ~60–90 days post-sale, i.e. **outside this cycle by design** |
| **Stretch** | ≥30 sales (~$210 royalty at $9.99 / 70%) | Signal worth reinvesting in |
| **Falsified** | 0 sales in 21 days of live listing | Recency thesis fails on execution. Diagnose before re-running |

Recording M1-A as success while M1-B is still outstanding is **not** a claim of realised profit. The ledger tracks them separately and reports accordingly.

## Schedule

| Day | Action | Owner | Gate |
|---|---|---|---|
| 1 | Phase 0 deliverables; strategy set; Asset A0001 drafted | AI | ✅ done 2026-08-15 |
| 1 | Writing Job JOB-0001 issued | AI | ✅ done |
| 2–4 | Manuscript completion, critic pass, compliance pass, source re-verification | AI | — |
| 5 | **Human Editorial Gate** — Owner reviews A0001 | **Owner** | **H2 — blocking** |
| 5 | **Payout setup begins in parallel** — KDP account, tax interview, bank | **Owner** | **H1 — blocking, start early** |
| 6–7 | Revisions from Owner feedback → editorial memory | AI | — |
| 8 | Cover (original typographic design), metadata, categories, keywords, description | AI | — |
| 9 | **Upload and publish, with AI-generated disclosure** | **Owner** (AI prepares complete package) | **H3** |
| 10–12 | Amazon review period; listing goes live | — | — |
| 12–30 | Daily sales/rank observation; ledger updates | AI + Owner reporting | — |
| 15 | **Decision point:** if ≥3 sales, pay $20 for Draft2Digital wide distribution. If 0 sales, diagnose instead of spending | AI recommends, Owner authorises | Spend gate |
| 21 | **Diagnosis checkpoint** — if 0 sales, run the diagnosis tree below | AI | — |
| 30 | Cycle review; keep / improve / kill; C2 planned | AI | — |

**Critical path note:** H1 (payout setup) is scheduled at day 5, not day 9, specifically because a US TIN application can take **up to 7 weeks** if no acceptable local TIN exists. Starting it late is the single most likely cause of a missed cycle.

## Diagnosis tree (day 21, if zero sales)

Zero sales is data, not failure — but only if it is diagnosed rather than repeated.

```
0 sales at day 21
├── Impressions ≈ 0?  → DISCOVERY failure
│   └── Wrong categories/keywords. Fix metadata (cheap, same asset).
│       If a second metadata configuration also returns ~0 → the recency
│       thesis fails on Amazon's surface. Pivot to a distribution-led route.
├── Impressions > 0, clicks ≈ 0? → PACKAGING failure
│   └── Title/cover/price. Fix cover and subtitle. Asset unchanged.
├── Clicks > 0, sales ≈ 0? → CONVERSION failure
│   └── Sample or description under-sells. Rewrite description; re-cut sample.
└── Cannot observe any of the above? → INSTRUMENTATION failure
    └── Fix reporting first. An unmeasurable experiment teaches nothing
        and must not be re-run blind.
```

**Kill rule:** if two consecutive metadata configurations produce ~0 impressions over 14 days, the "recency into marketplace search" hypothesis is falsified for this surface. Do not write a second book to test the same failed assumption — that is the volume trap this strategy exists to avoid.

## Explicitly out of scope for C1

Deliberately excluded to keep the test small and honest:

- Building any software or automation (brief §19 — prove the loop first).
- Paid advertising, including Amazon Ads. This cycle tests **organic** discovery; adding paid traffic would contaminate the result.
- Multi-title catalogue. Catalogue size is the strongest income correlate long-term, but building one before validating a single title is the mass-production error.
- Newsletter, Patreon, audiobook, translations. All are downstream of a validated asset.
- Second platform beyond the day-15 D2D gate.

## What C1 teaches regardless of outcome

| Outcome | Learning |
|---|---|
| Sales | Recency thesis holds. C2 scales the *method* — next recency window (2026-12-02 EU transitional deadline) — not the volume |
| Impressions, no sales | Discovery works, packaging or conversion is the problem. Cheap to fix, asset intact |
| No impressions | Marketplace search is not reachable cold in this category. Requires a distribution-led strategy, and the Top-5 ranking must be revisited |
| Blocked at H1 | Payout geography is the binding constraint, and platform selection must be re-run against the Owner's actual rails |
