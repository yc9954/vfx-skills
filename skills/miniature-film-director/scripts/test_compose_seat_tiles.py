"""Synthetic tile integration tests; not foreground removal or projection QA."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("compose_seat_tiles.py")
AVAILABLE = (all(shutil.which(t) for t in ("ffmpeg", "ffprobe"))
             and all(importlib.util.find_spec(m) for m in ("numpy", "PIL")))


@unittest.skipUnless(AVAILABLE, "requires ffmpeg, ffprobe, NumPy and Pillow")
class TileCompositionTests(unittest.TestCase):
    def setUp(self):
        from PIL import Image, ImageDraw
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / "asymmetric source.mkv"
        image = Image.new("RGB", (64, 64), (16, 100, 40))
        draw = ImageDraw.Draw(image)
        draw.rectangle((23, 17, 29, 23), fill=(240, 20, 20))
        draw.rectangle((34, 39, 40, 45), fill=(20, 20, 240))
        png = self.root / "source.png"
        image.save(png)
        subprocess.run(["ffmpeg", "-v", "error", "-n", "-loop", "1", "-framerate", "4",
                        "-i", str(png), "-frames:v", "2", "-c:v", "ffv1",
                        str(self.source)], check=True)
        self.before = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.output = self.root / "new output.mp4"
        self.receipt = self.root / "receipt.json"

    def run_composer(self, *extra, seats=("32,32,0", "96,32,180")):
        args = [sys.executable, str(SCRIPT), str(self.source), str(self.output),
                "--canvas", "128x64", "--tile", "64x64", "--background", "16,100,40",
                "--feather", "4", "--fps", "4", "--seconds", "0.5",
                "--receipt", str(self.receipt)]
        for seat in seats:
            args.extend(["--seat", seat])
        return subprocess.run(args + list(extra), capture_output=True, text=True)

    def test_frame_contract_rotation_and_source_preservation(self):
        result = self.run_composer()
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads(self.receipt.read_text())
        self.assertEqual(receipt["frames"], 2)
        self.assertFalse(receipt["mirrored"])
        self.assertFalse(receipt["projection_calibrated"])
        decoded = subprocess.run(["ffmpeg", "-v", "error", "-i", str(self.output),
                                  "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                 check=True, capture_output=True).stdout
        self.assertEqual(len(decoded), 128 * 64 * 3 * 2)
        for x, y in ((26, 20), (101, 43)):
            offset = (y * 128 + x) * 3
            red, green, blue = decoded[offset:offset + 3]
            self.assertGreater(red, 180)
            self.assertLess(max(green, blue), 70)
        self.assertEqual(hashlib.sha256(self.source.read_bytes()).hexdigest(), self.before)

    def test_existing_output_is_preserved(self):
        self.output.write_bytes(b"existing result")
        self.assertNotEqual(self.run_composer().returncode, 0)
        self.assertEqual(self.output.read_bytes(), b"existing result")
        self.assertFalse(self.receipt.exists())

    def test_overlap_rejected_before_writing(self):
        result = self.run_composer(seats=("32,32,0", "48,32,180"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("overlap", result.stderr)
        self.assertFalse(self.output.exists())

    def test_foreground_in_feather_region_is_not_certified(self):
        result = self.run_composer("--feather", "25")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mismatched color or foreground", result.stderr)
        self.assertFalse(self.receipt.exists())


if __name__ == "__main__":
    unittest.main()
