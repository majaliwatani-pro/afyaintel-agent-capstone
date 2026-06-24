from __future__ import annotations

import hashlib
import json
import os
import time

from .config import CACHE_PATH, FACILITY_NAME, MODEL_NAME

try:
    from google import genai
    from google.genai import types
except ImportError:  # Live model access is optional.
    genai = None
    types = None


def _load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save_cache(cache: dict[str, str]) -> None:
    try:
        CACHE_PATH.write_text(
            json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except OSError:
        pass


def _cache_key(query: str) -> str:
    payload = f"{MODEL_NAME}|{query.strip().lower()}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def quota_fallback_message(language: str) -> str:
    if language == "sw":
        return (
            "Huduma ya Gemini haipatikani kwa sasa kutokana na kikomo cha matumizi. "
            "AfyaIntel inaendelea katika hali ya ndani kwa kazi za akiba, muda wa matumizi, ripoti na usalama."
        )
    return (
        "Gemini quota is currently unavailable. AfyaIntel is continuing in local operational mode "
        "for stock, expiry, reporting, and safety tasks."
    )


def call_gemini(query: str, retry_once: bool = True) -> tuple[str | None, str]:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or genai is None or types is None:
        return None, "MODEL_UNAVAILABLE"

    cache = _load_cache()
    key = _cache_key(query)
    if key in cache:
        return cache[key], "CACHE_HIT"

    system_instruction = f"""You are AfyaIntel, a bilingual health-facility operations assistant for {FACILITY_NAME}.
You may explain operational concepts, stock-management processes, reporting workflows, and software usage.
Never diagnose, prescribe, recommend a medicine for symptoms, or process identifiable patient information.
Respond in Swahili when the user writes in Swahili; otherwise respond in English.
Be concise. If the request requires a local inventory value, state that deterministic inventory tools must be used instead of guessing.
"""

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2,
            ),
        )
        text = (response.text or "").strip()
        if text:
            cache[key] = text
            _save_cache(cache)
            return text, "MODEL_SUCCESS"
        return None, "EMPTY_MODEL_RESPONSE"
    except Exception as exc:  # SDK exception types vary by version.
        message = str(exc)
        daily_quota = "GenerateRequestsPerDayPerProjectPerModel" in message
        temporary_limit = any(
            token in message
            for token in ["retryDelay", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE"]
        )
        if daily_quota:
            return None, "DAILY_QUOTA_EXHAUSTED"
        if temporary_limit and retry_once:
            time.sleep(2)
            return call_gemini(query, retry_once=False)
        return None, "MODEL_ERROR"
