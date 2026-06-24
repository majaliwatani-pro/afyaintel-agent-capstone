from __future__ import annotations

from dataclasses import dataclass


SYMPTOM_DICTIONARY = {
    "homa": "fever",
    "fever": "fever",
    "kukohoa": "cough",
    "cough": "cough",
    "kuharisha": "diarrhea",
    "diarrhea": "diarrhea",
    "kutapika": "vomiting",
    "vomiting": "vomiting",
    "maumivu": "pain",
    "pain": "pain",
    "kichwa": "headache",
    "headache": "headache",
}
RED_FLAG_TERMS = {
    "kupumua kwa shida": "difficulty_breathing",
    "difficulty breathing": "difficulty_breathing",
    "amepoteza fahamu": "unconscious",
    "unconscious": "unconscious",
    "damu nyingi": "severe_bleeding",
    "severe bleeding": "severe_bleeding",
    "chest pain": "chest_pain",
}


@dataclass(frozen=True)
class ClinicalCue:
    normalized_text: str
    extracted_symptoms: list[str]
    red_flags: list[str]
    clinical_intent: str
    requires_human_review: bool


def normalize_clinical_text(text: str) -> str:
    return " ".join(text.lower().strip().split())


def extract_clinical_cues(text: str) -> ClinicalCue:
    normalized = normalize_clinical_text(text)
    symptoms = sorted({canonical for term, canonical in SYMPTOM_DICTIONARY.items() if term in normalized})
    red_flags = sorted({canonical for term, canonical in RED_FLAG_TERMS.items() if term in normalized})
    if red_flags:
        intent = "urgent_red_flag_review"
    elif symptoms:
        intent = "symptom_structuring_for_clinician"
    else:
        intent = "non_clinical_or_operational"
    return ClinicalCue(
        normalized_text=normalized,
        extracted_symptoms=symptoms,
        red_flags=red_flags,
        clinical_intent=intent,
        requires_human_review=bool(symptoms or red_flags),
    )


def format_clinical_cues(text: str, language: str) -> str:
    cues = extract_clinical_cues(text)
    if language == "sw":
        lines = [
            "# Muhtasari wa NLP ya Kliniki (kwa mapitio ya mtaalamu)",
            f"Maandishi yaliyosafishwa: {cues.normalized_text}",
            f"Dalili zilizotambuliwa: {', '.join(cues.extracted_symptoms) if cues.extracted_symptoms else 'Hakuna'}",
            f"Viashiria hatarishi: {', '.join(cues.red_flags) if cues.red_flags else 'Hakuna'}",
            f"Aina ya nia: {cues.clinical_intent}",
            "Uamuzi: Taarifa hii ni cue ya kusaidia mapitio ya mhudumu wa afya; si utambuzi wa ugonjwa.",
        ]
        return "\n".join(lines)
    lines = [
        "# Clinical NLP Cue Summary (for human review)",
        f"Normalized text: {cues.normalized_text}",
        f"Extracted symptoms: {', '.join(cues.extracted_symptoms) if cues.extracted_symptoms else 'None'}",
        f"Red flags: {', '.join(cues.red_flags) if cues.red_flags else 'None'}",
        f"Intent class: {cues.clinical_intent}",
        "Decision: This is a human-review support cue, not a diagnosis.",
    ]
    return "\n".join(lines)
