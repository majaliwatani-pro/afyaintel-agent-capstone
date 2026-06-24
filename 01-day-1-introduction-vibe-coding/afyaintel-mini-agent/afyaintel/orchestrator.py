from __future__ import annotations

from datetime import date

from .audit import record_event
from .data import DataValidationError, load_stock_data, parse_reference_date
from .domain import QueryResult
from .language import detect_language
from .model import call_gemini, quota_fallback_message
from .safety import evaluate_clinical_safety, safety_response
from .research_tools import research_operational_response
from .tools import help_response, local_operational_response


def process_query(
    query: str,
    *,
    allow_model: bool = True,
    reference_date: date | None = None,
    write_audit: bool = True,
) -> QueryResult:
    language = detect_language(query)
    safety = evaluate_clinical_safety(query)

    if safety.blocked:
        result = QueryResult(
            response=safety_response(language, safety.emergency),
            execution_path="SAFETY_ROUTED",
            language=language,
            blocked=True,
            emergency=safety.emergency,
        )
    else:
        try:
            items = load_stock_data()
            ref_date = reference_date or parse_reference_date()
        except (OSError, DataValidationError) as exc:
            result = QueryResult(
                response=f"Data validation error: {exc}",
                execution_path="DATA_ERROR",
                language=language,
            )
        else:
            # Research-aligned tools (forecast, FHIR, sync, dashboard, governance, NLP)
            # are checked first because their prompts often contain generic words like
            # "stock" or "inventory" that would otherwise be caught by broad summary tools.
            local = research_operational_response(query, items, language, ref_date)
            if local is None:
                local = local_operational_response(query, items, ref_date)
            if local is not None:
                result = QueryResult(local, "LOCAL_TOOL", language)
            elif allow_model:
                model_answer, model_status = call_gemini(query)
                if model_answer:
                    result = QueryResult(model_answer, model_status, language)
                else:
                    result = QueryResult(
                        quota_fallback_message(language)
                        + "\n\n"
                        + help_response(language),
                        model_status,
                        language,
                    )
            else:
                result = QueryResult(
                    help_response(language), "LOCAL_FALLBACK", language
                )

    if write_audit:
        record_event(
            query=query,
            language=result.language,
            execution_path=result.execution_path,
            blocked=result.blocked,
            emergency=result.emergency,
        )
    return result
