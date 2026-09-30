#!/usr/bin/env python3
"""Recoverable cleanup of an explicit, reviewed list of local legacy intermediates."""
import argparse
import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vfx_skills.runtime import atomic_json


def cleanup(plan_file, apply=False):
    plan = json.loads(plan_file.read_text())
    legacy = (ROOT / ".local/legacy").resolve()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    destination = Path.home() / ".Trash" / f"VFX-Skills-cleanup-{stamp}"
    operations = []
    for item in plan["targets"]:
        relative = Path(item["path"])
        source = legacy / relative
        if relative.is_absolute() or ".." in relative.parts or len(relative.parts) < 2:
            raise ValueError("Refusing broad or escaping cleanup target.")
        if source.is_symlink() or not source.exists() or not source.resolve().is_relative_to(legacy):
            raise ValueError("Cleanup target missing, symbolic or outside the legacy archive.")
        if not item.get("reason") or not item.get("verified_replacement"):
            raise ValueError("Every target needs a reason and verified recovery/replacement evidence.")
        operations.append({"source": str(source), "trash": str(destination / relative), **item})
    sources = [Path(item["source"]) for item in operations]
    if len(set(sources)) != len(sources) or any(a != b and a.is_relative_to(b) for a in sources for b in sources):
        raise ValueError("Overlapping or duplicate targets are not allowed.")
    receipt = {"applied": apply, "operations": operations, "completed": [],
               "note": "Recoverable in Trash; disk space not freed until Trash is emptied."}
    if apply:
        destination.mkdir(parents=True, exist_ok=False)
        report = ROOT / ".local/cleanup" / f"{stamp}.json"
        atomic_json(report, receipt)
        for item in operations:
            target = Path(item["trash"])
            target.parent.mkdir(parents=True, exist_ok=True)
            Path(item["source"]).rename(target)
            receipt["completed"].append(item["source"])
            atomic_json(report, receipt)
        atomic_json(destination / "RESTORE_RECEIPT.json", receipt)
        receipt["local_receipt"] = str(report)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(json.dumps(cleanup(args.plan, args.apply), indent=2))
