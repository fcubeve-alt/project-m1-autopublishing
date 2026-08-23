"""The guarantee that matters: Money OS unavailable must not break a business.

If these fail, the architecture is wrong -- not the test.
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from moneyos import contract, transport, supervisor


def test_business_continues_when_moneyos_is_down():
    """A project records normally against a dead Money OS."""
    t = transport.NullTransport()
    with tempfile.TemporaryDirectory() as d:
        t.emit(d, "project", {"project_id": "x", "name": "X",
                              "integration_level": "L1", "status": "ACTIVE"})
        for i in range(3):
            t.emit(d, "ledger_entry", {"id": f"L{i}", "direction": "REVENUE",
                                       "date": "2026-08-16", "net_usd": 10.0})
        pending, msg = t.flush(d)          # never raises
        assert pending == 4, pending
        assert "queued locally" in msg
        assert len(contract.read(d, "ledger_entry")) == 3
    print("PASS business continues while Money OS is unavailable")


def test_emit_does_no_network_io():
    """contract.emit must be a pure local write -- no socket module use."""
    src = open(os.path.join(os.path.dirname(__file__), "..", "moneyos", "contract.py")).read()
    for banned in ("import socket", "import requests", "urllib.request", "http.client"):
        assert banned not in src, f"contract.py must not perform network I/O: found {banned}"
    print("PASS contract.emit performs no network I/O")


def test_append_only_last_write_wins():
    with tempfile.TemporaryDirectory() as d:
        contract.emit(d, "work_item", {"id": "W1", "kind": "task", "title": "t",
                                       "status": "ACTIVE", "recorded_at": "2026-01-01T00:00:00Z"})
        contract.emit(d, "work_item", {"id": "W1", "kind": "task", "title": "t",
                                       "status": "DONE", "recorded_at": "2026-02-01T00:00:00Z"})
        assert len(contract.read(d, "work_item")) == 2, "history must be preserved"
        assert contract.current(contract.read(d, "work_item"))["W1"]["status"] == "DONE"
    print("PASS append-only history preserved, last write wins")


def test_blocked_requires_reason():
    with tempfile.TemporaryDirectory() as d:
        try:
            contract.emit(d, "work_item", {"id": "W2", "kind": "task", "title": "t",
                                           "status": "BLOCKED"})
        except contract.ContractError:
            print("PASS BLOCKED without blocked_by is rejected")
            return
        raise AssertionError("BLOCKED without blocked_by should be rejected")


def test_portfolio_degrades_not_fails_on_unreachable_project():
    rep = supervisor.report({"ghost": "/nonexistent/path"})
    assert rep["unreachable"], "unreachable project must be reported"
    assert rep["portfolio"]["projects_reporting"] == 0
    print("PASS portfolio view degrades instead of failing")


if __name__ == "__main__":
    for fn in [test_business_continues_when_moneyos_is_down, test_emit_does_no_network_io,
               test_append_only_last_write_wins, test_blocked_requires_reason,
               test_portfolio_degrades_not_fails_on_unreachable_project]:
        fn()
    print("\nall offline-guarantee tests passed")
