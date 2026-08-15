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

## 4. CURRENT STAGE — WAITING (justified)

**Three missions concluded 2026-08-15. In-scope opportunity space is exhausted pending one capability input.**

| Mission | Outcome | Type | Cost |
|---|---|---|---|
| **M-A** — Class A platforms | **⚠️ PENDING INDEPENDENT AUDIT** (was CONCLUDED — negative) | Market-bound *(claim under audit)* | $0 · ~0 Owner hrs · ~30 searches |
| **M-P** — professional compliance products | **KILLED at P-0** | Market-bound (need met institutionally) | $0 · 0 Owner hrs · 2 searches · 0 words |
| **M-C** — retail marketplaces | **⚠️ PROVISIONAL KILL — PENDING INDEPENDENT AUDIT** | Claimed capability-bound *(under audit)* | $0 · 0 Owner hrs · 2 searches · 0 words |
| **M-B** — audience-first | **SCREENED OUT** | Fails attention constraint | 0 searches |

**Critically: M-C's kill saved the Owner the H1 gate.** Falsifying it from the desk cost 2 searches; running C-0 would have cost up to 7 weeks of tax setup plus an upload to observe a predictable outcome.

### Idle Justification Check — run 2026-08-15, result: **WAITING is correct**

| Question | Answer |
|---|---|
| Decision-critical unknowns reducible without the Owner? | **No** — the binding unknown is Amazon first-page data, verified unobtainable here |
| Authorised candidates screenable cheaply? | **No** — M-B screened out today; M-S/M-T are out of scope and parked |
| Any active hypothesis falsifiable cheaply? | **No** — all three in-scope hypotheses now resolved |
| Unblocked work elsewhere in the Mission? | **No** — Class A closed, Class B not income, Class C capability-blocked |
| Out-of-scope opportunity to screen at portfolio level? | **No** — recorded; promoting one requires an Owner scope decision |
| Capability bottleneck with reusable value? | **Was YES → now resolved.** `missions/CAPABILITY_UNLOCK.md` written |
| Scheduled watchlist/maintenance due? | **No** — next review 2026-11-15 |
| Further work EV > compute cost? | **No** — remaining work would be busywork |

**All NO ⇒ WAITING is earned, not defaulted.**

### Wake conditions — the exact events that resume autonomous operation

| # | Event | Resumes |
|---|---|---|
| **W-1** | **Owner returns Amazon first-page data** for ≥1 candidate term (`CAPABILITY_UNLOCK.md`) | M-C reopens with a screened niche; H1 becomes worth answering |
| **W-2** | Owner answers **H1** | Does *not* by itself revive M-C — the niche-selection gap is the binding constraint, not payout |
| **W-3** | Owner grants a **scope change** admitting an out-of-scope family (services, templates) | Portfolio screening resumes |
| **W-4** | Environment gains **Amazon-domain egress** | M-C reopens immediately, no Owner time needed |
| **W-5** | **2026-11-15** — scheduled watchlist review | ≤3 searches on Class A residue |
| **W-6** | Owner reports `simily.co` is live and paying | Watchlist W3 resolves; may reopen a Class A candidate |

**Nothing is pending on the Owner as an obligation.** W-1 is an offer, not a request — declining is reasonable and costs nothing already spent.

## 5. THE CENTRAL FINDING — M-A's delivered answer *(⚠️ UNDER AUDIT — see `audit/`)*

**Class A — the exact model this experiment existed to test — is systematically closed to disclosed AI-generated content in 2026.** Seven platforms verified closed, three dead, exactly two verified open (both defeated by our constraints), residue out-of-scope or unverifiable.

**Mission cost: $0.00 cash · ~0 Owner hours · ~30 searches · no software · no irreversible commitments.**

**Why it is structural, not fashion:** platforms paying creators from their own audience bear the cost of every marginal item, so zero-marginal-cost supply threatens them existentially and they barred it. Retail marketplaces bear no such cost — the buyer pays per copy — which is why that class stayed open. **Economics predicted policy.** The finding reverses only if *who bears marginal cost* changes, not if sentiment does.

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

## 6. MISSION PORTFOLIO

| ID | Family | Status |
|---|---|---|
| **M-A** | Class A — platforms paying creators from their own audience | **⚠️ PENDING INDEPENDENT AUDIT** — conclusion not treated as settled until a verdict is issued |
| **M-C** | Class C — retail publishing marketplaces | **⚠️ PROVISIONAL KILL — PENDING INDEPENDENT AUDIT (A-002).** Kill not treated as settled; may have confused experiment-level evidence with mission-level conclusion |
| **M-P** | Professional / compliance information products | **KILLED at P-0, 2026-08-15** — 2 searches, 0 words. Need met institutionally |
| **M-S** | AI-assisted services (freelance) | CANDIDATE — strongest buyer intent, fails autonomy |
| **M-T** | Functional templates/tools | CANDIDATE — no distribution |
| **M-B** | Audience-first | **SCREENED OUT 2026-08-15** — requires sustained human community engagement (Royal Road mandates human comments/PMs); fails the 2–3h/month attention constraint |

**Class A residue → `missions/WATCHLIST.md`** (Vocal, Tapas, Simily, GoodNovel cluster). Quarterly, ≤3 searches, next review **2026-11-15**.

**Assets preserved as free inputs, not as reasons to continue:** A0001 (~9,000-word handbook, cover, full package) · A0002 research (AB 723) · platform matrix · compliance policy.

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
| 9 | Let "easy to start" substitute for "fits the model" | **R9** |
| 10 | Nearly stretched a mission into a new family rather than concluding it | **R10** |
| 11 | **Assumed a professional need with budget implied a market** | **R11** |

**Root cause of the original drift (Owner-confirmed):** *incorrect mission abstraction in cycle one* — generalising "Vocal" to "AI writing income" within the first few tool calls. **Not** a memory or context-length failure. Any future post-mortem should check abstraction before blaming context.

## 10. NEXT ACTIONS

**M-A asks nothing further.** The mission is closed and requires no Owner action.

**P-0 ran and killed M-P** for 2 searches and 0 words. **M-C is now chartered** per the pre-committed trigger.

1. **Owner — H1 is now the binding gate on everything.** Country of tax residence, existing KDP account, payout rails. M-C cannot test its central question (organic discovery) without publishing, and cannot publish without H1. Up to 7 weeks if a US TIN is needed.
2. **Agent — done:** `missions/M-C_EXPERIMENT_DESIGN.md` proposes testing M-C's core question (C-0, organic discovery) with a **$0 marginal-cost probe** — listing the existing A0001 — rather than committing a 60–80k novel to learn something about metadata. Strong kill signal, weak go signal, which is the right shape for a first test.
3. **Agent — deliberately NOT doing:** genre/format selection for a future M-C novel. That work would be performed on an experiment C-0 may kill. Deferred until C-0 returns.
4. **Agent:** re-run the counterfactual test if C-0 passes. M-C won the charter by default when M-P's trigger fired; winning by default is not justification.
5. **Owner — H2 question when it arrives:** C-0 proposes listing A0001, which is explicitly *not* our strongest product. Declining is legitimate; the probe then costs more but its logic is unchanged.
6. **Optional 30-second Owner check:** is `simily.co` live and paying? Unverifiable from here (watchlist W3).

**Standing rule:** no production until the counterfactual test is re-run at the commitment point (R7).

## 11. KEY FILES

| File | Contains |
|---|---|
| `PROJECT_STATE.md` | **This file — start here** |
| `OPERATING_RULES.md` | R1–R9 decision rules |
| `ledger/DECISION_LOG.md` | Every decision, reasoning, rejected alternatives |
| `missions/M-A_CLOSEOUT.md` | **Concluded mission — the negative finding and its evidence** |
| `missions/M1_OPPORTUNITY_FAMILIES.md` | **Family comparison — where capital goes next** |
| `missions/M-C_CHARTER.md` | Class C candidate charter (not chartered) |
| `missions/WATCHLIST.md` | Class A residue, quarterly, ≤3 searches |
| `docs/SCOPE_INTEGRITY_CHECK.md` | A/B/C classification; scope decision |
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
