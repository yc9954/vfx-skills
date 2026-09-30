from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path


def root() -> Path:
    candidate = Path(os.environ.get("VFX_SKILLS_ROOT", Path(__file__).resolve().parents[2]))
    if not (candidate / "config/workflow.json").is_file():
        raise ValueError("Run from the source checkout or set VFX_SKILLS_ROOT to it.")
    return candidate.resolve()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_new(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def atomic_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".vfx-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def local_run(name: str) -> Path:
    import re
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,79}", name):
        raise ValueError("Run ID must be a short lowercase slug, never a path.")
    base = root() / ".local/runs"
    path = base / name
    if path.is_symlink() or not path.resolve().is_relative_to((root() / ".local").resolve()):
        raise ValueError("Run escapes the local workspace.")
    return path
