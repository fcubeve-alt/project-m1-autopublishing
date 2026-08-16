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

## 4. CURRENT STAGE — ACTIVE: AUDIT REMEDIATION

**Corrected 2026-08-16.** This section previously read `WAITING (justified)`. That was stale
and is now withdrawn — see "The withdrawn WAITING claim" below.

**Not waiting, not idle, not blocked.** One mission is reopened, one audit is unfinished, and
seven claims are unverified. There is more executable work than budget.

| Mission | Outcome | Type | Cost |
|---|---|---|---|
| **M-A** — Class A platforms | **🔴 REOPENED — CONCLUSION WITHDRAWN.** Audit A-001 verdict: REJECT | Negative finding **withdrawn** | $0 · ~0 Owner hrs · ~30 searches |
| **M-P** — professional compliance products | **KILLED at P-0** (stands, contamination-checked) | Market-bound (need met institutionally) | $0 · 0 Owner hrs · 2 searches · 0 words |
| **M-C** — retail marketplaces | **🔴 REOPENED — KILL WITHDRAWN.** Audit A-002 verdict: **REJECT CONCLUSION** | Claimed capability-bound; **premise false** | $0 · 0 Owner hrs · 2 searches · 0 words |
| **M-B** — audience-first | **SCREENED OUT** (stands) | Fails attention constraint | 0 searches |

### The withdrawn WAITING claim

The Idle Justification Check dated 2026-08-15 returned "all NO ⇒ WAITING is earned." **Audit
A-001 invalidated its premises**, so the check no longer supports its own conclusion. Two of
its answers were false as written:

| Check question | Then | Now |
|---|---|---|
| Decision-critical unknowns reducible without the Owner? | "No" | **Yes** — V1–V7 are all reducible by search, with no Owner input |
| Unblocked work elsewhere in the Mission? | "No — Class A closed" | **Yes** — Class A is reopened; its conclusion is withdrawn |

The remaining answers rested on the withdrawn Class A finding or on M-C's un-audited kill.
**Per R12, an Idle Justification Check may not be re-run to justify waiting while §10 items
are open.** WAITING would not be earned and must not be re-entered until A-002 reports and
V1–V7 are resolved.

### Search capability — retested 2026-08-16

The single live constraint at handoff was a session search limit, expected but not confirmed
to have reset. **Retested this session: `WebSearch` works.** Handoff §8 item 1 is discharged.
This removes the only environmental blocker on A-002 and on V1–V7.

Egress is otherwise unchanged: allowlist, `WebFetch` unusable for platform domains,
`WebSearch` with `allowed_domains` is the working research channel. **Do not re-derive this**
(R2 — it is TESTED, not inferred).

### Wake conditions — retained, but none is currently load-bearing

| # | Event | Resumes |
|---|---|---|
| **W-1** | **Owner returns Amazon first-page data** for ≥1 candidate term (`CAPABILITY_UNLOCK.md`) | M-C niche screen. **May be made moot by A-002 charge 2** — do not chase the Owner for it before A-002 reports |
| **W-2** | Owner answers **H1** | Does *not* by itself revive M-C |
| **W-3** | Owner grants a **scope change** admitting an out-of-scope family | Portfolio screening resumes |
| **W-4** | Environment gains **Amazon-domain egress** | M-C data path opens directly |
| **W-5** | **2026-11-15** — scheduled watchlist review | Superseded while M-A is reopened |
| **W-6** | Owner reports `simily.co` is live and paying | **Superseded — being verified now as V2**, no Owner time needed |

**Nothing is pending on the Owner as an obligation.** H1 blocks *publishing only* and is not
on the critical path while audit remediation is in progress.

## 5. ~~THE CENTRAL FINDING~~ — ⛔ WITHDRAWN BY AUDIT A-001

> **Everything in this section is withdrawn.** Independent audit rejected it. Retained only as a record of the error. See `audit/A-001_POSTMORTEM.md`.

### The withdrawn text follows

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
| **M-A** | Class A — platforms paying creators from their own audience | **🔴 REOPENED.** A-001 = REJECT CONCLUSION. Closeout withdrawn; Vocal, Simily, Ream, Pratilipi all live candidates again |
| **M-C** | Class C — retail publishing marketplaces | **🔴 REOPENED 2026-08-16.** A-002 = REJECT CONCLUSION. It did confuse experiment-level evidence with a mission-level conclusion — evidence reaches **L5 weakly / L4 as prior**, kill applied at **L2/L3** — and the capability premise was false besides. **Reopened ≠ attractive:** declining on economics remains available and needs none of the remediation |
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
| 12 | Treated a blocked action as a stopped system; entered WAITING while executable work was open | **R12** |
| 13 | Documented a constraint without using it as a filter | **R13** |
| 14 | Acted on a negative conclusion without independent audit — false negatives are invisible | **R14** |
| 15 | Graded evidence by row rather than by claim; ran a checklist that left no artifact | **R15** |

**Root cause of the original drift (Owner-confirmed):** *incorrect mission abstraction in cycle one* — generalising "Vocal" to "AI writing income" within the first few tool calls. **Not** a memory or context-length failure. Any future post-mortem should check abstraction before blaming context.

## 10. NEXT ACTIONS

**Rewritten 2026-08-16.** The previous version was written under the withdrawn Class A finding
and stated "M-A asks nothing further." M-A is reopened; that is no longer true.

### Done this session

1. ✅ **Search budget retested** — `WebSearch` works. The one live environmental constraint is gone.
2. ✅ **§4 corrected** from stale `WAITING` to `ACTIVE — AUDIT REMEDIATION`.
3. ✅ **V1–V7 verified** against primary sources — `audit/V1-V7_VERIFICATION.md`. Five confirmed,
   one split, one partial. **The auditor was wrong on one claim** (Tapas subscriber gate), which
   is why Charter §6.2 requires verifying auditors rather than deferring to them.
4. 🔄 **A-002 re-run commissioned** as an independent agent per Charter §2, instructed to record
   findings incrementally so a mid-run termination cannot again destroy all work.

### Also done this session

5. ✅ **A-002 complete — `REJECT CONCLUSION`.** M-C's kill withdrawn, mission reopened, closeout
   banner-marked, `audit/A-002_POSTMORTEM.md` written and **R16** added per the pre-committed
   protocol. The re-run hit the same search limit but the incremental-write instruction preserved
   331 report lines and 19 evidence rows, against zero from the first attempt.

### Open — the A-002 remediation backlog (auditor's priority order, now the mission backlog)

5a. **Withdraw the capability-bound framing** in preflight §6a — ✅ done (lines 111/113 corrected
    and banner-marked).
5b. **Verify whether the Creators API retains `SalesRank`** — PA-API was deprecated 2026-05-15. If
    the successor dropped the field, the official-BSR finding weakens to a historical one.
5c. **Cost the unblocked routes** — Google Books with a free API key (reachable today, but
    anonymous quota is zero); Keepa/Rainforest via GitHub Actions.
5d. **Verify whether Keepa's / Rainforest's own collection is Amazon-ToS-compliant.** Unverified,
    and **the strongest ground on which a rebuilt kill could stand.**
5e. **Re-derive or abandon the niche heuristics.** Not decision-grade in either direction.
5f. **Account for the seven unexamined channels** — Leanpub and Everand first, as most
    structurally different. Per R16.4, unexamined must be *recorded*, not silent.
5g. **Test GitHub Actions runner egress** — preflight grades it INFERRED; the auditor did not test
    it either.

**Do not re-close M-C on capability grounds without a route-by-route negative (R16.5).** Closing it
on **economics** remains available to the Owner at any time and needs none of the above.
6. **Resume M-A research** on the corrected economics: **Simily ($20/1k — ~5.3× Vocal)**,
   Vocal free tier ($3.80/1k), **Ream** (permits AI, never searched), **Pratilipi** (never
   searched; AI policy `UNKNOWN`), Vocal Challenges (a payment route never examined).
7. **Close the residual unknowns** in `V1-V7_VERIFICATION.md` — Simily and Pratilipi AI policies
   are the highest-value of these, since both are otherwise live candidates.
8. **Do not reinstate the withdrawn Class A finding**, in whole or in part. If Class A closes
   again it closes on new evidence with an evidenced R15b checklist attached.

### Owner

9. **H1 is no longer a class-wide gate.** Verification showed payout rails are platform-specific
   — Vocal is Stripe-only, but Simily uses Tipalti, Listverse pays via PayPal **or Bitcoin**.
   H1 blocks *publishing on specific platforms*, not the mission, and is **off the critical path**
   while audit remediation runs. Nothing is owed by the Owner right now.
10. **W-1 (Amazon first-page data) must not be chased** before A-002 reports — its second charge
    may establish a compliant data route that makes the request moot.

**Standing rule:** no production until the counterfactual test is re-run at the commitment point (R7).

## 11. KEY FILES

| File | Contains |
|---|---|
| `PROJECT_STATE.md` | **This file — start here** |
| `SESSION_HANDOFF.md` | Operational delta since this file's last update — read second |
| `OPERATING_RULES.md` | **R1–R15** decision rules (R15 binding on every closeout) |
| `audit/AUDIT_CHARTER.md` | Auditor function, four verdicts, pre-committed responses, L1–L5 discipline |
| `audit/A-001_POSTMORTEM.md` | What failed in M-A, verified vs pending, contamination table |
| `audit/A-002_HYPOTHESIS_LEVELS.md` | Brief for the M-C audit |
| `audit/A-002_AUDIT_REPORT.md` · `A-002_EVIDENCE_MATRIX.csv` | A-002 output (in progress) |
| `audit/V1-V7_VERIFICATION.md` | **Primary-source verification of the auditor's own claims** |
| `audit/M-A_AUDIT_REPORT.md` · `M-A_AUDIT_MATRIX.csv` | A-001 output — external claims now verified in V1–V7 |
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
