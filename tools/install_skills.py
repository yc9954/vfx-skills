#!/usr/bin/env python3
"""Link only this repository's registered skills; back up existing copies first."""
import argparse
import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vfx_skills.catalog import validate
from vfx_skills.runtime import atomic_json


def install(destination, apply=False):
    if not validate()["passed"]:
        raise ValueError("Fix skill validation before installation.")
    destination = destination.expanduser().resolve()
    if destination == ROOT or destination.is_relative_to(ROOT):
        raise ValueError("Install destination must be outside this repository.")
    names = json.loads((ROOT / "config/workflow.json").read_text())["skills"]
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup = ROOT / ".local/skill-backups" / stamp
    operations = []
    for name in names:
        target = destination / name
        source = ROOT / "skills" / name
        if target.is_symlink() and target.resolve() == source:
            continue
        operations.append({"target": str(target), "source": str(source),
                           "backup": str(backup / name) if target.exists() or target.is_symlink() else None})
    if apply:
        destination.mkdir(parents=True, exist_ok=True)
        backup.mkdir(parents=True, exist_ok=False)
        receipt = {"operations": operations, "completed": []}
        atomic_json(backup / "receipt.json", receipt)
        for item in operations:
            target = Path(item["target"])
            if item["backup"]:
                target.rename(item["backup"])
            target.symlink_to(item["source"], target_is_directory=True)
            receipt["completed"].append(item["target"])
            atomic_json(backup / "receipt.json", receipt)
    return {"applied": apply, "operations": operations}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=Path.home() / ".codex/skills")
    parser.add_argument("--apply", action="store_true", help="Without this, only print the plan")
    args = parser.parse_args()
    print(json.dumps(install(args.destination, args.apply), indent=2))
