# PROJECT STATE — Single Source of Truth

> **If you are a fresh agent or session: read this file first and completely.**
> It is designed so the project can be reconstructed without the Owner re-explaining anything.
> Last updated: **2026-08-15** · Update this file at the end of every working session.

---

## 1. MISSION (fixed — only the Owner may change this)

Build and validate a lawful, compliant, sustainable AI-powered **publishing** business that generates real external revenue, then continuously improve realized net profitability and degree of autonomous operation.

## 2. MISSION SCOPE (a hard boundary — do not widen it)

**The economic model, stated precisely:**

> AI produces English articles, stories, fiction or other written content → published on **third-party platforms that already have readers/distribution** → earns through **reads, creator revenue sharing, publication payments, contests, royalties, tips, or closely related content-based compensation**.

**Vocal Media was a seed *example* of this model, not a predetermined winner.** The reason to look beyond Vocal was its payout/account constraints — the task became finding platforms implementing the *same or closely related* economic model.

### Monetisation classes (use these labels in every analysis)

| Class | Definition | In scope? |
|---|---|---|
| **A** | Platform **directly compensates** creators for reads/content/royalties/contests/tips **using its own existing audience** | ✅ **Core of the mission** |
| **B** | **Audience-acquisition** platform — does not itself pay; monetisation happens elsewhere | ⚠️ In scope only as an **acquisition/learning** step, never counted as an income experiment |
| **C** | **Retail publishing marketplace** — sells the work to buyers, pays royalties | ✅ In scope (royalties are named in the model) |
| **OUT** | Freelance services, generic templates, micro-SaaS, professional tooling, any non-written-content product | ❌ Record in `docs/OUT_OF_SCOPE_REGISTER.md`, zero research budget |

**Never let "easy to start" substitute for "fits the economic model."**

## 3. HARD CONSTRAINTS

| Constraint | Value |
|---|---|
| Budget | ~$0. Standing spend authority **$10**; anything above requires Owner approval |
| Owner attention | ~2–3 hours per 30 days |
| Audience | **None.** Cannot buy traffic |
| Country of tax residence | **`UNKNOWN`** — blocks payout design (Human Gate H1) |
| Environment | Egress **allowlist**: GitHub + package registries reachable; general web blocked. `WebSearch` (with `allowed_domains`) is the working research channel |
| Marketplace data | Unobtainable (Amazon BSR/keywords). Scraping barred by our own compliance policy |
| Compliance | No fake identity, no CAPTCHA bypass, no deceptive AI disclosure, no policy evasion. Platforms that forbid what we are get **excluded, not worked around** |

## 4. CURRENT STAGE

**Stage 3.5 — Shortlist complete; Stage 6 experiment selection under revision after a scope-integrity check.**

Stages: Discovery ✅ → Screening ✅ → Shortlist ✅ → Content-Market Research ✅ (partial) → Platform × Content Matrix ✅ → **Experiment Selection (being corrected)** → Production/Test ⏸ → SCALE/HOLD/KILL.

**No production is authorised right now.** A0001 is HOLD, A0002 is PAUSED/out-of-scope, JOB-0003 is not issued.

## 5. THE CENTRAL FINDING (this is the most important thing in the file)

**Class A — the exact model this experiment exists to test — is close to systematically closed to disclosed AI-generated content in 2026.**

| Class A platform | Position | Grade |
|---|---|---|
| Medium | AI writing cannot be paywalled, disclosed or not | **[P]** |
| **AlphaNovel** | *"Using AI to generate or write a book is not allowed… will be rejected for a contract."* Only spelling/grammar AI permitted | **[P]** |
| Wattpad | Does **not monetise** AI content — text, covers or illustrations | **[P]** |
| Publish0x | *"AI generated content may be removed"* | **[P]** |
| Reedsy contests | *"Use of generative AI… is not permitted"* | **[P]** |
| beehiiv | Entirely-AI publications without meaningful human input not permitted | **[P]** |
| Literary magazines | Refuse AI **and AI-assisted** | **[P]** |
| HubPages / Quora Partner / Kindle Vella | Dead or closed | **[R]/[P]** |
| **Vocal Media** | **OPEN** with mandatory tagging — but read earnings are Vocal+ only ($9.99/mo), ~16,700 reads/mo to net $100, and **publication is hard-blocked without Stripe** | **[P]** |
| Tapas | OPEN with mandatory tag (from Mar 2026) — but 1,000-subscriber gate before premium | **[R]** |
| Simily | AI policy `[U]`; reported ~$0.02/view; **also reported as declining** — verify liveness before any investment | **[U]** |
| AnyStories / GoodNovel / Bravonovel / NovelCat / Stary cluster | AI policy `[U]`; exclusive digital rights typical; **Writer Beware "Bad Contract Alert"** on Stary/Dreame; GoodNovel reportedly claims rights to all future work | **[R]** |
| Listverse | $100/list flat; no explicit AI rule but originality clause likely covers it | **[U]** |
| NewsBreak | 200 followers + 10 articles to apply; reach degraded | **[R]** |

**Interpretation:** platforms that pay creators directly out of their own audience have, by 2026, largely barred or de-monetised substantially-AI-generated work. Where they permit it, the tag is never free (Vocal's paywall, Tapas's subscriber gate). **Class C (retail royalties) is the systematic exception**, because the buyer decides on the product rather than on a badge.

**This is a finding, not a research failure — and it is the answer the experiment was built to produce.**

## 6. OPPORTUNITY PORTFOLIO

`DISCOVERED → SCREENING → VALIDATING → EXPERIMENT → SCALE / HOLD / KILL`

| ID | Candidate | Class | State |
|---|---|---|---|
| P-KDP | Amazon KDP wide/non-exclusive | **C** | **VALIDATING** — primary income candidate |
| P-RR | Royal Road serial | **B** | **ACQUISITION PROBE** — pays nothing; not an income experiment |
| P-VOC | Vocal Media | **A** | HOLD — only verified-open Class A; economics fail at our scale; Stripe hard-block |
| P-TAP | Tapas | **A** | SCREENING — open with tag; 1,000-sub gate |
| P-SIM | Simily | **A** | SCREENING — best reported rate; liveness and AI policy both `[U]` |
| P-D2D | Draft2Digital wide retail | **C** | HOLD — $20 + $12/yr; gated on an asset proving itself |
| P-SUB | Substack | B/infra | HOLD — no cold-start distribution |
| A0001 | AI-disclosure handbook | C | **HOLD** — failed counterfactual test |
| A0002 | AB 723 workbook | OUT | **PAUSED** — out of scope, in register O4 |

## 7. HUMAN GATES

| ID | Gate | Status |
|---|---|---|
| **H1** | **Country of tax residence** + existing KDP account? + payout rails (bank/PayPal/Stripe) | 🔴 **OPEN — blocking, on the critical path.** Product-independent. Up to **7 weeks** if a US TIN is needed |
| H2 | Editorial approval before publishing substantive content | Pending an asset |
| H3 | Upload/publish (no KDP API for individuals) | Pending |
| H4 | Sales reporting (dashboard unreachable from here) | Pending |
| — | Spend above **$10** | Requires approval |

## 8. DECISIONS (full reasoning in `ledger/DECISION_LOG.md`)

D0001 per-read category deprioritised · D0002 Vocal `UNKNOWN` (later corrected) · D0003 KDP wide, no Select · D0004 recency over volume · D0005 A0001 chosen · D0006 build no software · D0007 M1-A/M1-B split · D0008 three trade-press errors corrected · D0009 length held, price cut · D0010 Reviewer round 1 · D0011 A0001 demoted on counterfactual test · D0012 scope drift corrected, A0002 paused · **D0013 monetisation-class integrity check (this update)**

## 9. FAILURES AND LESSONS (see `OPERATING_RULES.md`)

| # | Failure | Rule |
|---|---|---|
| 1 | Treated `UNKNOWN` as a negative verdict (Vocal) | **R1** |
| 2 | Inferred network limits instead of testing | **R2** |
| 3 | Committed without comparing alternatives | **R3** |
| 4 | Confused *need* with *purchase intent* | **R4** |
| 5 | Stated legal interpretation as fact | **R5** |
| 6 | Reported assumed work as validated | **R6** |
| 7 | Let a project become the Mission | **R7** |
| 8 | Widened the scope boundary and called it rigour | **R8** |
| 9 | **Let "easy to start" substitute for "fits the model"** | **R9** |

**Root cause of the original drift (Owner-confirmed):** *incorrect mission abstraction in cycle one* — generalising "Vocal" to "AI writing income" within the first few tool calls. **Not** a memory or context-length failure. Any future post-mortem should check abstraction before blaming context.

## 10. NEXT ACTIONS

1. **Owner:** answer **H1**. Nothing else is required from the Owner right now.
2. **Owner decision proposed, not enacted:** `docs/SCOPE_INTEGRITY_CHECK.md` §4 — with Class A now conclusively mapped as near-closed, does this experiment conclude on that finding, or continue via Class C?
3. **Agent:** re-run the counterfactual test on E2 before any production. It is genre-corrected but **not authorised** — see the open tension below.

### Class A residue — RESOLVED 2026-08-15

| Candidate | Resolution |
|---|---|
| **AnyStories / NovelSnack / Readink** | **OUT of scope** — work-for-hire ghostwriting: writers take a supplied outline, 10 chapters × 1,500 words/week at $40/chapter. Selling labour, not publishing own content. Writer Beware "Bad Contract Alert" covers all three as one group **[R]** |
| **Simily** | **`[U]` — unverifiable from here.** Only signal is a 2023 report of profile and earnings pages returning 404. Held open per R1 (`UNKNOWN` is never evidence against), not invested in. **A 30-second check the Owner could do**: is simily.co live and paying? |
| GoodNovel / Bravonovel / NovelCat / Stary | AI policy `[U]`; exclusive digital rights typical; Writer Beware alert. Not pursued on contract risk alone |
| Listverse · NewsBreak | `[U]`, low ceiling, not ranking-relevant |

**Conclusion: no viable open Class A venue exists for us.** Vocal is open but economically unviable and Stripe-gated; Tapas is open but audience-gated.

### Open tension on E2 (must be resolved before production)

Stage 4 genre research corrected E2 from a 65–100pp Short Read to a genre-correct **60–80k word** cozy mystery — a Short Read would have violated the form's central reader expectation. But the correction does not fix the economics:

- **~80% of authors with 1–3 books earn under $100/month**; catalogue size is the strongest income predictor.
- Cozy mystery runs on **series read-through**, which a single title cannot produce.
- So E2 has **low expected revenue** and **high expected information value** (does disclosed-AI fiction achieve organic discovery where the AI policy is neutral?), at **substantially higher production cost** than the version it replaced.

Under R4, an information-value justification is only legitimate when the revenue expectation is stated honestly. It now is. Under R7, the raised cost demands a fresh counterfactual test at the commitment point — which has **not** been run and is the gate on production.

## 11. KEY FILES

| File | Contains |
|---|---|
| `PROJECT_STATE.md` | **This file — start here** |
| `OPERATING_RULES.md` | R1–R9 decision rules |
| `ledger/DECISION_LOG.md` | Every decision, reasoning, rejected alternatives |
| `docs/SCOPE_INTEGRITY_CHECK.md` | A/B/C classification; proposed scope decision |
| `docs/PLATFORM_LANDSCAPE_V2.md` | 38 screened candidates, shortlist |
| `docs/PLATFORM_CONTENT_MATRIX.md` | Stages 4–6 |
| `docs/OUT_OF_SCOPE_REGISTER.md` | Parked findings (incl. A0002) |
| `docs/MODEL_ROUTER_DESIGN.md` | Dynamic model routing architecture |
| `ledger/REVENUE_LEDGER.csv` · `COST_LEDGER.csv` | Economics. **Revenue $0.00 · Spend $0.00** |

## 12. STATE MANAGEMENT PROTOCOL

- **This file is the reconstruction point.** Update it at the end of every session, before context is at risk.
- Git history is the checkpoint mechanism — every meaningful change is committed with reasoning in the message.
- **No secrets in this repository, ever.**
- **Chosen architecture: structured repository files + git.** A memory MCP was evaluated and **rejected as a duplicate** — the repo is already project-scoped, searchable, exportable, diffable, survives session/model/agent changes, and is readable by a human without tooling. A second store would split the source of truth. Re-evaluate only if state grows beyond what plain files can serve.
