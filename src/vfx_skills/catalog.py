from __future__ import annotations

import re
import shutil
from pathlib import Path
from urllib.parse import unquote

from .runtime import root, read_json


def route(backend: str, stage: str, specialists=()):
    config = read_json(root() / "config/workflow.json")
    try:
        selected = list(config["routes"][backend][stage])
    except KeyError as exc:
        raise ValueError(f"Unsupported route: {backend}/{stage}; do not silently change backend.") from exc
    for name in specialists:
        if name not in config["specialists"]:
            raise ValueError(f"Unknown specialist: {name}")
        selected.append(config["specialists"][name])
    return {"backend": backend, "stage": stage, "skills": list(dict.fromkeys(selected))}


def validate():
    base = root()
    config = read_json(base / "config/workflow.json")
    failures = []
    for name in config["skills"]:
        path = base / "skills" / name / "SKILL.md"
        if not path.is_file():
            failures.append(f"Missing skill: {name}")
            continue
        text = path.read_text()
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            failures.append(f"Invalid frontmatter: {name}")
            continue
        header = text.split("---", 2)[1]
        if f"name: {name}\n" not in header or not re.search(r"^description: .+", header, re.M):
            failures.append(f"Invalid skill metadata: {name}")
        if not (path.parent / "agents/openai.yaml").is_file():
            failures.append(f"Missing agent metadata: {name}")
    for doc in (base / "skills").rglob("*.md"):
        for link in re.findall(r"\]\(([^\s)]+)\)", doc.read_text()):
            if re.match(r"(?:[a-zA-Z]+:|#)", link):
                continue
            target = unquote(link.split("#", 1)[0])
            if target and not (doc.parent / target).exists():
                failures.append(f"{doc.relative_to(base)}: missing {target}")
    for stages in config["routes"].values():
        for names in stages.values():
            for name in names:
                if name not in config["skills"]:
                    failures.append(f"Unknown routed skill: {name}")
    return {"skills": len(config["skills"]), "passed": not failures, "failures": failures}


def doctor():
    import os
    tools = {name: shutil.which(name) for name in ("higgsfield", "ffmpeg", "ffprobe", "gh")}
    blender = os.environ.get("VFX_BLENDER") or shutil.which("blender")
    if not blender:
        for directory in (Path.home() / "Applications", Path("/Applications")):
            found = sorted(directory.glob("Blender*.app/Contents/MacOS/Blender"))
            if found:
                blender = str(found[-1])
                break
    tools["blender"] = blender
    return {"root": str(root()), "tools": tools, "skill_validation": validate(),
            "legacy_present": (root() / ".local/legacy").is_dir(),
            "gpu_verified": False, "authentication_verified": False,
            "note": "Installation discovery only; no login, GPU job, upload or generation."}
