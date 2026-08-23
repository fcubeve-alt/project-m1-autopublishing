"""Contract objects: validation and local-first outbox I/O.

Transport-agnostic. This module knows how to WRITE records locally and READ them
back. It does not know how they travel to Money OS -- see transport.py.
"""
from __future__ import annotations
import json, os, datetime
from typing import Iterable, Iterator

CONTRACT_VERSION = "0.1"

KINDS = ("project", "work_item", "approval", "ledger_entry", "decision", "event")

_FILENAME = {
    "project": "project.json",
    "work_item": "work_items.ndjson",
    "approval": "approvals.ndjson",
    "ledger_entry": "ledger.ndjson",
    "decision": "decisions.ndjson",
    "event": "events.ndjson",
}

WORK_STATUS = {"PROPOSED", "ACTIVE", "BLOCKED", "DONE", "ABANDONED"}
BLOCKED_BY = {"HUMAN_APPROVAL", "HUMAN_ACTION", "EXTERNAL_PARTY", "POLICY_UNKNOWN",
              "ELIGIBILITY", "PREREQUISITE", "CAPABILITY", "FUNDS"}
GATE_TYPE = {"SPEND", "IRREVERSIBLE", "IDENTITY_KYC", "LEGAL_CONTRACT",
             "EXTERNAL_COMMUNICATION", "PUBLISH", "POLICY_UNCLEAR", "IP_RISK"}
DECISION = {"PENDING", "APPROVED", "REJECTED", "WITHDRAWN"}
DIRECTION = {"REVENUE", "COST"}
LEVELS = {"L0", "L1", "L2"}
PROJECT_STATUS = {"ACTIVE", "PAUSED", "BLOCKED", "CLOSED"}

_REQUIRED = {
    "project": ("contract_version", "project_id", "name", "integration_level", "status", "recorded_at"),
    "work_item": ("id", "kind", "title", "status", "recorded_at"),
    "approval": ("id", "gate_type", "request", "decision", "recorded_at"),
    "ledger_entry": ("id", "direction", "date", "net_usd", "recorded_at"),
    "decision": ("id", "title", "choice", "recorded_at"),
    "event": ("id", "type", "recorded_at"),
}


class ContractError(ValueError):
    """A record does not satisfy the contract."""


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def validate(kind: str, rec: dict) -> None:
    """Raise ContractError if rec is invalid. Unknown fields are always allowed."""
    if kind not in KINDS:
        raise ContractError(f"unknown kind: {kind}")
    for f in _REQUIRED[kind]:
        if rec.get(f) in (None, ""):
            raise ContractError(f"{kind}: missing required field '{f}'")

    if kind == "project":
        if rec["integration_level"] not in LEVELS:
            raise ContractError(f"project: integration_level must be one of {sorted(LEVELS)}")
        if rec["status"] not in PROJECT_STATUS:
            raise ContractError(f"project: status must be one of {sorted(PROJECT_STATUS)}")
    elif kind == "work_item":
        if rec["status"] not in WORK_STATUS:
            raise ContractError(f"work_item {rec['id']}: status must be one of {sorted(WORK_STATUS)}")
        if rec["status"] == "BLOCKED":
            b = rec.get("blocked_by")
            if not b:
                raise ContractError(f"work_item {rec['id']}: blocked_by is required when status=BLOCKED")
            if b not in BLOCKED_BY:
                raise ContractError(f"work_item {rec['id']}: blocked_by '{b}' not in {sorted(BLOCKED_BY)}")
    elif kind == "approval":
        if rec["gate_type"] not in GATE_TYPE:
            raise ContractError(f"approval {rec['id']}: gate_type '{rec['gate_type']}' invalid")
        if rec["decision"] not in DECISION:
            raise ContractError(f"approval {rec['id']}: decision '{rec['decision']}' invalid")
    elif kind == "ledger_entry":
        if rec["direction"] not in DIRECTION:
            raise ContractError(f"ledger {rec['id']}: direction must be REVENUE or COST")
        if not isinstance(rec["net_usd"], (int, float)):
            raise ContractError(f"ledger {rec['id']}: net_usd must be numeric")


def emit(outbox: str, kind: str, rec: dict) -> dict:
    """Record locally. MUST succeed locally and return immediately.

    This is the only write path a project business system ever touches.
    It performs no network I/O by design -- Money OS being unavailable
    cannot affect the caller.
    """
    rec.setdefault("recorded_at", now())
    if kind == "project":
        rec.setdefault("contract_version", CONTRACT_VERSION)
    validate(kind, rec)
    os.makedirs(outbox, exist_ok=True)
    path = os.path.join(outbox, _FILENAME[kind])
    if kind == "project":
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=2)
            f.write("\n")
    else:
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def read(outbox: str, kind: str) -> list[dict]:
    """Read records of one kind. Returns [] when the file is absent."""
    path = os.path.join(outbox, _FILENAME[kind])
    if not os.path.exists(path):
        return []
    if kind == "project":
        with open(path, encoding="utf-8") as f:
            return [json.load(f)]
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def current(records: Iterable[dict]) -> dict[str, dict]:
    """Collapse an append-only stream to current state: last write per id wins."""
    latest: dict[str, dict] = {}
    for r in records:
        rid = r.get("id")
        if rid is None:
            continue
        prev = latest.get(rid)
        if prev is None or str(r.get("recorded_at", "")) >= str(prev.get("recorded_at", "")):
            latest[rid] = r
    return latest
