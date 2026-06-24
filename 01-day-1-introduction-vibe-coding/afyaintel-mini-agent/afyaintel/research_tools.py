from __future__ import annotations

from datetime import date

from .dashboard import format_dashboard_payload
from .domain import StockItem
from .fhir import format_fhir_export
from .forecasting import format_forecast
from .governance import format_approval_matrix
from .nlp import format_clinical_cues
from .sync import format_sync_queue


def research_operational_response(
    query: str, items: list[StockItem], language: str, reference_date: date
) -> str | None:
    normalized = query.lower()
    if any(term in normalized for term in ["forecast", "stock-out", "stockout", "utabiri", "kuisha kwa akiba", "risk forecast"]):
        return format_forecast(items, reference_date, language)
    if any(term in normalized for term in ["fhir", "dhis2", "got-homis", "interoperability bundle"]):
        return format_fhir_export(items, language)
    if any(term in normalized for term in ["sync", "synchronize", "queue", "kusawazisha", "foleni"]):
        return format_sync_queue(items, language)
    if any(term in normalized for term in ["dashboard", "a2ui", "canvas", "visual"]):
        return format_dashboard_payload(items, reference_date, language)
    if any(term in normalized for term in ["approval", "governance", "human review", "idhini", "mamlaka"]):
        return format_approval_matrix(language)
    if any(term in normalized for term in ["nlp", "symptom extraction", "clinical cue", "swanglish", "dalili"]):
        return format_clinical_cues(query, language)
    return None
