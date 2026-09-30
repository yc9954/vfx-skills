"""Small, local, one-attempt Higgsfield adapter. Never uploads or retries."""
from __future__ import annotations

import datetime as dt
import json
import math
import re
import shutil
import subprocess
import uuid
from pathlib import Path

from .runtime import atomic_json, digest, file_hash, local_run, read_json, root, write_new

PARAMS = {"mode", "duration", "resolution", "aspect_ratio", "generate_audio", "prompt"}
MEDIA = {"image-references", "video-references", "audio-references", "start-image", "end-image"}
REQUEST_KEYS = {"schema", "model", "params", "media", "local_inputs", "delivery"}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise ValueError("Expected a finite, positive credit amount.")
    return value


def identifier(value):
    return str(uuid.UUID(value))


def validate_request(request):
    if set(request) - REQUEST_KEYS:
        raise ValueError("Unknown request fields; put project notes in the project record.")
    if request.get("schema") != 1 or not re.fullmatch(r"[a-z][a-z0-9_]{1,79}", request.get("model", "")):
        raise ValueError("Invalid request schema or model ID.")
    params = request.get("params", {})
    if not params or set(params) - PARAMS or not isinstance(params.get("prompt"), str) or not params["prompt"].strip():
        raise ValueError("Unsupported parameters or missing prompt. Inspect the current model schema first.")
    for value in params.values():
        if not isinstance(value, (str, int, float, bool)) or isinstance(value, float) and not math.isfinite(value):
            raise ValueError("Parameters must be finite scalar values.")
    for item in request.get("media", []):
        if item.get("flag") not in MEDIA:
            raise ValueError("Unsupported media flag.")
        identifier(item["id"])  # Paths/URLs are rejected: cost also auto-uploads local paths.
    for item in request.get("local_inputs", []):
        if not re.fullmatch(r"[a-f0-9]{64}", item.get("sha256", "")):
            raise ValueError("Input must include its SHA-256.")
        path = input_path(item)
        if not path.is_absolute() or not path.is_file() or file_hash(path) != item["sha256"]:
            raise ValueError("A local input is missing or changed.")
    return request


def input_path(item):
    path = Path(item["path"])
    if item.get("base") == "workspace":
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Workspace input must be a relative path.")
        path = (root() / path).resolve()
        if not path.is_relative_to(root()):
            raise ValueError("Workspace input escapes the repository.")
    elif item.get("base", "absolute") != "absolute":
        raise ValueError("Unknown input path base.")
    return path


def cli(*args):
    executable = shutil.which("higgsfield")
    if not executable:
        raise ValueError("higgsfield is not installed on PATH.")
    result = subprocess.run([executable, *args, "--json"], text=True, capture_output=True, timeout=120)
    if result.returncode:
        # Provider responses can contain private URLs/account data; don't echo stderr into logs.
        raise RuntimeError(f"Higgsfield returned exit {result.returncode}; inspect the service without resubmitting.")
    return json.loads(result.stdout)


def arguments(request):
    args = [request["model"]]
    for key, value in sorted(request["params"].items()):
        if isinstance(value, bool):
            value = str(value).lower()
        args.append(f"--{key}={value}")  # One argument prevents values becoming CLI flags.
    for item in request.get("media", []):
        args.append(f"--{item['flag']}={identifier(item['id'])}")
    return args


def prepare(source: Path, name: str):
    request = read_json(source)
    for item in request.get("local_inputs", []):
        if item.get("base") == "workspace":
            path = input_path(item)
        else:
            path = (source.parent / item["path"]).resolve()
        if path.is_relative_to(root()):
            item.update(base="workspace", path=path.relative_to(root()).as_posix())
        else:
            item.update(base="absolute", path=str(path))
    validate_request(request)
    path = local_run(name)
    path.mkdir(parents=True, exist_ok=False)
    write_new(path / "request.json", request)
    write_new(path / "manifest.json", {"request_sha256": digest(request), "prepared_at": now()})
    return {"run": name, "request_sha256": digest(request), "submitted": False}


def load(name):
    path = local_run(name)
    request = validate_request(read_json(path / "request.json"))
    sha = digest(request)
    if read_json(path / "manifest.json")["request_sha256"] != sha:
        raise ValueError("Prepared request changed; prepare a new run and obtain new approval.")
    return path, request, sha


def quote(name):
    path, request, sha = load(name)
    model = cli("model", "get", request["model"])
    cost = cli("generate", "cost", *arguments(request))
    credits = number(cost.get("credits"))
    atomic_json(path / "quote.json", {"request_sha256": sha, "at": now(), "credits": credits, "provider": cost})
    atomic_json(path / "model.json", model)
    return {"run": name, "request_sha256": sha, "quoted_credits": credits, "submitted": False}


def account_identity(account):
    # CLI versions expose different identity fields. Unknown identity fails closed.
    for key in ("id", "user_id", "email"):
        if isinstance(account.get(key), str) and account[key]:
            return digest({key: account[key]})
    raise ValueError("Cannot bind approval to the current account; inspect the CLI schema.")


def approve(name, cap, note):
    """Records an EXISTING user approval; never grants authority by itself."""
    path, request, sha = load(name)
    number(cap)
    if not note.strip() or (path / "attempt.json").exists():
        raise ValueError("Need the real approval source and an unattempted run.")
    current = quote(name)
    if current["quoted_credits"] > cap:
        raise ValueError("Quote exceeds the approved cap.")
    identity = account_identity(cli("account", "status"))
    write_new(path / "approval.json", {"request_sha256": sha, "max_credits": cap, "source": note,
                                      "account_sha256": identity, "attempts": 1, "at": now()})
    return {"run": name, "approval_recorded": True, "submitted": False}


def submit(name, execute=False):
    if not execute:
        raise ValueError("Submission requires --execute and an existing request-bound approval.")
    path, request, sha = load(name)
    approval = read_json(path / "approval.json")
    if approval.get("request_sha256") != sha or approval.get("attempts") != 1:
        raise ValueError("Approval does not match this request.")
    provider_sha = digest(arguments(request))
    claim = root() / ".local/attempts" / f"{provider_sha}.json"
    if (path / "attempt.json").exists() or claim.exists():
        raise ValueError("An attempt already exists. Reconcile status; never resubmit.")
    current = quote(name)
    cap = number(approval["max_credits"])
    if current["quoted_credits"] > cap:
        raise ValueError("Fresh quote exceeds approval.")
    account = cli("account", "status")
    if account_identity(account) != approval.get("account_sha256"):
        raise ValueError("Account changed since approval.")
    if number(account.get("credits")) < current["quoted_credits"]:
        raise ValueError("Insufficient available credits.")
    state = {"status": "submission_uncertain", "request_sha256": sha, "provider_sha256": provider_sha, "attempts": 1,
             "quoted_credits": current["quoted_credits"], "actual_charged": None, "at": now()}
    # O_EXCL via mode x: at most one process/run can claim this exact request.
    write_new(claim, {**state, "run": name})
    write_new(path / "attempt.json", state)
    try:
        result = cli("generate", "create", *arguments(request))
        atomic_json(path / "provider-response.json", result)
        if isinstance(result, list):
            if len(result) != 1:
                raise ValueError("Unexpected result count; reconcile via provider history.")
            result = result[0]
        job_id = result if isinstance(result, str) else result.get("id", result.get("job_id"))
        state.update(status="submitted", job_id=identifier(job_id))
    except Exception as exc:
        state["error_type"] = type(exc).__name__
        atomic_json(path / "attempt.json", state)
        atomic_json(claim, {**state, "run": name})
        raise RuntimeError("Submission outcome is uncertain. Do not retry; reconcile provider history.") from exc
    atomic_json(path / "attempt.json", state)
    atomic_json(claim, {**state, "run": name})
    return state


def status(name):
    path = local_run(name)
    if not (path / "attempt.json").exists():
        # Status does not validate local media: receipts remain inspectable if a guide disappears.
        request = read_json(path / "request.json")
        claim = root() / ".local/attempts" / f"{digest(arguments(request))}.json"
        if not claim.exists():
            return {"run": name, "status": "not_submitted"}
        state = read_json(claim)
    else:
        state = read_json(path / "attempt.json")
    if state.get("job_id"):
        return {"local_attempt": state, "provider": cli("generate", "get", identifier(state["job_id"]))}
    return state
