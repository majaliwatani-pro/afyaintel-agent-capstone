from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

APP_DIR = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = APP_DIR.parents[1]
ENV_PATH = WORKSPACE_ROOT / ".env"
STOCK_PATH = APP_DIR / "sample_stock.csv"
CACHE_PATH = APP_DIR / ".afyaintel_cache.json"
AUDIT_PATH = APP_DIR / ".afyaintel_audit.jsonl"
TOOL_MANIFEST_PATH = APP_DIR / "tool_manifest.json"

load_dotenv(ENV_PATH)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
DEFAULT_REFERENCE_DATE = os.getenv("AFYAINTEL_REFERENCE_DATE", "2026-06-15")
FACILITY_NAME = os.getenv("AFYAINTEL_FACILITY_NAME", "Afya Bora Dispensary")
SUPERVISOR_CONTACT = os.getenv(
    "AFYAINTEL_SUPERVISOR_CONTACT",
    "Facility Clinical Supervisor (DEMO CONTACT ONLY: +255 700 000 000)",
)
ALLOW_MODEL_IN_SERVER = os.getenv("AFYAINTEL_ALLOW_MODEL", "false").lower() == "true"

FHIR_EXPORT_PATH = APP_DIR / "fhir_inventory_bundle.json"
SYNC_QUEUE_PATH = APP_DIR / ".afyaintel_sync_queue.jsonl"
DASHBOARD_PATH = APP_DIR / "a2ui_dashboard_payload.json"
