from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import catalog, jobs


def main():
    parser = argparse.ArgumentParser(description="VFX Skills: explicit stages, local evidence, no implicit generation")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Read-only tool/path discovery")
    skills = commands.add_parser("skills")
    skills.add_argument("action", choices=["validate"])
    route = commands.add_parser("route", help="Select only the current workflow stage")
    route.add_argument("backend", choices=["blender", "higgsfield", "hybrid"])
    route.add_argument("stage")
    route.add_argument("--specialist", action="append", default=[])
    job = commands.add_parser("job").add_subparsers(dest="action", required=True)
    prepare = job.add_parser("prepare")
    prepare.add_argument("run")
    prepare.add_argument("request", type=Path)
    for action in ("quote", "status", "submit", "approve"):
        command = job.add_parser(action)
        command.add_argument("run")
        if action == "submit":
            command.add_argument("--execute", action="store_true")
        if action == "approve":
            command.add_argument("--cap", type=float, required=True)
            command.add_argument("--source", required=True, help="Exact source of an existing user approval; not self-authorization")
    args = parser.parse_args()
    try:
        if args.command == "doctor":
            result = catalog.doctor()
        elif args.command == "skills":
            result = catalog.validate()
        elif args.command == "route":
            result = catalog.route(args.backend, args.stage, args.specialist)
        elif args.action == "prepare":
            result = jobs.prepare(args.request.resolve(), args.run)
        elif args.action == "approve":
            result = jobs.approve(args.run, args.cap, args.source)
        elif args.action == "submit":
            result = jobs.submit(args.run, args.execute)
        else:
            result = getattr(jobs, args.action)(args.run)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result.get("passed") is False else 0
    except (ValueError, KeyError, OSError, RuntimeError) as exc:
        parser.exit(2, f"vfx: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
