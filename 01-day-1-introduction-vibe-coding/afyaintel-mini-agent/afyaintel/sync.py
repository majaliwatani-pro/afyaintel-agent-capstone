from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .config import SYNC_QUEUE_PATH
from .domain import StockItem
from .tools import get_low_stock


def enqueue_stock_summary(items: list[StockItem], path: Path = SYNC_QUEUE_PATH) -> int:
    event = {
        "event_type": "deidentified_stock_summary",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "facility_name": items[0].facility_name if items else "Unknown Facility",
        "total_items": len(items),
        "low_stock_items": [item.item_name for item in get_low_stock(items)],
        "sync_status": "queued_for_authorized_upload",
        "privacy_note": "No patient-identifiable data stored in this demo sync event.",
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    return 1


def format_sync_queue(items: list[StockItem], language: str) -> str:
    count = enqueue_stock_summary(items)
    if language == "sw":
        return (
            f"Tukio {count} la muhtasari wa akiba limewekwa kwenye foleni ya kusawazisha. "
            "Hakuna taarifa za mgonjwa zilizohifadhiwa kwenye demo hii."
        )
    return (
        f"Queued {count} de-identified stock-summary event for later synchronization. "
        "No patient-identifiable data was stored in this demo event."
    )
