#!/usr/bin/env python3
"""M1 -> Money OS contract adapter.

THIN ADAPTER. Lives in M1, not in Money OS. Money OS never imports M1 code.

M1's ledger/*.csv remain the source of truth; .moneyos/ is a derived export
that can be regenerated or deleted at any time with zero effect on M1.
"""
from __future__ import annotations
import csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTBOX = os.path.join(ROOT, ".moneyos")
sys.path.insert(0, os.path.join(ROOT, "staging", "money-os-core"))
from moneyos import contract  # noqa: E402

# M1's own status vocabulary -> contract (status, blocked_by).
# This table IS the compatibility test: every M1 status must land somewhere real.
STATUS_MAP = {
    "ASSET_READY_PENDING_H2":          ("BLOCKED", "HUMAN_APPROVAL"),
    "BLOCKED_BY_AUTHOR_ELIGIBILITY":   ("BLOCKED", "ELIGIBILITY"),
    "ACCOUNT_PAYMENT_GATE":            ("BLOCKED", "HUMAN_ACTION"),
    "POLICY_VERIFIED_ACCOUNT_GATE":    ("BLOCKED", "HUMAN_ACTION"),
    "BLOCKED_BY_STORE_PREREQUISITE":   ("BLOCKED", "PREREQUISITE"),
    "POLICY_UNVERIFIED":               ("BLOCKED", "POLICY_UNKNOWN"),
    "READY_TO_START_AFTER_FIRST_GATE": ("BLOCKED", "PREREQUISITE"),
}


def _rows(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get(list(r.keys())[0], "").strip()
                and not list(r.values())[0].startswith("#")]


def _num(v, default=None):
    if v is None:
        return default
    m = re.search(r"-?\d+(?:\.\d+)?", str(v).replace(",", ""))
    return float(m.group()) if m else default


def export():
    if os.path.isdir(OUTBOX):
        for fn in os.listdir(OUTBOX):
            os.remove(os.path.join(OUTBOX, fn))
    os.makedirs(OUTBOX, exist_ok=True)
    unmapped = []

    contract.emit(OUTBOX, "project", {
        "project_id": "m1-autopublishing",
        "name": "M1 Digital Asset & Publishing Factory",
        "integration_level": "L2",
        "status": "ACTIVE",
        "base_currency": "USD",
        "repo_url": "https://github.com/fcubeve-alt/project-m1-autopublishing",
    })

    # opportunities -> work_items
    for r in _rows("ledger/OPPORTUNITIES.csv"):
        raw = (r.get("status") or "").strip()
        status, blocked = STATUS_MAP.get(raw, (None, None))
        if status is None:
            unmapped.append(raw)
            status, blocked = "PROPOSED", None
        contract.emit(OUTBOX, "work_item", {
            "id": r["opportunity_id"],
            "kind": "opportunity",
            "title": f"{r.get('platform','')} — {r.get('opportunity_type','')}".strip(" —"),
            "status": status,
            "blocked_by": blocked,
            "blocked_detail": (r.get("eligibility") or "")[:300] or None,
            "expected_value_usd": _num(r.get("expected_revenue_usd"), None),
            "expected_cost_usd": _num(r.get("expected_cost_usd"), 0.0),
            "human_minutes_spent": 0,
        })

    # revenue + cost -> ledger
    for r in _rows("ledger/REVENUE_LEDGER.csv"):
        contract.emit(OUTBOX, "ledger_entry", {
            "id": r["entry_id"], "direction": "REVENUE", "date": r["date"],
            "category": r.get("event_type"), "counterparty": r.get("platform"),
            "work_item_id": None,
            "gross_usd": _num(r.get("gross_revenue_usd"), 0.0),
            "fees_usd": _num(r.get("platform_fee_usd"), 0.0),
            "net_usd": _num(r.get("net_royalty_usd"), 0.0) or 0.0,
            "cash_received_usd": _num(r.get("payout_received_usd"), 0.0),
            "cash_received_at": None,
            "human_minutes": int(_num(r.get("human_minutes"), 0) or 0),
            "note": (r.get("notes") or "")[:300],
        })
    for r in _rows("ledger/COST_LEDGER.csv"):
        amt = _num(r.get("amount_usd"), 0.0) or 0.0
        contract.emit(OUTBOX, "ledger_entry", {
            "id": r["entry_id"], "direction": "COST", "date": r["date"],
            "category": r.get("category"), "counterparty": None, "work_item_id": None,
            "gross_usd": amt, "fees_usd": 0.0, "net_usd": amt,
            "cash_received_usd": 0.0, "cash_received_at": None,
            "human_minutes": int(_num(r.get("human_minutes"), 0) or 0),
            "note": (r.get("description") or "")[:300],
        })

    # human gates -> approvals (from PROJECT_STATE section 7, hand-mapped)
    for a in [
        {"id": "APR-H1", "work_item_id": "OPP-002", "gate_type": "IDENTITY_KYC",
         "request": "Owner country of tax residence / payout rails (H1)",
         "risk_note": "Gates Listverse submission access and Vocal publishing", "decision": "PENDING"},
        {"id": "APR-H2", "work_item_id": "OPP-001", "gate_type": "EXTERNAL_COMMUNICATION",
         "request": "Approve and send Cracked pitch from Owner mailbox (H2)",
         "risk_note": "Represents Owner identity externally; irreversible once sent", "decision": "PENDING"},
    ]:
        a["amount_usd"] = 0.0
        contract.emit(OUTBOX, "approval", a)

    # decision log -> decisions
    dl = os.path.join(ROOT, "ledger", "DECISION_LOG.md")
    if os.path.exists(dl):
        text = open(dl, encoding="utf-8").read()
        seen = set()
        for m in re.finditer(r"\b(D\d{4})\b[^\n]*", text):
            did = m.group(1)
            if did in seen:
                continue
            seen.add(did)
            contract.emit(OUTBOX, "decision", {
                "id": did,
                "title": m.group(0).strip()[:160],
                "choice": "see ledger/DECISION_LOG.md",
                "rejected_alternatives": [],
                "rationale": None, "evidence_refs": [], "reversible": None,
                "outcome": None,
            })

    # submissions -> events
    for r in _rows("ledger/SUBMISSIONS.csv"):
        contract.emit(OUTBOX, "event", {
            "id": r["submission_id"], "type": "SUBMISSION_SENT",
            "work_item_id": None,
            "payload": {"platform": r.get("platform"), "status": r.get("status")},
        })

    counts = {k: len(contract.read(OUTBOX, k)) for k in contract.KINDS}
    return counts, unmapped


if __name__ == "__main__":
    counts, unmapped = export()
    print("exported:", json.dumps(counts))
    if unmapped:
        print("!! UNMAPPED M1 STATUSES (contract gap):", sorted(set(unmapped)))
        sys.exit(2)
    print("all M1 statuses mapped cleanly")
