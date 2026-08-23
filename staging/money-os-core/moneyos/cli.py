"""moneyos CLI — validate / status."""
from __future__ import annotations
import argparse, json, os, sys
from . import yaml_min
from . import contract, supervisor


def _registry(path: str) -> dict:
    return yaml_min.load(open(path, encoding="utf-8").read())


def cmd_validate(args) -> int:
    bad = 0
    for kind in contract.KINDS:
        for rec in contract.read(args.outbox, kind):
            try:
                contract.validate(kind, rec)
            except contract.ContractError as e:
                print(f"FAIL {e}"); bad += 1
    print("INVALID: %d record(s)" % bad if bad else "OK — all records satisfy contract v" + contract.CONTRACT_VERSION)
    return 1 if bad else 0


def cmd_status(args) -> int:
    reg = _registry(args.registry)
    base = os.path.dirname(os.path.abspath(args.registry))
    sources = {p["project_id"]: os.path.normpath(os.path.join(base, p["source"]))
               for p in reg.get("projects", []) if p.get("source")}
    rep = supervisor.report(sources)
    print(json.dumps(rep, indent=2, ensure_ascii=False) if args.json else supervisor.render(rep))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="moneyos")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="validate one project outbox")
    v.add_argument("outbox"); v.set_defaults(fn=cmd_validate)
    s = sub.add_parser("status", help="portfolio status")
    s.add_argument("--registry", default="projects/registry.yaml")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_status)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
