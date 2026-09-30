import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vfx_skills import catalog, jobs
from vfx_skills.runtime import local_run
from vfx_skills.runtime import file_hash, write_new

UPLOAD = "00000000-0000-4000-8000-000000000001"
JOB = "00000000-0000-4000-8000-000000000002"


class JobTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="VFX Skills test ")
        self.root = Path(self.temp.name)
        (self.root / "config").mkdir()
        (self.root / "config/workflow.json").write_bytes((ROOT / "config/workflow.json").read_bytes())
        self.env = patch.dict(os.environ, {"VFX_SKILLS_ROOT": str(self.root)})
        self.env.start()
        self.request = {"schema": 1, "model": "seedance_2_5", "params": {"prompt": "A chef pours milk", "duration": 10},
                        "media": [{"flag": "image-references", "id": UPLOAD}], "local_inputs": []}
        self.source = self.root / "source.json"
        self.source.write_text(json.dumps(self.request))
        self.remote = patch.object(jobs, "cli", side_effect=self.provider)
        self.mock_cli = self.remote.start()
        self.credit = 90
        self.create_failure = False
        self.account = "test@example.invalid"

    def tearDown(self):
        self.remote.stop()
        self.env.stop()
        self.temp.cleanup()

    def provider(self, *args):
        if args[:2] == ("generate", "cost"):
            return {"credits": self.credit}
        if args[:2] == ("account", "status"):
            return {"email": self.account, "credits": 200}
        if args[:2] == ("model", "get"):
            return {"id": "seedance_2_5"}
        if args[:2] == ("generate", "create"):
            if self.create_failure:
                raise TimeoutError()
            return [{"id": JOB}]
        if args[:2] == ("generate", "get"):
            return {"status": "completed"}
        self.fail(f"Unexpected remote command: {args[:2]}")

    def approved(self, run="test"):
        jobs.prepare(self.source, run)
        jobs.approve(run, 100, "Test fixture: user explicitly approved one request")

    def test_prepare_is_offline(self):
        jobs.prepare(self.source, "test")
        self.mock_cli.assert_not_called()

    def test_one_submission(self):
        self.approved()
        self.assertEqual(jobs.submit("test", True)["job_id"], JOB)
        with self.assertRaises(ValueError):
            jobs.submit("test", True)
        self.assertEqual(jobs.status("test")["provider"]["status"], "completed")

    def test_uncertain_never_retries(self):
        self.approved()
        self.create_failure = True
        with self.assertRaises(RuntimeError):
            jobs.submit("test", True)
        with self.assertRaises(ValueError):
            jobs.submit("test", True)
        self.assertEqual(jobs.status("test")["status"], "submission_uncertain")

    def test_duplicate_run_cannot_bypass_attempt(self):
        self.approved("one")
        self.approved("two")
        jobs.submit("one", True)
        with self.assertRaises(ValueError):
            jobs.submit("two", True)

    def test_bookkeeping_cannot_bypass_effective_request(self):
        self.approved("one")
        jobs.submit("one", True)
        self.request["delivery"] = {"label": "same paid request, another label"}
        self.source.write_text(json.dumps(self.request))
        self.approved("two")
        with self.assertRaises(ValueError):
            jobs.submit("two", True)

    def test_interrupted_claim_is_visible(self):
        self.approved()
        def interrupted(path, value):
            if path.name == "attempt.json":
                raise OSError("simulated disk failure")
            return write_new(path, value)
        with patch.object(jobs, "write_new", side_effect=interrupted):
            with self.assertRaises(OSError):
                jobs.submit("test", True)
        self.assertEqual(jobs.status("test")["status"], "submission_uncertain")
        self.assertFalse(any(c.args[:2] == ("generate", "create") for c in self.mock_cli.call_args_list))

    def test_prepared_run_moves_with_checkout(self):
        import shutil
        guide = self.root / "guide.png"
        guide.write_bytes(b"mock guide")
        self.request["local_inputs"] = [{"path": "guide.png", "sha256": file_hash(guide)}]
        self.source.write_text(json.dumps(self.request))
        self.approved()
        moved = self.root / "relocated workspace"
        moved.mkdir()
        for name in ("config", ".local", "guide.png"):
            shutil.move(str(self.root / name), str(moved / name))
        with patch.dict(os.environ, {"VFX_SKILLS_ROOT": str(moved)}):
            _, request, _ = jobs.load("test")
            self.assertEqual(request["local_inputs"][0]["base"], "workspace")
            self.assertEqual(jobs.submit("test", True)["job_id"], JOB)

    def test_quote_increase_blocks(self):
        self.approved()
        self.credit = 101
        with self.assertRaises(ValueError):
            jobs.submit("test", True)
        self.assertFalse(any(c.args[:2] == ("generate", "create") for c in self.mock_cli.call_args_list))

    def test_account_switch_blocks(self):
        self.approved()
        self.account = "different@example.invalid"
        with self.assertRaises(ValueError):
            jobs.submit("test", True)

    def test_changed_request_blocks(self):
        self.approved()
        path = local_run("test") / "request.json"
        value = json.loads(path.read_text())
        value["params"]["prompt"] = "Different film"
        path.write_text(json.dumps(value))
        with self.assertRaises(ValueError):
            jobs.submit("test", True)

    def test_media_path_cannot_trigger_auto_upload(self):
        self.request["media"][0]["id"] = "/tmp/private.png"
        with self.assertRaises(ValueError):
            jobs.validate_request(self.request)

    def test_parameters_cannot_smuggle_cli_flags(self):
        self.request["params"]["wait"] = True
        with self.assertRaises(ValueError):
            jobs.validate_request(self.request)
        self.request["params"].pop("wait")
        self.request["params"]["prompt"] = "--wait --image=/tmp/private.png"
        self.assertIn("--prompt=--wait --image=/tmp/private.png", jobs.arguments(self.request))

    def test_explicit_submit_required(self):
        with self.assertRaises(ValueError):
            jobs.submit("test")
        self.mock_cli.assert_not_called()

    def test_bad_numbers(self):
        for value in (True, 0, -1, float("nan"), float("inf"), "100"):
            with self.assertRaises(ValueError):
                jobs.number(value)

    def test_run_traversal(self):
        for name in ("../escape", "/tmp/escape", "foo/bar", ""):
            with self.assertRaises(ValueError):
                local_run(name)

    def test_quote_does_not_submit(self):
        jobs.prepare(self.source, "test")
        jobs.quote("test")
        self.assertFalse(any(c.args[:2] == ("generate", "create") for c in self.mock_cli.call_args_list))


class CatalogTests(unittest.TestCase):
    def test_collaborative_planning_routes(self):
        for backend in ("higgsfield", "blender", "hybrid"):
            self.assertIn("animation-causal-staging", catalog.route(backend, "plan")["skills"])
            self.assertIn("visual-image", catalog.route(backend, "storyboard")["skills"])
            self.assertEqual(catalog.route(backend, "previs")["skills"],
                             ["blender-contact-animation", "film-render-delivery"])

    def test_causal_specialist_deduplicates(self):
        result = catalog.route("hybrid", "plan", ["causal_staging"])
        self.assertEqual(result["skills"].count("animation-causal-staging"), 1)
        self.assertEqual(catalog.route("higgsfield", "generate")["skills"], ["blender-seedance-handoff"])

    def test_catalog_links(self):
        self.assertEqual(catalog.validate()["failures"], [])

    def test_backend_does_not_drift(self):
        self.assertEqual(catalog.route("higgsfield", "generate")["skills"], ["blender-seedance-handoff"])
        with self.assertRaises(ValueError):
            catalog.route("higgsfield", "build")

    def test_execution_from_other_cwd(self):
        result = subprocess.run([sys.executable, str(ROOT / "vfx.py"), "route", "higgsfield", "generate"],
                                cwd=tempfile.gettempdir(), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["backend"], "higgsfield")


if __name__ == "__main__":
    unittest.main()
