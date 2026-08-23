"""Lightweight portfolio Supervisor.

Answers three questions and nothing else:
  1. What is each project blocked on?
  2. How much expected value is waiting on a human?
  3. What is the nearest next step that does NOT depend on a human?

It does not schedule, dispatch, or execute. Its output is advisory, for people.
"""
from __future__ import annotations
from . import aggregate

HUMAN_BLOCKERS = {"HUMAN_APPROVAL", "HUMAN_ACTION"}


def report(sources: dict[str, str]) -> dict:
    """sources: {project_id: path}. Unreachable projects degrade, never crash."""
    projects, errors = {}, {}
    for pid, path in sources.items():
        try:
            projects[pid] = aggregate.load_project(path)
        except Exception as e:  # a missing project must not break the portfolio view
            errors[pid] = str(e)

    out = {"projects": {}, "portfolio": {}, "unreachable": errors}
    tot_rev = tot_cash = tot_cost = 0.0
    human_blocked = 0.0
    agent_actionable: list[dict] = []

    for pid, d in projects.items():
        fin = aggregate.financials(d["ledger"])
        blocked = aggregate.blocked_value(d["work_items"])
        pending_approvals = [a for a in d["approvals"].values() if a.get("decision") == "PENDING"]

        for b, slot in blocked.items():
            if b in HUMAN_BLOCKERS:
                human_blocked += slot["expected_value_usd"]

        for w in d["work_items"].values():
            if w.get("status") in ("PROPOSED", "ACTIVE"):
                agent_actionable.append({
                    "project": pid, "id": w.get("id"), "title": w.get("title"),
                    "expected_value_usd": w.get("expected_value_usd") or 0.0,
                })

        out["projects"][pid] = {
            "name": d["project"].get("name"),
            "integration_level": d["project"].get("integration_level"),
            "status": d["project"].get("status"),
            "financials": fin,
            "blocked_by": blocked,
            "pending_approvals": [
                {"id": a.get("id"), "gate_type": a.get("gate_type"), "request": a.get("request")}
                for a in pending_approvals
            ],
        }
        tot_rev += fin["recognised_revenue_usd"]
        tot_cash += fin["cash_received_usd"]
        tot_cost += fin["cost_usd"]

    agent_actionable.sort(key=lambda x: x["expected_value_usd"], reverse=True)
    out["portfolio"] = {
        "projects_reporting": len(projects),
        "recognised_revenue_usd": round(tot_rev, 2),
        "cash_received_usd": round(tot_cash, 2),
        "cost_usd": round(tot_cost, 2),
        "net_usd": round(tot_rev - tot_cost, 2),
        "expected_value_blocked_on_humans_usd": round(human_blocked, 2),
        "next_agent_actionable": agent_actionable[:5],
    }
    return out


def render(rep: dict) -> str:
    p = rep["portfolio"]
    L = ["=" * 62, "MONEY OS — PORTFOLIO STATUS", "=" * 62,
         f"projects reporting : {p['projects_reporting']}",
         f"recognised revenue : ${p['recognised_revenue_usd']:.2f}",
         f"cash received      : ${p['cash_received_usd']:.2f}",
         f"cost               : ${p['cost_usd']:.2f}",
         f"net                : ${p['net_usd']:.2f}",
         f"value blocked on humans: ${p['expected_value_blocked_on_humans_usd']:.2f}", ""]
    for pid, d in rep["projects"].items():
        L.append(f"--- {pid}  [{d['integration_level']}] {d['status']} — {d['name']}")
        f = d["financials"]
        L.append(f"    revenue ${f['recognised_revenue_usd']:.2f} / cash ${f['cash_received_usd']:.2f}"
                 f" / uncollected ${f['uncollected_usd']:.2f} / human {f['human_minutes']}min")
        if d["blocked_by"]:
            for b, s in sorted(d["blocked_by"].items(), key=lambda kv: -kv[1]["expected_value_usd"]):
                L.append(f"    BLOCKED {b:<16} n={s['count']}  ${s['expected_value_usd']:.2f}  {','.join(map(str,s['items']))}")
        for a in d["pending_approvals"]:
            L.append(f"    APPROVAL PENDING [{a['gate_type']}] {a['request']}")
        L.append("")
    if rep["unreachable"]:
        L.append("UNREACHABLE (portfolio view degrades, does not fail):")
        for pid, err in rep["unreachable"].items():
            L.append(f"    {pid}: {err}")
        L.append("")
    L.append("NEXT — highest expected value NOT blocked on a human:")
    if p["next_agent_actionable"]:
        for i in p["next_agent_actionable"]:
            L.append(f"    ${i['expected_value_usd']:>8.2f}  {i['project']}/{i['id']}  {i['title']}")
    else:
        L.append("    (none — every open item is waiting on a person)")
    L.append("=" * 62)
    return "\n".join(L)
