from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
APP = ROOT / "01-day-1-introduction-vibe-coding" / "afyaintel-mini-agent"
sys.path.insert(0, str(APP))

from afyaintel.data import load_stock_data  # noqa: E402
from afyaintel.tools import get_expiring_items, get_low_stock  # noqa: E402


def main() -> int:
    items = load_stock_data(APP / "sample_stock.csv")
    low = get_low_stock(items)
    expiring = get_expiring_items(items, date(2026, 6, 15))
    print("AfyaIntel stock data: VALID")
    print(f"Facility: {items[0].facility_name}")
    print(f"Records: {len(items)}")
    print(f"Low stock: {len(low)}")
    print(f"Expiring within 30 days: {len(expiring)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
