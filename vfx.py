"""Checkout-local entry point: no installation, network or heavy dependencies."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from vfx_skills.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
