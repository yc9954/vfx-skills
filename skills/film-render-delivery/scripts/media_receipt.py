#!/usr/bin/env python3
"""Read-only local media verification. Requires ffmpeg/ffprobe; no quality verdict."""

import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def positive_int(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return value


def positive_float(value):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return value


def rate(value):
    try:
        result = Fraction(str(value))
        if result <= 0:
            raise ValueError()
        return result
    except (ValueError, ZeroDivisionError):
        raise argparse.ArgumentTypeError("FPS must be positive, e.g. 24 or 30000/1001")


def fingerprint(path):
    state = path.stat()
    return (state.st_dev, state.st_ino, state.st_size, state.st_mtime_ns)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def finite_number(value):
    try:
        number = float(value)
        return number if math.isfinite(number) else None
    except (ValueError, TypeError):
        return None


def inspect_media(args):
    media = args.media.resolve(strict=True)
    if not media.is_file():
        raise ValueError("media must be a local regular file")
    scene = args.scene.resolve(strict=True) if args.scene else None
    if scene and not scene.is_file():
        raise ValueError("scene must be a local regular file")
    ffprobe, ffmpeg = shutil.which("ffprobe"), shutil.which("ffmpeg")
    if not ffprobe or not ffmpeg:
        raise ValueError("ffprobe and ffmpeg must be available on PATH")
    before = fingerprint(media)
    scene_before = fingerprint(scene) if scene else None
    probe = subprocess.run(
        [ffprobe, "-v", "error", "-count_frames", "-show_streams", "-show_format",
         "-of", "json", str(media)],
        capture_output=True, text=True, timeout=args.timeout,
    )
    if probe.returncode:
        raise ValueError("ffprobe failed: " + probe.stderr[-2000:])
    data = json.loads(probe.stdout)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    if not video:
        raise ValueError("no video stream")
    frames_text = str(video.get("nb_read_frames", ""))
    frames = int(frames_text) if frames_text.isdigit() else None
    try:
        fps = rate(video.get("avg_frame_rate", "0/0"))
    except argparse.ArgumentTypeError:
        fps = None
    duration = finite_number(video.get("duration"))
    if duration is None:
        ticks = finite_number(video.get("duration_ts"))
        try:
            duration = ticks * float(Fraction(video["time_base"])) if ticks is not None else None
        except (ValueError, ZeroDivisionError, KeyError):
            duration = None
    audio_count = sum(s.get("codec_type") == "audio" for s in streams)
    decode = subprocess.run(
        [ffmpeg, "-nostdin", "-v", "error", "-xerror", "-i", str(media),
         "-map", "0:v:0", "-map", "0:a?", "-f", "null", "-"],
        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, timeout=args.timeout,
    )
    digest = sha256(media)
    scene_digest = sha256(scene) if scene else None
    checks = []

    def check(name, ok, actual, expected):
        checks.append({"name": name, "passed": bool(ok), "actual": actual, "expected": expected})

    check("complete_decode", decode.returncode == 0 and not decode.stderr.strip(),
          {"exit_code": decode.returncode, "errors_tail": decode.stderr[-2000:]}, "no decode errors")
    check("nonempty_video", frames is not None and frames > 0, frames, "positive decoded frame count")
    check("input_unchanged", before == fingerprint(media), before == fingerprint(media), True)
    if scene:
        check("scene_unchanged", scene_before == fingerprint(scene), scene_before == fingerprint(scene), True)
    for label, actual, expected in (
        ("frame_count", frames, args.expect_frames),
        ("width", video.get("width"), args.expect_width),
        ("height", video.get("height"), args.expect_height),
    ):
        if expected is not None:
            check(label, actual == expected, actual, expected)
    if args.expect_fps is not None:
        check("average_fps", fps is not None and abs(float(fps - args.expect_fps)) < 1e-6,
              str(fps) if fps else None, str(args.expect_fps))
    if args.expect_seconds is not None:
        check("video_duration", duration is not None and abs(duration - args.expect_seconds) <= args.duration_tolerance,
              duration, {"seconds": args.expect_seconds, "tolerance_seconds": args.duration_tolerance})
    if args.audio != "any":
        check("audio_presence", audio_count > 0 if args.audio == "required" else audio_count == 0,
              audio_count, args.audio)
    report = {
        "schema": "film-media-receipt/v1", "media": str(media), "sha256": digest,
        "scene": {"path": str(scene), "sha256": scene_digest} if scene else None,
        "observed": {"frames": frames, "average_fps": str(fps) if fps else None,
                     "video_duration_seconds": duration, "width": video.get("width"),
                     "height": video.get("height"), "audio_streams": audio_count},
        "checks": checks, "technical_pass": all(c["passed"] for c in checks),
        "scope": "First video stream plus all audio decoded. Only supplied expectations were tested. "
                 "Average FPS does not establish CFR. Scene hash is identity, not scene inspection.",
        "perceptual_review": {"acting": "unverified", "contacts": "unverified",
                              "materials": "unverified", "audio_quality": "unverified"},
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("--expect-frames", type=positive_int)
    parser.add_argument("--expect-fps", type=rate)
    parser.add_argument("--expect-seconds", type=positive_float)
    parser.add_argument("--expect-width", type=positive_int)
    parser.add_argument("--expect-height", type=positive_int)
    parser.add_argument("--duration-tolerance", type=positive_float, default=0.05)
    parser.add_argument("--audio", choices=("any", "required", "absent"), default="any")
    parser.add_argument("--scene", type=Path)
    parser.add_argument("--receipt", type=Path, help="New JSON path; existing files are never overwritten")
    parser.add_argument("--timeout", type=positive_float, default=600)
    args = parser.parse_args()
    try:
        if args.receipt and (args.receipt.exists() or not args.receipt.parent.is_dir()):
            raise ValueError("receipt must be a new path inside an existing directory")
        report = inspect_media(args)
        encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.receipt:
            with args.receipt.open("x", encoding="utf-8") as stream:
                stream.write(encoded)
        print(encoded, end="")
        return 0 if report["technical_pass"] else 1
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"error": str(error), "technical_pass": False}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
