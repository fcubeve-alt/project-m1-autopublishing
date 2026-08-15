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

## Editorial memory

*Owner feedback from the Human Editorial Gate is recorded here so the same correction is never needed twice (brief §6). Empty until H2.*

| Date | Asset | Verdict | Feedback | Rule derived |
|---|---|---|---|---|
| — | — | — | *awaiting first editorial gate* | — |
