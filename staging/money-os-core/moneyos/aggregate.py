"""Read-only cross-project aggregation. Money OS never writes to a project."""
from __future__ import annotations
from . import contract


def load_project(source: str) -> dict:
    """Load one project's contract surface from a source path."""
    proj = contract.read(source, "project")
    if not proj:
        raise FileNotFoundError(f"no project.json at {source}")
    p = proj[0]
    return {
        "project": p,
        "work_items": contract.current(contract.read(source, "work_item")),
        "approvals": contract.current(contract.read(source, "approval")),
        "ledger": contract.read(source, "ledger_entry"),
        "decisions": contract.current(contract.read(source, "decision")),
        "events": contract.read(source, "event"),
    }


def financials(ledger: list[dict]) -> dict:
    """Recognised revenue and cash received are reported separately, always."""
    rev = sum(e.get("net_usd", 0) or 0 for e in ledger if e.get("direction") == "REVENUE")
    cost = sum(abs(e.get("net_usd", 0) or 0) for e in ledger if e.get("direction") == "COST")
    cash = sum(e.get("cash_received_usd", 0) or 0 for e in ledger)
    minutes = sum(e.get("human_minutes", 0) or 0 for e in ledger)
    return {
        "recognised_revenue_usd": round(rev, 2),
        "cost_usd": round(cost, 2),
        "net_usd": round(rev - cost, 2),
        "cash_received_usd": round(cash, 2),
        "uncollected_usd": round(rev - cash, 2),
        "human_minutes": minutes,
    }


def blocked_value(work_items: dict) -> dict:
    """Group expected value by what it is blocked on.

    This is the single most useful portfolio number: how much expected value is
    waiting on a human, and therefore cannot be unblocked by more agent work.
    """
    out: dict[str, dict] = {}
    for w in work_items.values():
        if w.get("status") != "BLOCKED":
            continue
        b = w.get("blocked_by") or "UNSPECIFIED"
        slot = out.setdefault(b, {"count": 0, "expected_value_usd": 0.0, "items": []})
        slot["count"] += 1
        slot["expected_value_usd"] += w.get("expected_value_usd") or 0.0
        slot["items"].append(w.get("id"))
    for slot in out.values():
        slot["expected_value_usd"] = round(slot["expected_value_usd"], 2)
    return out
