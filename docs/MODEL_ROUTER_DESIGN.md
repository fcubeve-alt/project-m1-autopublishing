# DYNAMIC MODEL ROUTER — Design

**Date:** 2026-08-15 · **Status:** design recorded for later Money OS integration. **Nothing built.**
**Rationale for not building now:** `BUILD_VS_NO_BUILD.md` and the Automation Upgrade Gate — the money loop is unproven, so routing infrastructure would optimise a workload that does not yet exist.

**Explicitly not a diagnosis.** The mission-abstraction failure in cycle one happened on a high-capability model. Routing would not have prevented it, and this document must not be read as implying otherwise. Routing is a **cost** mechanism, not a **correctness** mechanism.

---

## 1. What is actually possible in the present environment

| Capability | Available here? | Basis |
|---|---|---|
| Per-task model selection inside one Claude Code session | **No** | Session runs one configured model |
| Spawning subagents with a different model | **Partially** | The Agent tool accepts a `model` override — a real routing primitive, though coarse |
| Programmatic per-call routing | **No** | Requires API orchestration; this session has no Anthropic API entitlement (brief §14 forbids making it a dependency) |
| Cost/latency telemetry per call | **No** | Not exposed in-session |
| Cross-session routing memory | **Yes, crudely** | Repository files (this project already uses git as durable state) |

**Conclusion:** a genuine adaptive router requires **API-based orchestration** outside Claude Code. Within Claude Code, the only available primitive is subagent model override, which is worth using deliberately but is not a router.

---

## 2. Routing signals — adaptive, not a task-name table

A fixed "task → model" lookup fails because task labels do not carry difficulty. Route on **observable signals** instead:

| Signal | Meaning | Direction |
|---|---|---|
| **Reversibility** | Can a wrong answer be cheaply undone? | Irreversible → escalate |
| **Evidence conflict** | Do sources disagree? | Conflict → escalate |
| **Economic stake** | Does this commit money, time or the Owner's attention? | Stake → escalate |
| **Failure history** | Has a cheaper model already failed this class of task? | Escalate, and remember |
| **Output determinism** | Is there one correct answer checkable by rule? | Deterministic → cheapen |
| **Context depth** | Does it require holding the whole project? | Deep → escalate |
| **Volume** | Is this repeated many times? | High volume → cheapen |

## 3. Tiers

| Tier | Workload | Examples from *this* project |
|---|---|---|
| **Cheap** | Deterministic, verifiable, repetitive | CSV row formatting, extracting fields from a fetched page, date normalisation, link checking, ledger arithmetic |
| **General** | Ordinary research, drafting, coding | Platform screening searches, manuscript drafting, routine doc updates |
| **Frontier** | Architecture, conflicting evidence, economics, high-stakes review | **Every failure this project has had lives here**: mission abstraction, scope boundaries, the counterfactual test, legal-tier separation, Reviewer response |

**The observed pattern is instructive:** every serious error in this project was a *judgement* error at the frontier tier, not an execution error at the cheap tier. That argues for spending frontier capability on **framing and boundary decisions** and pushing execution downward — not the reverse.

## 4. Escalation and de-escalation

```
Task → classify by signals → route to tier
  ├─ output fails validation, or the model self-reports low confidence
  │     → escalate one tier, record the failure against that task class
  ├─ two failures at a tier for the same class
  │     → permanently raise that class's floor
  └─ frontier tier produces a plan with repetitive execution
        → hand execution back down, keep review at frontier
```

Both directions matter. A router that only escalates becomes an expensive router.

## 5. Guardrails

- **Never route by cost alone.** A cheap model on an irreversible decision is the most expensive possible saving.
- **These always run at frontier tier**, regardless of apparent simplicity: scope-boundary decisions · counterfactual tests · legal or compliance interpretation · anything touching money, identity or publication · Reviewer-challenge responses.
- **Log routing decisions** with the signals that produced them, so the policy can be audited against outcomes rather than assumed correct.
- **Cheap tiers must not silently degrade evidence standards.** `[Official]` / `[Reported]` / `[Unknown]` / `[Interpretation]` grading is mandatory at every tier.

## 6. Proposed measurement

Route quality is judged on **outcomes, not token savings**:

| Metric | Why |
|---|---|
| Escalation rate per task class | Reveals mis-set floors |
| Rework rate after cheap-tier output | The real cost of under-routing |
| Cost per *completed, accepted* deliverable | Not cost per call |
| High-stakes decisions made at correct tier | The metric that actually matters |

## 7. Recommendation

1. **Now:** build nothing. Use the Agent tool's `model` override deliberately for bulk extraction work if such work appears. Keep all judgement in-session at frontier tier.
2. **On first revenue:** revisit. If throughput becomes the constraint, an API-orchestrated router becomes justifiable under the Automation Upgrade Gate.
3. **For Money OS:** implement behind an adapter so the routing policy can be replaced without touching business logic — the same boundary discipline the brief requires of the Writer Provider (§15).
