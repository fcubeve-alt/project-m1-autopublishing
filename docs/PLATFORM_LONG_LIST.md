# PLATFORM LONG LIST

**Compiled:** 2026-08-15 · **Researcher:** Autonomous Business Brain
**Method:** `WebSearch` with `allowed_domains` scoping to official help centres and policy pages where reachable; general web search otherwise. `WebFetch` is unavailable — this session's egress policy denies direct HTTPS to all external hosts tested (see `DEVELOPMENT_ENVIRONMENT_PREFLIGHT.md`).

**Evidence grades**
- **P** — Primary. Extracted from the platform's own help centre, policy page or official blog.
- **S** — Secondary. Trade press, practitioner reporting or aggregated search synthesis. Directionally reliable, not authoritative.
- **U** — `UNKNOWN`. Not verified. Per the brief's hard rule, not filled in from model memory.

**Reading note:** the "Verdict" column answers one question only — *can an AI-assisted publisher lawfully earn here in August 2026?* A platform can be large, healthy and irrelevant to us at the same time.

---

## Category A — Marketplace retail (buyer arrives with purchase intent)

| # | Platform | How creators earn | AI policy | Evidence | Verdict |
|---|---|---|---|---|---|
| 1 | **Amazon KDP (eBook)** | 35% or 70% royalty. 70% band **$2.99–$12.99 as of 2026-07-07** (was $2.99–$9.99) | AI-**generated** text/images/translations must be disclosed at upload; AI-**assisted** need not be. Undisclosed AI = violation, account-level risk | P | **PRIMARY CANDIDATE** |
| 2 | **Amazon KDP Print** | Paperback royalty net of print cost | Same as above | P | Candidate (phase 2) |
| 3 | **Kindle Unlimited / KDP Select** | ~$0.00482 per normalised page (Apr 2026), diluting shared fund | Same as above | S | **Reject for A0001** — requires exclusivity, kills asset reuse |
| 4 | **Draft2Digital** | ~60% net after D2D's ~10% cut | **$20 to open a new account** and **$12/yr maintenance if a title earns <$100/12mo** — explicitly an anti-AI-content-farm measure | S | Candidate (phase 2), friction is intentional |
| 5 | **Kobo Writing Life** | 45% under $2.99; **70% at $2.99+** | U | S | Candidate (phase 2) |
| 6 | **Apple Books** | 70% | U | S | Candidate (phase 2) |
| 7 | **Google Play Books** | 52% | U | S | Lower priority (weakest split) |
| 8 | **Barnes & Noble Press** | U | U | U | Deferred |
| 9 | **IngramSpark** | U; print-focused, setup fees | U | U | Deferred — not zero-cost |
| 10 | **Leanpub** | 80% royalty (reported), technical/in-progress books | U | S | Watch — good split, niche audience |
| 11 | **Etsy (digital downloads)** | Sale price less fees | Disclosure mandatory on every listing; listings without it **filtered from search**. From **2026-08-11**, computerised-tool + templated designs disallowed unless the design is the seller's original work; purchased/templated prompts violate policy | P/S | **Deprioritised** — rules tightened 4 days ago, enforcement unclear |
| 12 | **Gumroad** | ~10% fee; direct bank transfer in 100+ countries | U | S | Fallback direct-sale rail |
| 13 | **Payhip** | Free tier 5% fee; paid tiers $29–$99/mo at 0–2% | U | S | Fallback direct-sale rail |
| 14 | **Ko-fi** | 0% on tips; 5% on Shop (free plan); PayPal-only payout where Stripe absent | U | S | Fallback, useful where Stripe unavailable |
| 15 | **Lemon Squeezy** | Merchant-of-record model | U | U | Watch — MoR handles VAT |
| 16 | **Sellfy** | U | U | U | Deferred |
| 17 | **Podia** | U | U | U | Deferred |

**Category read:** this is where the money is for us. Amazon is the only surface offering *free, purchase-intent distribution to an unknown seller on day one* while explicitly permitting disclosed AI-generated content.

---

## Category B — Serial fiction / web novel

| # | Platform | How creators earn | AI policy | Evidence | Verdict |
|---|---|---|---|---|---|
| 18 | **Royal Road** | Indirect — audience → Patreon/KDP | Three-tier policy. AI-**enhancement** (Grammarly-class) untagged. AI-**assisted** and AI-**generated** permitted **but must be tagged**, chapter pages only, quality must be maintained. No AI artwork exceptions. Comments/reviews/forum posts must stay human | P | **Viable but commercially punishing** — documented reader backlash against tagged works |
| 19 | **Wattpad** | Paid Stories / Creators Program | U for AI-authored content. Uses AI for moderation; reports of opaque shadow-banning | S | Deprioritised — moderation opacity is an unpriceable risk |
| 20 | **Tapas** | Reader subscriptions / ink | U | S | Deferred |
| 21 | **Inkitt / Galatea** | Contract-based; deployed AI personalisation in Galatea 2.0 (2025) | U for author-side AI | S | Deferred — contract terms need review |
| 22 | **Dreame** | Contract/exclusivity | U | U | Deferred |
| 23 | **Webnovel** | Contract/exclusivity; launched expanded **AI writing toolkit Feb 2026** | U for author-side AI | S | Watch — platform is AI-friendly directionally |
| 24 | **ScribbleHub** | Indirect | U | U | Deferred |
| 25 | **Laterpress** | Direct serial sales; positioned as Kindle Vella successor | U | S | Watch |
| 26 | **Radish** | Contract/exclusivity | U | U | Deferred |
| 27 | **Kindle Vella** | — | — | P | **DEAD** — shut down 2025-02-26 |

**Category read:** long time-to-revenue, audience-building required, and the tagging regimes convert our AI advantage into a scarlet letter. Not the Phase-1 route.

---

## Category C — Per-read, ad-share and creator programs

| # | Platform | How creators earn | AI policy | Evidence | Verdict |
|---|---|---|---|---|---|
| 28 | **Medium** | Partner Program, member reading time | **AI-generated writing cannot be paywalled — disclosed or not.** Undisclosed → Network Only distribution. Disclosed → General Distribution, never Boost. Enrollment can be revoked | P | **CLOSED to us** |
| 29 | **Vocal Media** | Per-read + tips; Vocal+ subscription | U — could not verify; `vocal.media` egress-blocked and no primary source reachable | U | **UNKNOWN — do not assume viable.** The brief's template candidate is unverified |
| 30 | **NewsBreak** | RPM-based | U | S | Marginal — needs 200 followers + 10 articles; contributor reach degraded since 2024 |
| 31 | **HubPages** | Ad share | — | S | **DYING** — stopped accepting new content 2025, wind-down finalising 2026 |
| 32 | **Quora Partner Program** | Ad share on questions | — | S | **CLOSED to new participants** |
| 33 | **Reddit Contributor Program** | $0.90/gold (100–4,999 karma); $1.00/gold (5,000+ karma), min 10 gold | U | S | Not a publishing business; karma gate is an audience gate |
| 34 | **Simily / small per-read sites** | Per-read | U | U | Deferred — insufficient scale to matter |

**Category read:** this category is the brief's centre of gravity and it is substantially closed, dying, or unverifiable. This is the single most important finding of Phase 0.

---

## Category D — Subscription / newsletter / membership

| # | Platform | How creators earn | AI policy | Evidence | Verdict |
|---|---|---|---|---|---|
| 35 | **Substack** | Paid subscriptions; **10% platform fee** + Stripe 2.9% + $0.30 + 0.5% billing. Creator keeps ~85–87%. Payouts daily/weekly, ~48h to bank | U for AI-authored content | P | Good economics, **but requires an audience we do not have** |
| 36 | **beehiiv** | Paid subs, Ad Network (Scale plan+), Web Boosts. **Email Boosts and Direct Links deprecated 2026-04-10.** Ad Network pays >$1M/mo across publishers | U | P | Same audience problem; Ad Network gated behind paid plan |
| 37 | **Ghost** | Self-hosted/Pro subscriptions | N/A (self-hosted) | U | Deferred — hosting cost, no built-in demand |
| 38 | **Patreon** | Membership | U | S | Downstream of an audience, not a source of one |

**Category read:** best margins in the entire survey, worst cold-start. Correct destination *after* first revenue, wrong starting point.

---

## Category E — Adjacent (courses, audio, licensing)

| # | Platform | How creators earn | AI policy | Evidence | Verdict |
|---|---|---|---|---|---|
| 39 | **Udemy** | Marketplace share 37%; **subscription share cut to 15% in Jan 2026** (was 25%); up to 97% on instructor-driven coupon sales | U | S | Watch — share erosion is a bad trend |
| 40 | **Skillshare** | Royalty pool by premium watch minutes, ~$0.05–0.10/min | U | S | Deferred |
| 41 | **Teachable** | Own storefront | N/A | U | Deferred |
| 42 | **ACX / audiobooks** | Royalty share | U | U | Phase 3 — natural derivative of a proven text asset |
| 43 | **Paying literary magazines** (Clarkesworld and peers) | Per-word rates | **Explicitly refuse "AI"/"AI-assisted" works** | P | **CLOSED to us** |

---

## Summary of the evidence

**Closed or dead to an AI-assisted publisher (7):** Medium Partner Program, paying literary magazines, HubPages, Quora Partner Program, Kindle Vella, and — for practical purposes — Wattpad and Etsy's templated-design route.

**Open, with disclosure (the real opportunity set):** Amazon KDP and the wide-retail aggregators; direct-sale rails (Gumroad / Payhip / Ko-fi); Royal Road under tagging.

**Open but audience-gated:** Substack, beehiiv, Patreon, Reddit.

**Unverified and therefore not counted as viable:** Vocal Media — the brief's own template candidate — plus most Category B contract platforms.

**The decisive asymmetry:** exactly one surface in this entire survey gives an unknown publisher free access to buyers with money out, on day one, with AI-generated content expressly permitted subject to disclosure. That is Amazon's search box. Everything else either requires an audience we do not have, forbids what we are, or is winding down.
