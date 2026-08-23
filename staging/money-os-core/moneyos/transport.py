"""Transport layer -- deliberately pluggable and outside the contract.

The contract defines what a RECORD looks like and what the outbox guarantees.
It says nothing about how records travel. Swapping transports must never
require a contract change or a change to any project's business code.

v0.1 ships FilesystemTransport as the reference implementation because it is
the easiest to debug and trivially satisfies "Money OS unavailable must not
break the business" -- there is nothing to be unavailable.

REST / queue / database-sync / CLI / Git transports can be added by
implementing the same three methods. Git is explicitly NOT privileged here:
it is one possible transport, not an architectural dependency.
"""
from __future__ import annotations
import os
from . import contract


class Transport:
    """Interface. flush() is allowed to fail forever without affecting callers."""

    def emit(self, outbox: str, kind: str, rec: dict) -> dict:
        raise NotImplementedError

    def flush(self, outbox: str) -> tuple[int, str]:
        """Best-effort delivery. Returns (records_pending, human-readable status).

        MUST NOT raise on unavailability. MUST NOT block the business path.
        """
        raise NotImplementedError

    def read(self, source: str, kind: str) -> list[dict]:
        raise NotImplementedError


class FilesystemTransport(Transport):
    """Reference transport: the outbox IS the delivery surface.

    Money OS reads project outboxes directly from a path it can see. There is
    no push step, therefore no failure mode and no queue backlog.
    """

    def emit(self, outbox: str, kind: str, rec: dict) -> dict:
        return contract.emit(outbox, kind, rec)

    def flush(self, outbox: str) -> tuple[int, str]:
        return (0, "filesystem transport: nothing to flush, outbox is the delivery surface")

    def read(self, source: str, kind: str) -> list[dict]:
        return contract.read(source, kind)


class NullTransport(Transport):
    """Money OS is unavailable. Records still land locally; nothing is delivered.

    Exists to make the guarantee testable: a project running against
    NullTransport must behave identically from the business system's point of
    view. See tests/test_offline.py.
    """

    def emit(self, outbox: str, kind: str, rec: dict) -> dict:
        return contract.emit(outbox, kind, rec)

    def flush(self, outbox: str) -> tuple[int, str]:
        pending = sum(len(contract.read(outbox, k)) for k in contract.KINDS)
        return (pending, f"money os unavailable: {pending} record(s) queued locally, will sync later")

    def read(self, source: str, kind: str) -> list[dict]:
        raise ConnectionError("money os unavailable")
