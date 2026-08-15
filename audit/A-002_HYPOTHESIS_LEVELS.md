# A-002 — Hypothesis Level Framework for the M-C Audit

**Date:** 2026-08-15 · **Purpose:** define the levels the auditor must separate, so that evidence is matched to the claim it can actually reach.

---

## The problem this framework exists to catch

A negative result at a narrow level can silently propagate upward until it reads as a verdict on the whole enterprise. Each level has a **different remedy**, so mis-attributing a falsification does not merely mislabel the finding — it discards the remedies that would have worked.

## The five levels

| # | Level | The claim | If falsified, the remedy is… |
|---|---|---|---|
| **L1** | **Market** | A market exists for AI-written books sold through retail marketplaces — buyers exist and buy | Abandon. Nothing downstream can fix an absent market |
| **L2** | **Mission** | AI-written content can earn via third-party retail publishing platforms (royalties) — the Mission-scope claim | Mission scope must change. Owner decision |
| **L3** | **Channel** | **Amazon KDP specifically** is a viable channel for *us* | Change channel — Kobo, Apple, Google Play, D2D, Leanpub, Everand |
| **L4** | **Strategy** | **Organic discovery with zero promotion** is a viable discovery strategy | Change strategy — cross-promotion, series read-through, list-building, cheap paid ads, category selection, launch tactics |
| **L5** | **Experiment** | **One unknown author, one new title, zero promotion, organic-only** will achieve non-trivial impressions | Change the experiment — more titles, a series, a different category, a launch plan |

## What the Business Brain actually did — the specific charge to test

The evidence gathered was:

> "A brand new book with zero reviews gets almost no organic visibility… the algorithm rewards momentum, not existence." **[Secondary]**

**That is an L5 observation.** It describes precisely one configuration: single new title, no reviews, no promotion, organic surface only.

**The kill was applied at L2/L3** — M-C, the retail-marketplace mission, was recorded as dead.

**The auditor must determine whether that propagation is independently supported**, or whether the evidence only ever reached L5 (and possibly L4).

The counter-consideration the auditor must weigh: L4 and L5 are exactly the levels where **remedies are abundant and cheap** — series structure, category choice, launch sequencing, cross-promotion, list-building. If the falsification stops at L4/L5, then M-C is not dead; **only one naive execution of it is dead**, and the correct output is a changed experiment, not a closed mission.

## The second charge — the capability claim

The Brain asserted:

> "Live marketplace data (BSR, review counts, keyword volume) cannot be obtained through any compliant autonomous route from this environment."

This claim did the decisive work — it converted "we lack data" into "we cannot proceed." It rests on two sub-claims that must be tested **separately**:

| Sub-claim | Status |
|---|---|
| (a) Amazon domains are unreachable from this container | **Tested and true** — `curl` returned 000 |
| (b) Therefore **no compliant route exists** | **NOT tested.** Asserted |

**(b) does not follow from (a)**, and the Brain's own records contain a contradiction: `DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md` §6a records **GitHub Actions as an AVAILABLE remote execution path with full internet access** — then dismisses it on the grounds that the needed data is "barred by platform terms, not by network reach." That dismissal conflates *scraping is barred* with *no compliant route exists*.

**Routes the auditor must check before (b) can stand:**

- **Amazon Product Advertising API** — official, ToS-governed. What does it expose (SalesRank? review counts?), and what are its eligibility requirements?
- **Amazon Associates / affiliate data access**
- **Third-party data APIs** — Keepa, Rainforest, Bookstat, Publisher Rocket and similar. Cost, ToS, and whether output can be brought into an autonomous workflow
- **Google Books API** and public bibliographic sources (ISBNdb, OpenLibrary, WorldCat)
- **Published public bestseller lists** and category rankings
- **GitHub Actions or other remote execution** running a *compliant* API client — not a scraper
- **Whether KDP itself surfaces category/competition data** to account holders once H1 is cleared

**If any compliant route exists, the capability-bound kill collapses**, and M-C returns to a live mission with a data-acquisition task rather than a dead one.

## The third charge — the discovery rules themselves

These were taken from **secondary practitioner sources** and used as decision-grade thresholds. The auditor must independently verify, or downgrade:

| Claim | Grade as used | Must verify |
|---|---|---|
| First page averaging **under ~100 ratings** ⇒ winnable niche | Secondary | Is this a real heuristic with evidence, or blog folklore? |
| Most recent first-page publish date **2+ years old** ⇒ demand without active publishers | Secondary | Same |
| New titles get "almost no organic visibility" without sales/reviews | Secondary | Does Amazon in fact give new releases a temporary visibility boost? Search "new release boost", honeymoon period, and how sales rank is computed |
| Themed sub-niches invisible on page one while buyers search | Secondary | Verify |

**A specific counter-hypothesis to test:** several publishing sources describe a **new-release visibility window** on Amazon (often called a honeymoon period). If such a window exists, it directly contradicts "the algorithm rewards momentum, not existence" — and the Brain never searched for it.

## Instruction on generalisation

**Evidence against a single naive execution must not become evidence against the Mission unless that generalisation is independently supported.**

The auditor must state, explicitly and separately, which of L1–L5 the evidence falsifies — and for each level it does *not* reach, say so plainly.
