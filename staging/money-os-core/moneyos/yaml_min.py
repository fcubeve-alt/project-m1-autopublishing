"""Minimal YAML subset reader for registry.yaml -- avoids a PyYAML dependency.

Supports exactly what the registry needs: a top-level key holding a list of
flat string maps. Anything more complex should move the registry to JSON.
"""
from __future__ import annotations


def load(text: str) -> dict:
    root: dict = {}
    cur_list = None
    cur_item = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        s = line.strip()
        if indent == 0 and s.endswith(":"):
            cur_list = []
            root[s[:-1].strip()] = cur_list
            cur_item = None
        elif s.startswith("- "):
            cur_item = {}
            if cur_list is None:
                cur_list = []
                root.setdefault("projects", cur_list)
            cur_list.append(cur_item)
            s = s[2:].strip()
            if ":" in s:
                k, v = s.split(":", 1)
                cur_item[k.strip()] = _scalar(v.strip())
        elif cur_item is not None and ":" in s:
            k, v = s.split(":", 1)
            cur_item[k.strip()] = _scalar(v.strip())
    return root


def _scalar(v: str):
    v = v.strip().strip('"').strip("'")
    if v in ("null", "~", ""):
        return None
    if v in ("true", "false"):
        return v == "true"
    return v
