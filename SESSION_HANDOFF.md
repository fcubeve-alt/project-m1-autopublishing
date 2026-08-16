# SESSION_HANDOFF

**Purpose:** the single file a new session reads first. It states what is true in this
repository right now, what is done, what is in progress, and what the next session must do.

**Last updated:** 2026-08-16 (Session S-002)
**Branch:** `claude/session-handoff-reconstruction-dl6gwa`

---

## 0. Provenance warning — read this before trusting any earlier claim

This file was **created in Session S-002**. It did not exist before.

Session S-002 was asked to "read SESSION_HANDOFF.md, reconstruct state, and resume from the
last valid checkpoint after task A-002 was interrupted." No such state existed:

| Checked | Result |
|---|---|
| `SESSION_HANDOFF.md` in working tree | absent |
| Any state / operating-rule file, any commit, any branch | absent |
| `git log --all`, reflog, stashes, dangling objects | one commit only: `61a2b44` "Add files via upload" |
| Files ever added in repo history | the two `.docx` specs, nothing else |
| GitHub issues / pull requests | zero of each |

**There was no prior checkpoint, and no task `A-002` record.** Whatever a previous session
did was never committed and is unrecoverable. Task IDs in this repo are therefore
**established by S-002**, not recovered. Do not treat `A-002` as having prior partial output.

---

## 1. What this project is

Two `.docx` specifications were uploaded and are the governing authority:

- `M1_Autonomous_Publishing_Business_Experiment_v1.1.docx` — the business mission: build a
  low-cost autonomous publishing business that earns **real, attributable external revenue**.
- `Project_M_AI_Development_Environment_Preflight_Skills_Spec_v1.1.docx` — the capability
  policy: research before coding, no blind tool installation, produce a preflight report.

Binding rules extracted from both are in [`OPERATING_RULES.md`](OPERATING_RULES.md).
Read that file second. The two hardest rules:

1. **Do not start by coding.** Phase 0 is research and feasibility.
2. **Unknown must be written `UNKNOWN` and researched.** Never fill a gap from model memory.

---

## 2. Environment capability (verified this session, not assumed)

| Capability | Status | Evidence |
|---|---|---|
| **Web Search** | ✅ **WORKS** | live queries returned current Aug-2026 results |
| **WebFetch — general web** | ❌ **BLOCKED** | `EGRESS_BLOCKED` on vocal.media, help.medium.com, royalroad.com, substack.com |
| **WebFetch — developer domains** | ✅ works | github.com fetched successfully |
| **curl — general web** | ❌ blocked | `CONNECT tunnel failed, response 403` |
| Git / GitHub MCP | ✅ works | branch pushed; issues & PRs readable |

**This is the single most important constraint on the project.** The mission spec requires
verifying *current official platform rules from official sources*. This environment can reach
a search engine but **cannot open the platforms' own policy pages.** All research below is
therefore search-snippet evidence, not official-source evidence.

Per the Capability Ladder ("access failure is not research failure"), this is escalated as
**HG-01** in §5 rather than treated as a dead end.

---

## 3. Task ledger — current state

Full detail in [`STATE/TASK_LEDGER.md`](STATE/TASK_LEDGER.md).

| ID | Task | Status |
|---|---|---|
| A-001 | Reconstruct session state; establish state layer | ✅ DONE (S-002) |
| A-002 | Verify research capability in this environment | ✅ DONE (S-002) — search works, official-source fetch does not |
| A-003 | Environment preflight report (Preflight spec §2) | ✅ DONE (S-002) — `DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` |
| A-004 | `PLATFORM_LONG_LIST.md` ≥30 candidates | 🟡 **PARTIAL** — 35 candidates listed, evidence tier T2–T5, no T1 |
| A-005 | `PLATFORM_RULES_MATRIX.csv` | 🟡 PARTIAL — schema complete, mostly `UNKNOWN` pending T1 |
| A-006 | `PLATFORM_TOP5.md` | ⛔ **BLOCKED** by HG-01 — selecting a Top 5 on T3/T4 evidence would violate the spec |
| A-007 | `CONTENT_INTELLIGENCE_REPORT.md` | ⛔ blocked — depends on A-006 |
| A-008 | `PAYMENT_FEASIBILITY.md` | ⛔ **BLOCKED** by HG-02 — Owner's lawful payment options unknown |
| A-009 | `COMPLIANCE_POLICY.md` | 🟡 partial input gathered (AI-policy findings, §4) |
| A-010 | `EXPERIMENT_PLAN_30D.md` | ⛔ blocked — depends on A-006/A-008 |
| A-011 | `HUMAN_GATES.md` | 🟡 two gates identified, see §5 |
| A-012 | `BUILD_VS_NO_BUILD.md` | ⛔ blocked — depends on A-006 |

**Nothing has been built. No code exists. That is correct per spec §1 and §12.**

---

## 4. Most decision-relevant findings so far

These change the shape of the business and should be read before any planning.

1. **AI-content policy is the dominant selection variable, not audience size or payout rate.**
   An AI-native publishing business is disqualified or throttled on several of the largest
   platforms regardless of quality.
2. **Medium bars AI-generated content from the Partner Program** — it cannot be paywalled, is
   ineligible for Boost, and non-compliance can mean removal from the program. Disclosed AI
   writing gets limited distribution. Medium is likely **not** a Phase-1 revenue platform.
3. **Two platforms that 2026 "best writing sites" listicles still recommend are dead:**
   Kindle Vella (closed Feb 2025) and Radish Fiction (shut down Dec 2025). This is direct
   confirmation that the spec's "do not rely on old top-lists" rule is load-bearing.
4. **Platform AI stances diverge sharply** — Wattpad and Tapas restrictive, Inkitt
   disclosure-label based, Webnovel actively shipping AI writing tools (Feb 2026). Stance,
   not popularity, should drive selection.
5. **Monetization is Stripe-gated on most Western platforms** (Substack ~10% + Stripe fees;
   Vocal pays via Stripe). Country eligibility is therefore a gating input, and it is unknown
   — see HG-02.

Source-quality caution: one search result asserted a "Wattpad Trust & Safety internal memo,
March 2024." An internal memo is not a public source; that claim is **treated as
unverified and must not be repeated** as fact. Several results were SEO/AI-generated
aggregator pages (tier T4).

---

## 5. Human gates — Owner action required

| ID | Gate | Why it blocks | What is needed |
|---|---|---|---|
| **HG-01** | Official-source web access | Spec demands current official rules; environment blocks platform domains | Either (a) widen the environment's network policy to allow target platform domains, or (b) approve a research capability with its own fetch path (the Preflight spec §3.4 proposes Firecrawl for exactly this gap), or (c) accept T2/T3 evidence with the risk recorded |
| **HG-02** | Owner's lawful payment/account options | Payout feasibility gates platform ranking; spec forbids nationality guesswork | Owner states which payout rails are lawfully available to them (e.g. Stripe-eligible country, PayPal, Payoneer, bank) — **do not infer this from timezone, email, or any other signal** |

Both are irreducible Owner decisions under the Capability Ladder step 7.

---

## 6. Next session: start here

1. Read `OPERATING_RULES.md`, then `STATE/TASK_LEDGER.md`.
2. Check whether HG-01/HG-02 have been answered. If HG-01 is resolved, resume **A-004** by
   promoting candidates to tier T1 with official sources; that unblocks A-005 → A-006.
3. If HG-01 is still open, do **not** produce `PLATFORM_TOP5.md` from search snippets.
   Continue widening the candidate pool and recording evidence instead.
4. **Update this file and the ledger before the session ends, and commit.** The failure that
   caused S-002 to start blind was uncommitted state.
