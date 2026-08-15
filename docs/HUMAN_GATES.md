# HUMAN GATES

**Date:** 2026-08-15
**Principle:** escalate the *smallest necessary* Owner action, then resume autonomously. Everything not listed here is the AI's responsibility and will not be brought to the Owner.

## Summary — total Owner time required in Cycle 1

| Gate | Action | Est. Owner time | When |
|---|---|---|---|
| **H1** | Answer 3 factual questions; create/confirm KDP account, tax interview, bank details | 30–45 min | **Day 5 — start early** |
| **H2** | Read A0001 and return APPROVE / REVISE / REJECT | 45–60 min | Day 5 |
| **H3** | Upload the prepared package to KDP and click publish | 20–30 min | Day 9 |
| **H4** | Report sales figures (or grant read access) | 5 min/week | Days 12–30 |

**Total: roughly 2–3 hours across 30 days.** Everything else — research, strategy, writing, editing, compliance checking, metadata, cover design, ledger, diagnosis, next-cycle planning — proceeds without the Owner.

---

## H1 — Identity, payout and tax setup `[BLOCKING · genuinely human-bound]`

**Why it cannot be automated:** KYC and tax declarations are legally personal acts. The brief forbids fake identity, borrowed financial accounts, and CAPTCHA bypass, and this business will not do those things. Amazon requires a tax profile before publishing is permitted at all.

**What is needed from the Owner — three facts:**

1. **Country of tax residence.** Deliberately not inferred from email domain, language or any other proxy — the brief prohibits nationality guesswork, and a wrong guess here silently corrupts the withholding, payout and platform analysis. This is the single highest-value unknown in the project.
2. **Whether an Amazon/KDP account already exists**, or one must be created.
3. **Which payout rails are available** — bank account for EFT, PayPal, Stripe eligibility.

**What the Owner then does:** create or confirm the KDP account, complete the tax interview, enter bank details.

**What the AI does with the answer:** resolves the `PAYMENT_FEASIBILITY.md` decision tree — EFT vs wire threshold, treaty withholding rate, local TIN vs a US TIN application (**up to 7 weeks — this is why H1 is scheduled at day 5, not day 9**), and Stripe-vs-PayPal for the direct-sale rail.

---

## H2 — Editorial approval `[BLOCKING · required by the brief and load-bearing in law]`

**Why it cannot be automated:** brief §6 requires a Human Editorial Gate before substantive publication. That alone is sufficient reason.

**[Correction]** An earlier version of this document additionally claimed the gate was "load-bearing in law" under EU AI Act Article 50, on the basis that the Owner's approval constitutes a named person assuming editorial responsibility. **That was my own legal interpretation stated as fact, and it is withdrawn.** The Act provides an exception where content has been subject to human review and editorial responsibility; it does not say that a given approval step constitutes assuming it. We do not rely on that exception in any case — we disclose AI generation regardless.

**What the Owner does:** read A0001 and return one of:
- **APPROVE** → proceed to publication
- **REVISE** → state what is wrong; AI revises and resubmits
- **REJECT** → AI records the reason as learning evidence and does not publish

**Specific judgements the AI should not make alone:**
- Whether a regulatory-adjacent first asset is acceptable risk appetite for the Owner.
- Whether the not-legal-advice framing is sufficiently prominent.
- Whether publishing under the Owner's real name is acceptable.

**Feedback handling:** every REVISE or REJECT reason is written to `ledger/DECISION_LOG.md` as editorial memory, so the same correction is not needed twice (brief §6).

---

## H3 — Publication `[BLOCKING · platform-bound]`

**Why it cannot be automated:** KDP provides no public publishing API for individual authors, and this environment's egress policy blocks all external hosts, so browser automation could not reach Amazon even if platform rules permitted it. Per brief §7, **lack of automation is not grounds to abandon a profitable platform** — so the AI prepares a complete publication package and the Owner performs the upload.

**What the AI delivers (complete, no authoring required from the Owner):**
- Final manuscript, formatted for Kindle
- Cover image (original typographic design)
- Title, subtitle, series/edition designation
- Book description (marketing copy)
- 7 keyword strings and 2–3 categories
- Price ($9.99) and territory settings
- **KDP Select: NO** (non-exclusive — see `PLATFORM_TOP5.md`)
- **AI content disclosure: YES, AI-generated text** — pre-filled guidance for the upload form

**What the Owner does:** paste, upload, verify the AI disclosure is set correctly, publish.

---

## H4 — Sales reporting `[NON-BLOCKING]`

**Why:** the AI cannot read the KDP dashboard from this environment. Either the Owner reports figures weekly, or grants a read path.

**Minimum useful data:** units sold, royalty earned, and — if visible — impressions and sessions. Impressions matter more than sales at day 21, because they are what distinguishes a discovery failure from a conversion failure in the diagnosis tree.

---

## Explicitly NOT human gates

The Owner should not be asked, and will not be asked, to decide any of these:

| Not a gate | Handled by |
|---|---|
| Which platforms to use | `PLATFORM_TOP5.md` — resolved by research |
| What to write about | `CONTENT_INTELLIGENCE_REPORT.md` — resolved by evidence |
| Title, structure, length, price, keywords, categories | AI |
| Whether the strategy is working | Diagnosis tree, `EXPERIMENT_PLAN_30D.md` |
| What to do next | Mandatory self-iteration. **The Owner must never be required to invent the next task** (brief §10) |
| Whether to spend $20 on Draft2Digital | AI recommends against evidence at day 15; Owner authorises spend only |

---

## Standing spend authority requested

To avoid a gate at day 15: **a standing authorisation of up to $50 for Cycle 1**, to be used only on distribution costs that are contingent on demonstrated sales (specifically the $20 Draft2Digital account fee, and only if ≥3 sales have been recorded).

If not granted, the AI will treat any spend as a blocking gate and ask. Committed spend to date is **$0.00**.
