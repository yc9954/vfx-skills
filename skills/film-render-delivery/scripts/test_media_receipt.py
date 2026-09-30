#!/usr/bin/env python3
"""Behavior tests with disposable synthetic media; requires ffmpeg/ffprobe."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("media_receipt.py")


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg/ffprobe required")
class ReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="film-receipt-test-")
        cls.root = Path(cls.temp.name)
        cls.video = cls.root / "silent clip.mp4"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-f", "lavfi", "-i",
                        "color=c=blue:size=64x64:rate=12:duration=1", "-an", "-c:v", "mpeg4",
                        str(cls.video)], check=True, capture_output=True, timeout=30)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def run_receipt(self, *args, media=None):
        return subprocess.run([sys.executable, str(SCRIPT), str(media or self.video), *args],
                              capture_output=True, text=True, timeout=30)

    def test_expected_media_passes_without_perceptual_claim(self):
        result = self.run_receipt("--expect-frames", "12", "--expect-fps", "12/1",
                                  "--expect-seconds", "1", "--expect-width", "64",
                                  "--expect-height", "64", "--audio", "absent")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["technical_pass"])
        self.assertTrue(all(v == "unverified" for v in report["perceptual_review"].values()))
        self.assertEqual(len(report["sha256"]), 64)

    def test_wrong_length_is_failure(self):
        result = self.run_receipt("--expect-frames", "13", "--expect-seconds", "2")
        self.assertEqual(result.returncode, 1, result.stderr)
        failed = [c["name"] for c in json.loads(result.stdout)["checks"] if not c["passed"]]
        self.assertIn("frame_count", failed)
        self.assertIn("video_duration", failed)

    def test_absent_required_audio_is_failure(self):
        self.assertEqual(self.run_receipt("--audio", "required").returncode, 1)

    def test_audio_stream_is_detected(self):
        audio_video = self.root / "with-audio.mp4"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(self.video),
                        "-f", "lavfi", "-i", "sine=frequency=400:duration=1", "-c:v", "copy",
                        "-c:a", "aac", "-shortest", str(audio_video)], check=True,
                       capture_output=True, timeout=30)
        result = self.run_receipt("--audio", "required", media=audio_video)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["observed"]["audio_streams"], 1)

    def test_existing_receipt_preserved(self):
        receipt = self.root / "existing.json"
        receipt.write_text("user original", encoding="utf-8")
        result = self.run_receipt("--receipt", str(receipt))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(receipt.read_text(), "user original")

    def test_new_receipt_and_scene_identity(self):
        scene = self.root / "identity-only.blend"
        scene.write_bytes(b"not-a-real-scene: hash-binding-test-only")
        receipt = self.root / "new-receipt.json"
        result = self.run_receipt("--scene", str(scene), "--receipt", str(receipt))
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(receipt.read_text())
        self.assertEqual(report["scene"]["path"], str(scene.resolve()))
        self.assertIn("not scene inspection", report["scope"])

    def test_invalid_media_is_not_success(self):
        invalid = self.root / "invalid.mp4"
        invalid.write_bytes(b"this is not a video")
        self.assertEqual(self.run_receipt(media=invalid).returncode, 2)

    def test_missing_file_is_not_success(self):
        self.assertEqual(self.run_receipt(media=self.root / "missing.mp4").returncode, 2)

    def test_invalid_fps_rejected(self):
        self.assertEqual(self.run_receipt("--expect-fps", "0/0").returncode, 2)

    def test_wrong_fps_and_size_are_failures(self):
        result = self.run_receipt("--expect-fps", "24", "--expect-width", "128")
        self.assertEqual(result.returncode, 1, result.stderr)
        failed = [c["name"] for c in json.loads(result.stdout)["checks"] if not c["passed"]]
        self.assertIn("average_fps", failed)
        self.assertIn("width", failed)


if __name__ == "__main__":
    unittest.main()
