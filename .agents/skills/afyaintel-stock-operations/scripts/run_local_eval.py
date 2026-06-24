from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
APP = ROOT / "01-day-1-introduction-vibe-coding" / "afyaintel-mini-agent"


def main() -> int:
    command = [sys.executable, "main.py", "--evaluate-local"]
    return subprocess.call(command, cwd=APP)


if __name__ == "__main__":
    raise SystemExit(main())
