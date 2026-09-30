#!/usr/bin/env python3
"""Backed-up migration of local Python path literals and simple shell entry paths.

Does not rewrite evidence, binary assets, nested repositories, caches or arbitrary shell commands.
"""
import argparse
import ast
import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tokenize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vfx_skills.runtime import atomic_json

EXCLUDE = {"hfcache", "node_modules", ".git", "__pycache__", ".venv", "venv"}


def transform_python(text, old, new):
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    edits = []
    for token in tokenize.generate_tokens(io.StringIO(text).readline):
        if token.type != tokenize.STRING or old not in token.string:
            continue
        try:
            value = ast.literal_eval(token.string)
        except (SyntaxError, ValueError):
            continue
        # Pure path literals only. Embedded scripts/commands require manual inspection.
        if isinstance(value, str) and (value == old or value.startswith(old + "/")) and "\n" not in value:
            if any(c in value for c in (";", "|", "$", "`")):
                continue
            start = offsets[token.start[0] - 1] + token.start[1]
            end = offsets[token.end[0] - 1] + token.end[1]
            edits.append((start, end, repr(new + value[len(old):])))
    for start, end, replacement in reversed(edits):
        text = text[:start] + replacement + text[end:]
    ast.parse(text)
    return text


def transform_shell(text, old, new):
    # Existing quoted path occurrences remain quoted; quote only bare cd/export paths.
    text = re.sub(r'(["\'])' + re.escape(old) + r'([^"\'\n]*)\1',
                  lambda m: m[1] + new + m[2] + m[1], text)
    text = re.sub(r'\bcd ' + re.escape(old) + r'([A-Za-z0-9_./-]*)(?=\s|$)',
                  lambda m: 'cd "' + new + m[1] + '"', text)
    text = re.sub(r'(\bexport [A-Z_]+=)' + re.escape(old) + r'([A-Za-z0-9_./-]*)(?=\s|$)',
                  lambda m: m[1] + '"' + new + m[2] + '"', text)
    result = subprocess.run(["/bin/zsh", "-n"], input=text, text=True, capture_output=True)
    if result.returncode:
        raise ValueError("Shell syntax check failed; not modifying source.")
    return text


def migrate(old_root, apply=False):
    legacy = ROOT / ".local/legacy"
    if not legacy.is_dir() or legacy.is_symlink():
        raise ValueError("Need an actual local legacy directory.")
    old = str(old_root).rstrip("/")
    new = str(legacy.resolve())
    changes, remaining, skipped = [], [], []
    patches = []
    for folder in (legacy / "pipeline", legacy / "engine"):
        for path in sorted(folder.rglob("*")):
            if path.suffix not in {".py", ".sh"} or path.is_symlink() or any(p in EXCLUDE for p in path.relative_to(legacy).parts):
                continue
            text = path.read_text()
            if old not in text:
                continue
            try:
                updated = transform_python(text, old, new) if path.suffix == ".py" else transform_shell(text, old, new)
            except (SyntaxError, tokenize.TokenError, ValueError):
                skipped.append(str(path.relative_to(legacy)))
                continue
            if old in updated:
                remaining.append(str(path.relative_to(legacy)))
            if updated != text:
                patches.append((path, text, updated))
                changes.append({"path": str(path.relative_to(legacy)),
                                "before_sha256": hashlib.sha256(text.encode()).hexdigest(),
                                "after_sha256": hashlib.sha256(updated.encode()).hexdigest()})
    receipt = {"old_root": old, "new_root": new, "applied": apply, "changes": changes,
               "remaining_manual_review": remaining, "skipped_invalid_source": skipped}
    if apply:
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = ROOT / ".local/path-migration" / stamp
        backup.mkdir(parents=True, exist_ok=False)
        receipt["backup_root"] = str(backup)
        atomic_json(backup / "receipt.json", receipt)
        for path, before, after in patches:
            saved = backup / path.relative_to(legacy)
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_text(before)
            path.write_text(after)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-root", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    result = migrate(args.old_root, args.apply)
    print(json.dumps(result, indent=2))
