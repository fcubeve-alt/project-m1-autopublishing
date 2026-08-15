# PAYMENT FEASIBILITY

**Date:** 2026-08-15
**Hard rule observed:** no nationality guesswork. The Owner's country of tax residence is `UNKNOWN` and is **not** inferred from the account email domain, language, or any other proxy. This document maps the mechanism; the Owner supplies the one fact that resolves it.

## 1. The single unresolved variable

Everything below reduces to one input: **the Owner's country of tax residence and the bank account available there.**

That fact is not researchable — it is not on the public web, it is the Owner's private circumstance, and guessing it would violate the brief's explicit instruction. It is therefore a legitimate human gate (`HUMAN_GATES.md`, gate H1), not a research failure.

**It does not block current work.** The 30-day plan is sequenced so that manuscript production, editorial review and compliance checking all complete before payout setup is on the critical path. The answer is needed at approximately day 10, not day 1.

## 2. Amazon KDP payout mechanics — verified

| Element | Verified position | Source grade |
|---|---|---|
| Tax profile | **All non-US persons must complete a tax profile to be eligible to publish.** Not optional | P |
| Tax ID | A local tax identification number is normally accepted. If the country issues none of the accepted types, a US TIN can be applied for via the IRS — **up to 7 weeks** | P |
| Withholding | Statutory **30% US withholding**; reducible where an active US double-taxation treaty applies and the Owner qualifies as a resident under Article 4 | P |
| Payout method | **EFT / direct deposit has no minimum threshold** — paid in full regardless of amount. Cheque and wire have per-marketplace thresholds and possible fees/FX loss | P |
| Payment timing | **60 days after the end of the month** in which royalties meet the threshold | P |
| Royalty rate | 70% option, band **$2.99–$12.99 effective 2026-07-07**. Residency in a 70% territory is **not** required to receive the 70% rate — it depends on the customer's country | P |

**The three findings that matter most:**

1. **EFT has no threshold; wire and cheque do.** Whether EFT is available in the Owner's country is therefore the difference between receiving the first $7 royalty and waiting to accumulate a threshold. This alone can decide M1-B.
2. **Up to 7 weeks for a US TIN** if no acceptable local TIN exists. This is the only item that could delay first revenue by more than a month, which is why it is asked now rather than at publication.
3. **Cash lag is ~60–90 days** from first sale. This is why the success criterion was split into M1-A (sale recorded) and M1-B (cash received) in `STRATEGIC_REVIEW.md` §P5. Reporting a sale as "revenue realised" before cash lands would be a false report.

## 3. Direct-sale rail — payout coverage

Companion and fallback rails, ranked by breadth of payout coverage:

| Rail | Payout mechanism | Fee | Fit |
|---|---|---|---|
| **Ko-fi** | Stripe where available; **PayPal-only in countries without Stripe** | 0% tips / 5% Shop (free plan) | **Widest coverage — the fallback if Stripe is unavailable** |
| **Gumroad** | Direct bank transfer in 100+ countries; PayPal | ~10% | Broad, simple |
| **Payhip** | 13 payment processors; merchant-of-record covers EU/UK only | 5% free tier | Best at volume; MoR narrow |
| **Substack** | Stripe → bank, daily or weekly, **~48h** | 10% + Stripe fees | Fastest cash of any option, but audience-gated |

**Note on Stripe:** Substack documents India, Brazil, Indonesia, Mexico, Malaysia and Thailand as exceptions with differing fee treatment. If the Owner is in one of these or in a country Stripe does not serve, **Ko-fi's PayPal payout path is the designed fallback** — this is exactly why a direct rail is ranked #2 rather than dismissed.

## 4. Decision tree (resolves the moment H1 is answered)

```
Owner country known
├── EFT available for KDP in that country?
│   ├── YES → KDP primary. No threshold. First cash ≈ 60–90 days post-sale.
│   └── NO  → KDP still viable (wire/cheque, threshold applies)
│             AND raise direct-rail priority for faster small-sum cash.
├── Acceptable local TIN?
│   ├── YES → proceed; treaty may cut 30% withholding
│   └── NO  → start US TIN application IMMEDIATELY (up to 7 weeks — critical path)
└── Stripe available?
    ├── YES → Gumroad or Payhip as the direct rail
    └── NO  → Ko-fi (PayPal payout)
```

## 5. Cost side of the ledger

Committed spend to date: **$0.00.**

| Item | Cost | Status |
|---|---|---|
| KDP account and eBook publishing | $0 | No listing fee |
| Cover | $0 planned | Typographic cover; the design must be our own original work, not a purchased template |
| ISBN | $0 | Not required for Kindle eBooks |
| Research tooling | $0 | `WebSearch` only; no paid service |
| Writer | $0 marginal | `CLAUDE_MANUAL_SUBSCRIPTION` — existing subscription, per brief §14–17 |
| Draft2Digital | **$20 + $12/yr** if title earns <$100/12mo | **Deferred to day 15+, contingent on Amazon validating the asset** |

No paid infrastructure is proposed. The only spend on the horizon is the $20 D2D account fee, and it is explicitly gated on evidence.

## 6. Open items

| Item | Status | Owner |
|---|---|---|
| Country of tax residence | `UNKNOWN` | **Owner (H1)** |
| EFT availability in that country | `UNKNOWN` — resolves from country | Derived |
| Local TIN availability / US TIN need | `UNKNOWN` — resolves from country | Derived |
| Stripe availability | `UNKNOWN` — resolves from country | Derived |
| Existing Amazon or KDP account | `UNKNOWN` | Owner (H1) |
| Per-marketplace wire/cheque thresholds | `UNKNOWN` — `kdp.amazon.com` egress-blocked; only reachable via search snippets | Re-check at setup |
