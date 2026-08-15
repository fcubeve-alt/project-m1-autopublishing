# BUILD VS NO-BUILD

**Date:** 2026-08-15
**Decision: BUILD NOTHING in Cycle 1.**

## The reasoning

The brief's §19 Automation Upgrade Gate permits automation only after evidence shows a viable path, meaningful revenue signal, justified cost, and a material reduction in human effort. **None of those four conditions is met yet**, because revenue is currently zero.

There is also a harder constraint. Building software here would produce something that cannot run:

- This session's egress policy **denies outbound HTTPS to every external host tested**. A scraper, price monitor, rank tracker or publishing bot would have nothing to connect to.
- KDP exposes **no public publishing API** for individual authors, so a publishing pipeline has no endpoint.
- The container is **ephemeral** — anything not committed to git is lost when it is reclaimed. Runtime state has nowhere durable to live.

Building an autonomous publishing stack in this environment would produce an impressive artifact that has never once touched a real platform. That is the precise failure mode both source documents warn against.

## What runs manually with existing tools

| Function | Mechanism | Adequate? |
|---|---|---|
| Platform research | `WebSearch` with `allowed_domains` scoping | Yes — reaches primary sources; the only working channel |
| Writing | `CLAUDE_MANUAL_SUBSCRIPTION` (brief §14–17) | Yes — $0 marginal cost |
| Editorial / critic / compliance passes | AI, in-session, against `COMPLIANCE_POLICY.md` | Yes |
| Ledger | CSV in git | Yes — at 1 asset, a database would be pure overhead |
| Task tracking | Markdown + session task list | Yes |
| Publishing | Human (H3) — no API exists | Forced |
| Sales data | Human report (H4) — dashboard unreachable | Forced |
| Memory across sessions | **The git repository itself** | Yes — see below |

## Capability Resolution Ladder, applied honestly

Per brief §11 and Preflight §6, before proposing anything new:

| Capability proposed by the Preflight spec | Ladder result |
|---|---|
| **Firecrawl** (P2) | **REJECT** — a crawling layer over a network path that is closed. Would not function |
| **Agent-Reach** (P0) | **REJECT** — cross-platform reachability is exactly what the egress policy denies. Its value proposition is nullified here |
| **Context7** (P0) | **REJECT** — documentation retrieval for code we are not writing |
| **Playwright** (P0) | **REJECT** — cannot reach external sites; and per brief §7 we do not automate account operations platforms disallow |
| **Taskmaster AI** (P1) | **REJECT** — the session task list already provides this. Preflight §3.3 itself says avoid duplication, and flags credential/path concerns |
| **PraisonAI** (Optional) | **REJECT** — multi-agent orchestration for a one-asset business is architecture theatre |
| **LiveKit Agents** (Project-specific) | **NOT APPLICABLE** — no voice/realtime requirement |
| **OpenMontage** (Project-specific) | **DEFER** — AGPLv3, heavy dependencies, and video is a Phase-3 derivative at best |
| **Persistent memory MCP** (P1) | **REJECT — already solved.** The git repo *is* the persistent, searchable, exportable, project-scoped, secret-free memory the spec describes. Adding an MCP memory server would duplicate it and split the source of truth |

**Every capability in the Preflight spec is rejected or deferred for Cycle 1.** That is not obstruction — it is the ladder working. Step 1 is "check your own existing capabilities," and the existing capabilities cover the actual work. Installing tools that cannot reach the network would enlarge the attack surface for zero measurable benefit, which Preflight §7 explicitly warns against.

## What would be worth building — later, and only on evidence

| Trigger | Build | Justification threshold |
|---|---|---|
| ≥3 assets in production | Asset/rights tracker | Only when cross-posting rights become error-prone across platforms |
| Recurring revenue across ≥2 platforms | Ledger consolidation script | Only when manual reconciliation exceeds ~30 min/week |
| Validated re-issue cadence | Source-monitoring watcher | **Requires egress access this environment does not have.** Would need an environment change first |
| Writer API justified per §19 | Writer Provider adapter | Only when human minutes at the Writer step exceed API cost |

Each is a genuine build only once the metric that justifies it is being recorded. Until then they are speculative.

## What is being built instead

A business, not an application:

```
STRATEGIC_REVIEW.md              independent assessment and corrections
docs/                            the nine Phase-0 deliverables + preflight
ledger/REVENUE_LEDGER.csv        realised economics
ledger/COST_LEDGER.csv           every cent, including $0 entries
ledger/DECISION_LOG.md           decisions, rationale, rejected alternatives, editorial memory
jobs/                            portable Writing Jobs (brief §16)
assets/                          the content assets themselves
```

This structure is deliberately **portable and provider-agnostic**. Nothing in it couples to Claude, to this container, or to any vendor. It satisfies brief §15 — a Writer Provider change requires no redesign of research, compliance, publishing, ledger or iteration logic — because none of those are code. They are documents and data.

The most valuable engineering decision available in Cycle 1 is to write no code at all.
