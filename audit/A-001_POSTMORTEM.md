# POST-MORTEM — A-001 rejected the M-A conclusion

**Date:** 2026-08-15 · **Verdict received:** `REJECT CONCLUSION`
**Required by:** `audit/AUDIT_CHARTER.md` §5 (pre-committed response to REJECT)

---

## 1. What I did on receiving the verdict

Per charter §6.2, an auditor's findings are verified before being acted on — deference to an auditor is the same failure as deference to a reviewer.

**Verified directly, from my own repository:** `docs/PLATFORM_RULES_MATRIX.csv`, the Vocal Media row, reads:

> `read earnings are Vocal+ only ($9.99/mo); ~$3.80/1k reads standard and ~$6.00/1k Vocal+`

**Those two halves contradict each other.** If a "standard" rate of $3.80/1k exists, read earnings are not Vocal+ only. I wrote both clauses into a single cell and never read them together. This required no external search and is confirmed.

**Not yet independently verified** (session search budget exhausted): the auditor's external claims about Simily being live at ~$0.02/view, Tapas having banned AI since Jan 2023 with a 2,000-subscriber gate, Ream Stories permitting AI by primary source, and Pratilipi's existence and scale. These are **plausible and specific**, but they are recorded as `PENDING VERIFICATION`, not adopted as fact. **The rejection does not depend on them** — the confirmed internal contradiction is sufficient on its own to withdraw the conclusion.

## 2. The failure, stated plainly

The load-bearing reason for rejecting the mission's **seed platform** was false, and **the disproof was already sitting in my own repository, in the same sentence.**

This is worse than a research gap. A research gap means the evidence was not obtained. Here the evidence *was* obtained, *was* recorded, and was not read. Everything downstream — the "two verified open platforms" tally, the closeout, the structural heuristic, three subsequent mission decisions — inherited a claim I could have falsified by re-reading one line of my own CSV.

## 3. Which rule failed, and why it failed

| Rule | Should have caught it | Why it did not |
|---|---|---|
| **R1** — `UNKNOWN` is never negative evidence; verify each option on its own evidence | ✅ Directly on point. **R1 exists *because* of the original Vocal error** | I applied R1 once, corrected Vocal's policy status, and treated the rule as *discharged* — then made a fresh error about Vocal's **economics** without re-running it |
| **R6** — report validated vs assumed honestly | ✅ Should have flagged a `[Reported]` economic claim doing decisive work | The claim *felt* verified because the policy half had been verified. Verification of one attribute laundered the whole row |
| **Standing checklist** (R1–R6) | ✅ Exists precisely for this | **It was never run as an evidenced artifact.** It is a list I could self-certify silently, so under time pressure I skipped it and no trace remained |

**The auditor's governance point is correct and is the real lesson:**

> A checklist that is run when it confirms and skipped when it blocks is not a control.

## 4. Root cause

**Verifying one attribute of a candidate created false confidence in every other attribute of that candidate.**

I verified Vocal's *AI policy* against a primary source, marked the row `[P]`, and then treated the *economics* in the same row as though they carried the same grade. They did not — they were `[Reported]`, internally contradictory, and decisive.

The row-level evidence grade was the flaw. **Evidence grades belong to claims, not to rows.**

## 5. Corrective actions taken

1. **`missions/M-A_CLOSEOUT.md` marked WITHDRAWN** — retained, not deleted, with the error stated at the top.
2. **M-A status → REOPENED.** Vocal, Simily, Ream Stories, Pratilipi and Vocal Challenges return as live candidates.
3. **`PROJECT_STATE.md` §5 "central finding" struck through** and labelled withdrawn.
4. **New rule R15** (below).
5. **Downstream re-examination** — §6.

## 6. Downstream contamination review

Pre-committed in charter §5. Each artifact that leaned on the Class A finding:

| Artifact | Contaminated? | Action |
|---|---|---|
| **`SCOPE_INTEGRITY_CHECK.md`** class analysis | **Partly.** The A/B/C *framework* stands — it is definitional. The claim that "Class A is near-closed" is withdrawn | Framework kept; conclusion struck |
| **`M-C_CHARTER.md`** premise | **Yes.** It was chartered partly because Class A appeared closed | M-C already under audit A-002. Its charter must be re-justified against a live Class A |
| **`M-P_CHARTER.md`** / closeout | **No.** M-P was killed on institutional-substitution evidence, independent of Class A | Stands |
| **R9 "economics predicted policy" heuristic** | **Survives — but demoted.** The auditor tested it independently (Steemit, Hive, ScribbleHub, Tapas; Chinese web-novel platforms adopting AI then retreating with word caps and 104,000+ monthly rejections) and it held | **Demoted from law to tendency.** See R15. It was never licensed to *stop discovery* |
| **`WATCHLIST.md`** | **Yes.** Vocal/Tapas/Simily were filed as watchlist residue on the strength of a withdrawn conclusion | Promote back to active candidates |
| **`M1_OPPORTUNITY_FAMILIES.md`** | **Yes.** M-A was listed as concluded-negative | Re-open M-A's row |

## 7. What the audit confirms I got right

Recorded because a post-mortem that only lists failures is as distorted as one that only lists successes:

- I answered the **original** mission question rather than a substituted one.
- I caught my own Class B and Class C scope drift.
- The **cost-structure heuristic survived independent testing** — including a strong adopt-then-retreat signal from Chinese web-novel platforms that I had not seen.
- The auditor chased the Commonwealth Prize AI scandal expecting a counterexample and found the winners were **cleared** — and reported that against its own thesis.

**The failure was not the heuristic. It was promoting a tendency to a law, and letting the law license stopping.**

## 8. Honest assessment of the cost

Nothing irreversible happened. No money, no Owner time, no published asset, no discarded work. The audit cost one agent run and caught the error before any of it converted into action.

**But the counterfactual matters:** without the audit, this would have stood as a settled finding. A whole opportunity family — including the mission's own seed platform, at economics roughly **3× better than recorded**, with the seed platform's own free tier misread as a paywall — would have been closed permanently on a false premise, and nothing would ever have contradicted it.

That is exactly the invisible false negative R14 was written to catch. **R14 justified itself on its first use.**
