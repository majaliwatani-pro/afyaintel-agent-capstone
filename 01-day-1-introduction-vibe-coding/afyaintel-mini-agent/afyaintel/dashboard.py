from __future__ import annotations

import json
from pathlib import Path

from .config import DASHBOARD_PATH
from .domain import StockItem
from .forecasting import build_forecast
from .tools import get_expiring_items, get_low_stock


def build_dashboard_payload(items: list[StockItem], reference_date, path: Path = DASHBOARD_PATH) -> dict:
    low = get_low_stock(items)
    expiring = get_expiring_items(items, reference_date)
    forecast = build_forecast(items, reference_date)
    payload = {
        "schema": "A2UI-DEMO-1.0",
        "title": "AfyaIntel Facility Operations Dashboard",
        "components": [
            {"type": "metric", "label": "Total items", "value": len(items)},
            {"type": "metric", "label": "Low-stock items", "value": len(low)},
            {"type": "metric", "label": "Expiring within 30 days", "value": len(expiring)},
            {
                "type": "table",
                "label": "High-risk stock-out items",
                "columns": ["item", "risk", "estimated_stockout_date"],
                "rows": [
                    [risk.item_name, risk.risk_level, risk.estimated_stockout_date]
                    for risk in forecast if risk.risk_level == "HIGH"
                ],
            },
        ],
        "safety_note": "Dashboard is decision support only; procurement requires human approval.",
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


def format_dashboard_payload(items: list[StockItem], reference_date, language: str) -> str:
    payload = build_dashboard_payload(items, reference_date)
    if language == "sw":
        return (
            "A2UI dashboard payload imetengenezwa kwa demo. "
            f"Vipengele: {len(payload['components'])}. Maamuzi ya uendeshaji yahakikiwe na binadamu."
        )
    return (
        "A2UI dashboard payload generated for demo rendering. "
        f"Components: {len(payload['components'])}. Operational decisions require human review."
    )
