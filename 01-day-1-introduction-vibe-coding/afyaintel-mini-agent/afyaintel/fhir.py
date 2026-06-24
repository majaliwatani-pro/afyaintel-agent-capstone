from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .config import FHIR_EXPORT_PATH
from .domain import StockItem


def inventory_to_fhir_bundle(items: list[StockItem]) -> dict:
    facility = items[0].facility_name if items else "Unknown Facility"
    entries = [
        {
            "resource": {
                "resourceType": "Organization",
                "id": "facility-demo",
                "name": facility,
                "type": [{"text": "Primary care facility"}],
            }
        }
    ]
    for index, item in enumerate(items, start=1):
        entries.append(
            {
                "resource": {
                    "resourceType": "Basic",
                    "id": item.item_code or f"inventory-{index}",
                    "code": {"text": "Medication inventory snapshot"},
                    "subject": {"reference": "Organization/facility-demo"},
                    "extension": [
                        {"url": "itemName", "valueString": item.item_name},
                        {"url": "category", "valueString": item.category},
                        {"url": "currentStock", "valueInteger": item.current_stock},
                        {"url": "minimumRequired", "valueInteger": item.minimum_required},
                        {"url": "unit", "valueString": item.unit},
                        {"url": "expiryDate", "valueDate": item.expiry_date.isoformat()},
                        {"url": "stockStatus", "valueString": "LOW" if item.is_low_stock else "ADEQUATE"},
                    ],
                }
            }
        )
    return {
        "resourceType": "Bundle",
        "type": "collection",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "entry": entries,
        "note": "Demo FHIR-compatible bundle for review only; not validated against a national exchange endpoint.",
    }


def write_fhir_bundle(items: list[StockItem], path: Path = FHIR_EXPORT_PATH) -> Path:
    payload = inventory_to_fhir_bundle(items)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def format_fhir_export(items: list[StockItem], language: str) -> str:
    path = write_fhir_bundle(items)
    if language == "sw":
        return (
            "Bundle ya FHIR-compatible imeandaliwa kwa matumizi ya demo tu. "
            f"Imehifadhiwa: {path.name}. Inahitaji uthibitisho wa FHIR na idhini kabla ya kubadilishana data halisi."
        )
    return (
        "FHIR-compatible inventory bundle generated for demonstration only. "
        f"Saved as: {path.name}. Formal FHIR validation and authorization are required before real exchange."
    )
