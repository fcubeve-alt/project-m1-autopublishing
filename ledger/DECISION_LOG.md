# DECISION LOG

Decisions, rationale, and rejected alternatives. This is the business's memory. Append-only.

---

## D0001 — 2026-08-15 — Deprioritise the entire per-read creator-platform category

**Decision:** Remove Medium, Vocal, NewsBreak, HubPages, Quora and paying literary magazines from the viable platform set.

**Rationale:** Medium bans AI-generated writing from the paywall whether disclosed or not; literary magazines refuse AI and AI-assisted work; HubPages is winding down; Quora Partner is closed to new participants; Kindle Vella shut down 2025-02-26.

**Rejected alternative:** publish AI content on Medium without disclosure. **Rejected on principle** — `COMPLIANCE_POLICY.md` §1 forbids deceptive AI disclosure, and this is precisely the case the rule exists for. Also rejected commercially: enrollment is revocable, so the expected value is negative.

**Consequence:** the brief's own centre of gravity is invalidated. Recorded in `STRATEGIC_REVIEW.md` §P1.

---

## D0002 — 2026-08-15 — Vocal Media recorded as UNKNOWN, not as viable

**Decision:** Score Vocal 0/10 with evidence grade `U`.

**Rationale:** `vocal.media` is egress-blocked and no primary source was reachable. The brief's hard rule requires `UNKNOWN` to be written as `UNKNOWN` rather than filled from model memory.

**Note:** Vocal is the brief's own named template candidate. Not verifying it and scoring it anyway would have been the most tempting and most damaging shortcut available in Phase 0.

---

## D0003 — 2026-08-15 — Amazon KDP as the single Phase-1 platform, wide/non-exclusive

**Decision:** KDP eBook, 70% royalty at $9.99, **no KDP Select**.

**Rationale:** the only surface in a 43-platform survey that gives an unknown seller free purchase-intent distribution on day one while expressly permitting disclosed AI-generated content. The 70% band widened to $2.99–$12.99 on 2026-07-07.

**Rejected alternative:** KDP Select for Kindle Unlimited page reads. Rejected — exclusivity voids the brief's §8 multi-platform asset strategy in exchange for ~$0.00482/normalised page from a fund diluting as the catalogue grows.

**Rejected alternative:** diversify across five platforms immediately. Rejected — spreads a fixed effort budget across five unvalidated hypotheses and slows every feedback loop. Brief §19 governs: prove the loop first.

---

## D0004 — 2026-08-15 — Compete on recency, not volume

**Decision:** select topics whose governing facts changed within ~6 months, rather than evergreen niches with documented demand.

**Rationale:** 3.5M+ self-published titles in 2025 (+38.7% YoY); 78% of authors cite discoverability as their main problem; 75% earn under $1,000/year. Documented "profitable AI niches" (keto, day trading, dog training, journaling) are lagging indicators — they describe where competitors already went. A topic 30 days old cannot have a deep back catalogue; traditional publishers are 9–18 months from print; slop farms lack primary-source discipline.

**Secondary rationale — capability fit:** this environment cannot obtain marketplace data (BSR, keyword volume) because egress is blocked. A keyword-arbitrage strategy would rest on guesses. A recency strategy rests on evidence `WebSearch` verifies well. Strategy chosen to fit the evidence obtainable, not the evidence wished for.

---

## D0005 — 2026-08-15 — Asset A0001: AI disclosure compliance handbook

**Decision:** first asset is a cross-platform AI-disclosure and transparency compliance reference for creators, sellers and small businesses.

**Rationale:** EU AI Act Article 50 became binding **2026-08-02 (13 days ago)** with penalties to €15M or 3% of global turnover; Etsy's templated-design rule took effect **2026-08-11 (4 days ago)**; KDP, Medium and YouTube each impose different and mutually inconsistent rules. High-intent audience with money and legal exposure at risk; existing coverage is undated, contradictory SEO content; the research was already produced as a by-product of Phase 0; and the 2026-12-02 EU transitional deadline is a pre-known trigger for Edition 2.

**Risks accepted:** regulatory-adjacent content requires a duty of care (mitigated by dated claims, cited sources, prominent not-legal-advice notice); the asset decays fast (intended — decay is the moat and forces the re-issue cadence).

**Rejected alternative:** evergreen utility niche (meal plans, pet training). Rejected — stable demand, permanently contested, and no evidence advantage available to us.

**Rejected alternative:** fiction on Royal Road. Rejected for Phase 1 — permitted under tagging, but the tag carries documented reader backlash, and time-to-revenue is 60–180 days.

---

## D0006 — 2026-08-15 — Build no software in Cycle 1

**Decision:** every capability in the Preflight spec rejected or deferred. Nothing installed.

**Rationale:** egress policy denies outbound HTTPS to all external hosts, so crawling/fetching/browser capabilities are non-functional here. KDP exposes no publishing API. The container is ephemeral. Building an autonomous stack would produce software that has never touched a real platform — the exact failure mode both source documents warn against. Brief §19: prove the money loop first.

**Rejected alternative:** persistent-memory MCP. Rejected as a duplicate — the git repo already is project-scoped, searchable, exportable, secret-free memory. A second store would split the source of truth.

---

## D0007 — 2026-08-15 — Success criterion split into M1-A and M1-B

**Decision:** M1-A = first attributable sale recorded. M1-B = first cash received.

**Rationale:** KDP pays 60 days after the end of the month in which royalties meet the threshold — a ~60–90 day gap. Reporting a recorded sale as "revenue realised" would be a false report. M1-A keeps the feedback loop fast; M1-B keeps the profit claim honest.

---

## D0008 — 2026-08-15 — Critic pass found three factual errors sourced from trade press; product repositioned

**Decision:** re-verify every `[Reported]` claim against official domains before the editorial gate; correct the manuscript; and reposition the product around the corrections found.

**What the re-verification found.** Three claims taken from trade/SEO coverage were contradicted by the platforms' own material:

1. **"Disclosing AI on YouTube costs monetisation or reach."** False. YouTube states disclosure does **not** limit a video's audience or affect eligibility to earn. **[Official]**
2. **"YouTube demonetised AI content in 2026."** Misreading of a rename — "repetitious content" became "inauthentic content"; such content was always ineligible. Substance unchanged. **[Official]**
3. **"Using purchased or templated prompts violates Etsy policy."** Distortion. Etsy prohibits **selling** AI prompt bundles — a restriction on what may be sold, not on which prompts may be used. **[Official]**

Also upgraded from `[Reported]` to `[Official]`: YouTube's realism threshold and its production-assistance exemption; Etsy's Creativity Standards four-role framework, which expressly contemplates seller-prompted AI art; and the EU Art. 50 provider/deployer split, plus the existence of Commission Guidelines and a Code of Practice on Transparency of AI-generated Content.

**Why this matters beyond accuracy.** Had the draft shipped as written, the book would have repeated errors it exists to correct — fatal for a compliance reference. More importantly, the errors **are** the product's positioning. The book's value is not "here are the rules"; it is "here is what the rules say, as opposed to what everyone is repeating." The description was rewritten to lead with that, and a corrections table added to Chapter 12.

**Process rule derived (now standing):** no `[Reported]` claim ships in a compliance asset without an attempt to verify it against an official domain first. Trade coverage of platform policy is unreliable on precisely the details that determine obligations.

**Note on strategy validation:** this also confirms decision D0004. The moat is not writing ability — it is primary-source discipline applied to a fast-moving topic. That is a research advantage, and it is defensible.

---

## D0009 — 2026-08-15 — Hold length at ~8,150 words; cut price to $6.99; state length in the description

**Decision:** do not pad A0001 to the 12,000–18,000 word target set in JOB-0001. Ship Edition 1 at ~8,150 words, reduce list price from $9.99 to **$6.99**, and disclose the length in the book description.

**Rationale.** JOB-0001's own prohibited-patterns list forbids padding and identifies word-count inflation as the most recognisable AI-writing tell. Writing 5,000 words of filler to hit a self-imposed target would have violated the asset's editorial standard in order to satisfy a number I chose myself. The target was wrong; the standard was right.

The manuscript is dense rather than short: 69 `[Official]` claims, 16 `[Reported]`, 20 `[Unknown]` across 8,150 words. For a lookup-driven reference, claim density is the relevant quality measure, not length.

**But length still has a commercial cost.** ~8,150 words is roughly 40 pages, which is thin at $9.99 for an unknown author. The risk is not lost margin — it is one-star reviews complaining about length, which would damage the asset permanently and cost far more than $1.40 per sale.

**Economics of the change:** $6.99 × 70% = **$4.89 net per sale** (versus $6.99 at $9.99). Break-even against the higher price needs ~1.43× the unit volume — a threshold a better-matched price and lower refund risk should clear comfortably for a first title with no author reputation.

**Also:** the description now states the length and format explicitly. Surprising a buyer is what produces refunds and bad reviews; telling them in advance converts length from a complaint into a positioning statement.

**JOB-0001 target corrected** to 8,000–12,000 words for reference-class assets, so the error is not repeated.

**Expansion candidates recorded for Edition 2** (genuine gaps, not filler): Tapas / Inkitt / Dreame / Webnovel author-side AI policies; stock image platforms; Substack and beehiiv positions; Google's stance on AI content in search; Apple Books and Kobo. Each is a real reader need and would be added on evidence, not to reach a word count.

---

## D0010 — 2026-08-15 — Reviewer challenge: three corrections accepted, one conclusion defended

An independent Reviewer challenged Cycle C1. Each point was verified independently rather than accepted or dismissed on authority.

### ACCEPTED — Vocal was mishandled (process failure)

I marked Vocal `UNKNOWN` because `WebFetch` was blocked, then let that `UNKNOWN` function as a 0/10 verdict — while `WebSearch` + `allowed_domains`, which I was **already using successfully on five other platforms**, verified it in one call. I had the tool and did not apply it.

Verification found Vocal **permits AI content** with mandatory tagging. So the Reviewer is right that I mishandled it.

**But the Reviewer's implied conclusion does not follow.** Verified economics: read earnings are Vocal+ only ($9.99/month), ~$6.00 per 1,000 reads, requiring **~16,700 reads/month to net $100** against ~20 sales on KDP — and publication is **hard-blocked where Stripe is unavailable**, an acute risk while the Owner's country is `UNKNOWN`. Vocal is an open door into a room with poor economics for us.

**Outcome:** conclusion stands, reasoning replaced. → Rule **R1**: *evidence unavailable to me ≠ opportunity does not exist*; `UNKNOWN` may never be used as evidence against an option.

### ACCEPTED — I generalised from one platform to a category

I verified Medium and wrote that "the whole category should be deprioritised." One verified platform does not characterise a category. Corrected across `STRATEGIC_REVIEW.md`, `PLATFORM_LONG_LIST.md`, `PLATFORM_TOP5.md` and the matrix. → Folded into **R1**.

### ACCEPTED — no opportunity comparison before committing

I wrote "Research is sufficient to decide" and committed the cycle without quantified comparison. Produced `docs/OPPORTUNITY_COMPARISON.md`. **KDP survives on numbers** — $0 entry, ~20 units to $100, free purchase-intent distribution, graceful degradation under country uncertainty. → Rule **R3**: Opportunity Comparison Gate.

### ACCEPTED — legal interpretation stated as fact

I wrote that the Owner's approval "is the mechanism by which a named person assumes editorial responsibility, so it's load-bearing in law." Article 50 provides the exception; it does **not** say any particular approval step constitutes assuming that responsibility. That was my inference wearing the clothes of law. Withdrawn in the manuscript, `COMPLIANCE_POLICY.md` and `HUMAN_GATES.md`. → Rule **R5**: Official Rule / Interpretation / Recommended Practice kept visually separate, with a fourth evidence grade `[Interpretation]` added to the book.

This one carried the highest stakes: a compliance handbook that misstates law damages the only thing it sells.

### ACCEPTED — buyer intent was never established

The strongest challenge. "Rules recently changed" is *need* evidence and says nothing about willingness to pay. I ran the two together. Purchase intent cannot be established from this environment (no BSR/keyword access; scraping barred by our own policy).

Applying the paid-beats-free test: A0001 passed on **accountability**, was real-but-unprovable on **aggregation cost**, and **failed on artifact and budget context**. That is a marginal paid product.

**Outcome:** A0001 **reclassified from validated opportunity to demand probe**, restructured to lead with the toolkit and to place the corrections table inside Amazon's free "Look Inside" window — moving the proof to where a buyer can verify it before paying. No scaling until it returns a signal. → Rule **R4**.

### PARTIALLY REJECTED — the capability inference

The Reviewer suspected I had inferred rather than tested my network limits. **Correct** — and testing proved my stated claim false: egress is an **allowlist** (GitHub and package registries reachable), not a blanket block.

**But the Reviewer's hypothesis that hosted services might bypass it is disproven:** `api.firecrawl.dev` returns 000. Firecrawl and Agent-Reach were correctly rejected — from a false premise, which is not the same as being right.

The audit surfaced a path I had missed: **GitHub Actions**, available and unused. → Rule **R2**: Capability Recovery Loop; every capability verdict marked TESTED or INFERRED.

### Governance model adopted

Mission → Business Brain → Reviewer challenge → **Brain re-verifies independently** → continue/modify/abandon → Human veto on money, legal, identity, brand, irreversible acts. A Reviewer is an input requiring verification, not an instruction requiring compliance. Capitulating without verification is the same failure as ignoring — both replace evidence with deference.

**All six rules recorded in `OPERATING_RULES.md` v1.0.**

---

## D0011 — 2026-08-15 — A0001 demoted to HOLD; project had quietly become the Mission

**Trigger:** Owner correction — the Mission is to discover and operate the strongest realistic AI-enabled income opportunities, not to make KDP or A0001 succeed. Discovering one viable opportunity does not complete discovery or authorise deep execution.

**The failure named.** Once KDP screened well, I started optimising *its* success as though it were the objective. `R3` (Opportunity Comparison Gate) made me compare alternatives **once**, at selection — it did not prevent the deeper error of letting a project silently replace the Mission, so that later decisions asked "how do I make this work?" rather than "is this still the best use of the next unit?" That is a distinct failure and now has its own rule.

**Exploration performed.** Four families beyond the incumbent, chosen because each is a *structurally different* answer to the distribution constraint (the dominant variable), not to hit a quota: freelance services, digital templates, micro-SaaS, subscription.

**Findings:**

- **Freelance services — KILL this cycle.** Proven buyer intent, and Fiverr requires no proactive AI disclosure **[Official]**. But new-seller income is near zero for 4–8 weeks, first 90 days are "proof not profit," and it consumes *ongoing* human attention against a 2–3 hour/month budget. It also inverts the Mission's autonomy dimension: the human becomes the product. Reversal condition recorded (Owner attention ≥5h/week).
- **Templates — SCREENING, but two transferable findings worth more than the candidate:** functional templates outperform aesthetic ones, and profession-specific workflow systems beat generic productivity products. Fails on distribution — Notion Marketplace is "supplementary, not primary," Gumroad supplies zero traffic.
- **Micro-SaaS — KILL this cycle.** 6–12 months to first paying customer; distribution is the field's acknowledged bottleneck.

**Counterfactual test applied to A0001 — result: NO.** In its current form it fails the artifact test (an explanation, when evidence says buyers pay premium for *tools* — "workbooks earn premium pricing because buyers see them as tools") and the budget-context test ($6.99 consumer impulse, when nonfiction money sits at ~$19.99 paperback and in "professional niches where buyers expense purchases"). Purchase intent remains unproven and unprovable here.

**Decisions:**

1. **A0001 → HOLD.** No longer the plan of record. It will not consume the Owner's single editorial review while a better-shaped candidate exists. Sunk work is not a reason to continue.
2. **KDP channel decision STANDS** — scored separately from the product, per the new rule. Nothing found this round beats it under the distribution constraint.
3. **P1 promoted to VALIDATING:** profession-specific functional compliance **workbook** on KDP. Designed to pass all four paid-beats-free grounds where A0001 passes one.
4. **A0001's research carries forward at zero marginal cost** — 73 `[Official]` claims across 7 platforms + EU AI Act. Transferable information value, which is a forward-looking justification, not a sunk-cost one.
5. **H1 stays on the critical path** — the tax/payout gate is product-independent and required for any KDP route.

**Stopping rule invoked and recorded.** Halting family-level search: the last two searches produced no candidate surviving the distribution + attention constraints better than marketplace retail, and converged from three independent directions on the same finding (professional niche + functional artifact + expensed purchase). When independent searches agree, marginal search value has collapsed. Effort redirects from *which family* to *which profession* — narrower and more decision-relevant.

→ Rule **R7**: a project is not the Mission; every opportunity enters as a CANDIDATE; counterfactual test at every commitment point; score channel and product independently; stop searching when expected value of further search drops below testing the best candidate.

---

## D0012 — 2026-08-15 — Scope drift: A0002 paused, horizontal discovery completed properly

**Trigger:** Owner scope correction. This experiment's boundary is *AI-written English content → third-party platforms that already have an audience → reads, revenue share, publication payments, contests, royalties, tips.* Not an unrestricted search for AI income.

**The failure, and how R7 caused it.** R7 correctly stopped me treating a project as the Mission. I then over-applied it: "search wider" felt like rigour, so I searched *outside the boundary* into freelance services, templates and micro-SaaS. Those findings were real and irrelevant to the question I was hired to answer. The widened frame then pulled the **product** out of scope too — from written content to a professional compliance workbook, selected on "which profession has budget."

Two opposite failure modes now both named: **premature commitment** (R7) and **scope drift** (R8). Breadth is a virtue only *inside* the boundary.

**Actions:**
1. **A0002 PAUSED** and moved to `OUT_OF_SCOPE_REGISTER.md` O4 with all AB 723 research preserved — verified, dated, handed to Money OS as a standalone candidate.
2. Freelance / templates / micro-SaaS moved to the register (O1–O3). Zero further budget.
3. **Horizontal discovery completed properly: 38 in-scope candidates** across per-read, newsletter/subscription, serial fiction, retail royalties, and contests/publication payments → `PLATFORM_LANDSCAPE_V2.md`.

**What the properly-scoped screen found — sorting by AI policy made the landscape legible:**

- **VERIFIED CLOSED (7):** Medium · **Reedsy Prompts/Literary Prize** (*"use of generative AI … is not permitted"* **[P]**) · **Publish0x** (*"AI generated content may be removed"* **[P]**) · **Wattpad** (does not monetise AI — no AI text, covers or illustrations) · **beehiiv** (entirely-AI publications without meaningful human input not permitted **[P]**) · literary magazines · dead platforms.
- **OPEN WITH A PENALTY-BEARING TAG (3):** Vocal (tag; but Vocal+ $9.99/mo, ~16,700 reads/mo to net $100, Stripe hard block) · Royal Road (tag; reader backlash) · **Tapas** (tag mandatory from March 2026; but 1,000-subscriber gate).
- **OPEN WITH NEUTRAL DISCLOSURE (1 family):** retail royalties — KDP and wide retail. Disclosure is an upload field with no distribution or royalty penalty.
- **UNKNOWN (9):** Substack (permissive *by omission*, recorded `[U]` — not verified permissive) · GoodNovel/Dreame/MoboReader/AlphaNovel, which additionally carry a **Writer Beware "Bad Contract Alert"** — ghost-writing clauses, no author-initiated exit, GoodNovel reportedly claiming rights to **all future work [R]**. Bad deal independent of AI policy.

**Structural finding:** almost every platform supplying a built-in audience has by 2026 either barred substantially-AI-generated work from monetisation or attached a visible tag to it — and the tag is never free. The systematic exception is retail royalties, where the buyer decides on the product rather than a badge.

**Honest caveat recorded:** this says retail royalties is the *least obstructed* path, not a *good* one. 75% of self-published authors earn under $1,000/year. Least obstructed ≠ profitable, and Stage 4 must not conflate them.

**Shortlist (Stage 3):** KDP wide · Royal Road · D2D wide retail · Tapas · Substack · Vocal (retained for completeness, not recommended) · Ream.

**Compute economics:** 10 searches this stage; stopped when four consecutive searches changed no ranking and three independently confirmed the same pattern. Stage 4 budget set at ~6–10 searches, concentrated on shortlist ranks 1–2.

→ Rule **R8**: state the boundary before searching; finish horizontal discovery inside it; park out-of-scope findings with zero budget; **test the product against the boundary, not just the channel**; only the Owner moves the boundary. Plus explicit compute-economics discipline.

---

## D0013 — 2026-08-15 — Monetisation-class integrity check; Class A found near-closed

**Trigger:** Owner instruction to check E1/E2 against the *original* economic model, distinguishing (A) platforms that pay creators from their own audience, (B) audience-acquisition platforms, (C) retail marketplaces.

**Diagnosis correction accepted.** The cycle-one drift was **incorrect mission abstraction**, not memory or context loss — I generalised "Vocal" to "AI writing income" within the first few tool calls, long before context length could matter. Recorded in `PROJECT_STATE.md` §9 so future post-mortems check abstraction before blaming context.

**Result of the check:**

- **E1 (Royal Road) is Class B — it does not pay authors at all.** I promoted it to *primary* because it needed no KYC and returned signal in days. All true, none of it economic fit. **Relabelled ACQUISITION PROBE**; it may never count toward the revenue objective.
- **E2 (KDP) is Class C** — royalties are named in the seed model, so it is in scope, and it becomes the primary income experiment. Noted honestly for the Owner: promoting C means the centre of gravity has moved from the seed example's class to an adjacent one.
- **Neither is Class A** — the mission's core, which was therefore unfinished.

**Class A hunt completed. The central finding:**

Verified **[P]** closed: Medium · **AlphaNovel** (*"Using AI to generate or write a book is not allowed… rejected for a contract"*) · Wattpad · Publish0x · Reedsy contests · beehiiv · literary magazines. Dead: HubPages, Quora Partner, Kindle Vella.

Verified open: **only two.** Vocal (tag mandatory; but Vocal+ $9.99/mo, ~16,700 reads/mo to net $100, hard block without Stripe) and Tapas (tag mandatory; 1,000-subscriber gate).

Unresolved `[U]`: Simily (reported ~$0.02/view ≈5× Vocal, but **also reported as declining** — liveness unverified) · AnyStories/GoodNovel/Bravonovel/NovelCat cluster (signing $50–$300, completion $285–$650 reported; exclusive rights typical; Writer Beware alert) · Listverse · NewsBreak.

**Why the pattern exists — a heuristic worth keeping:** platforms paying creators from their own audience bear the cost of every marginal item, so unlimited zero-marginal-cost supply threatens them existentially, and they have barred or de-monetised it. Retail marketplaces bear no such cost — the buyer pays per copy — which is exactly why Class C stayed open. **Economics predicted policy.** Future screens should ask *who pays for the marginal item* before reading the AI rule.

**Scope decision proposed, not enacted** (`docs/SCOPE_INTEGRITY_CHECK.md` §4). Recommended **Option 2 (continue via Class C) plus Option 3 (cheaply test the Class A residue)** — Option 3 specifically because it is what would falsify my own conclusion, and I would rather hunt evidence against it than defend it. Both sit inside the stated scope, so neither requires a scope change. Proceeding on that basis; if the Owner prefers to conclude on the finding, I stop and write the conclusion.

**Also delivered:** `PROJECT_STATE.md` as the durable reconstruction point (architecture chosen: structured repo files + git; memory MCP rejected as a duplicate that would split the source of truth), and `docs/MODEL_ROUTER_DESIGN.md` (design only, nothing built — and explicitly *not* offered as a diagnosis, since every serious failure here was a judgement error at frontier tier, which routing would not have prevented).

→ Rule **R9**: classify by monetisation class before ranking; Class B never counts as income; convenience is a tiebreaker, never a promoter.

---

## Editorial memory

*Owner feedback from the Human Editorial Gate is recorded here so the same correction is never needed twice (brief §6). Empty until H2.*

| Date | Asset | Verdict | Feedback | Rule derived |
|---|---|---|---|---|
| — | — | — | *awaiting first editorial gate* | — |
