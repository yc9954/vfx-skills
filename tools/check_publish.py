#!/usr/bin/env python3
"""Audit the Git INDEX, not the working tree. No secrets or large assets in commits."""
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"src", "skills", "config", "examples", "docs", "tests", "tools", ".github"}
ROOT_FILES = {"README.md", "AGENTS.md", "NOTICE.md", "pyproject.toml", "vfx.py", ".gitignore", ".gitattributes"}
RULES = {
    "private_key": rb"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
    "provider_token": rb"\b(?:hf_|tsk_|ghp_|github_pat_|sk-proj-)[A-Za-z0-9_-]{20,}",
    "signed_url": rb"[?&](?:X-Amz-Signature|Signature|access_token)=[A-Za-z0-9%_-]{20,}",
    "machine_path": rb"/Users/[A-Za-z0-9_.-]+/|C:\\\\Users\\\\",
}


def violations(path, data, mode="100644"):
    failures = []
    parts = Path(path).parts
    if not parts or (len(parts) == 1 and path not in ROOT_FILES) or (len(parts) > 1 and parts[0] not in ALLOWED):
        failures.append("non-source path")
    if any(part in {".local", ".secrets", "node_modules", "__pycache__"} or part.startswith(".env") for part in parts):
        failures.append("private/cache path")
    if mode not in {"100644", "100755"}:
        failures.append("symlink/submodule is not publishable")
    if len(data) > 5 * 1024 * 1024:
        failures.append("file exceeds 5 MiB")
    if b"\0" in data:
        failures.append("binary file")
    for name, pattern in RULES.items():
        if re.search(pattern, data):
            failures.append(name)
    return failures


def audit():
    output = subprocess.check_output(["git", "ls-files", "--stage", "-z"], cwd=ROOT)
    failures = []
    count = total = 0
    for record in output.split(b"\0"):
        if not record:
            continue
        meta, name = record.split(b"\t", 1)
        mode, oid, stage = meta.decode().split()
        path = name.decode()
        if stage != "0":
            failures.append({"path": path, "rules": ["unmerged index"]})
            continue
        data = subprocess.check_output(["git", "cat-file", "blob", oid], cwd=ROOT) if mode != "160000" else b""
        count += 1
        total += len(data)
        found = violations(path, data, mode)
        if found:
            failures.append({"path": path, "rules": found})
    return {"passed": bool(count) and not failures, "files": count, "bytes": total, "failures": failures}


if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
