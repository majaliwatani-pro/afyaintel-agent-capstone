from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

from .config import DEFAULT_REFERENCE_DATE, STOCK_PATH
from .domain import StockItem


class DataValidationError(ValueError):
    """Raised when inventory data is missing, malformed, or unsafe to use."""


def parse_reference_date(value: str | None = None) -> date:
    raw = value or DEFAULT_REFERENCE_DATE
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise DataValidationError(
            "AFYAINTEL_REFERENCE_DATE must use YYYY-MM-DD format."
        ) from exc


def _optional_float(row: dict[str, str], key: str, default: float) -> float:
    raw = (row.get(key) or "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError as exc:
        raise DataValidationError(f"Invalid numeric value for {key}.") from exc


def load_stock_data(path: Path = STOCK_PATH) -> list[StockItem]:
    if not path.exists():
        raise FileNotFoundError(f"Stock file was not found: {path}")

    required_columns = {
        "item_name",
        "category",
        "current_stock",
        "minimum_required",
        "unit",
        "expiry_date",
        "facility_name",
    }
    items: list[StockItem] = []

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required_columns - set(reader.fieldnames or [])
        if missing:
            raise DataValidationError(
                f"Stock file is missing required columns: {', '.join(sorted(missing))}"
            )

        for row_number, row in enumerate(reader, start=2):
            try:
                current_stock = int(row["current_stock"])
                minimum_required = int(row["minimum_required"])
                expiry = date.fromisoformat(row["expiry_date"].strip())
            except (TypeError, ValueError) as exc:
                raise DataValidationError(
                    f"Invalid numeric or date value on CSV row {row_number}."
                ) from exc

            if current_stock < 0 or minimum_required < 0:
                raise DataValidationError(
                    f"Negative stock quantity detected on CSV row {row_number}."
                )

            item_name = row["item_name"].strip()
            unit = row["unit"].strip()
            facility_name = row["facility_name"].strip()
            if not item_name or not unit or not facility_name:
                raise DataValidationError(
                    f"Blank required text value detected on CSV row {row_number}."
                )

            default_daily_issue = max(1.0, minimum_required / 30) if minimum_required else 1.0
            daily_issue_average = _optional_float(row, "daily_issue_average", default_daily_issue)
            if daily_issue_average < 0:
                raise DataValidationError(
                    f"Negative daily_issue_average detected on CSV row {row_number}."
                )

            items.append(
                StockItem(
                    item_name=item_name,
                    category=row["category"].strip(),
                    current_stock=current_stock,
                    minimum_required=minimum_required,
                    unit=unit,
                    expiry_date=expiry,
                    facility_name=facility_name,
                    item_code=(row.get("item_code") or "").strip(),
                    batch_id=(row.get("batch_id") or "").strip(),
                    daily_issue_average=daily_issue_average,
                    readiness_level=(row.get("readiness_level") or "Level 2: Hybrid").strip(),
                    sync_status=(row.get("sync_status") or "queued").strip(),
                )
            )

    if not items:
        raise DataValidationError("Stock file contains no inventory records.")

    facilities = {item.facility_name for item in items}
    if len(facilities) != 1:
        raise DataValidationError(
            "The demo CSV must contain records for exactly one facility."
        )
    return items
