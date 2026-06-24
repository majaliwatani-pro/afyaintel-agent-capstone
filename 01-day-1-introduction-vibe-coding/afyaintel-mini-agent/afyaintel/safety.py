from __future__ import annotations

from .config import SUPERVISOR_CONTACT
from .domain import SafetyDecision

EMERGENCY_TERMS = {
    "respiratory distress",
    "difficulty breathing",
    "unconscious",
    "severe bleeding",
    "chest pain",
    "kupumua kwa shida",
    "amepoteza fahamu",
    "damu nyingi",
    "dharura",
}
SYMPTOM_TERMS = {
    "fever",
    "pain",
    "cough",
    "vomiting",
    "diarrhea",
    "headache",
    "sore throat",
    "homa",
    "maumivu",
    "kukohoa",
    "kutapika",
    "kuharisha",
    "kichwa kuuma",
    "mgonjwa",
}
ADVICE_TERMS = {
    "what medicine",
    "which medicine",
    "what drug",
    "diagnose",
    "prescribe",
    "treatment",
    "dosage",
    "dose",
    "nimpe dawa gani",
    "nitumie dawa gani",
    "tiba gani",
    "ugonjwa gani",
    "nifanye nini",
}


def evaluate_clinical_safety(text: str) -> SafetyDecision:
    normalized = text.lower()
    emergency = any(term in normalized for term in EMERGENCY_TERMS)
    requests_clinical_advice = any(term in normalized for term in ADVICE_TERMS)
    contains_symptom = any(term in normalized for term in SYMPTOM_TERMS)

    if emergency:
        return SafetyDecision(True, True, "Potential emergency or urgent clinical condition")
    if requests_clinical_advice and contains_symptom:
        return SafetyDecision(True, False, "Request for diagnosis, treatment, or prescription")
    return SafetyDecision(False, False, "Operational request")


def safety_response(language: str, emergency: bool = False) -> str:
    if language == "sw":
        base = (
            "LENGO LA USALAMA WA KIAFYA\n"
            "AfyaIntel ni msaidizi wa shughuli za kituo. Haitoi utambuzi wa ugonjwa, "
            "maagizo ya dawa, wala mpango wa matibabu.\n"
            "Tafadhali wasiliana na mtaalamu wa afya aliyehitimu au kituo cha afya kilicho karibu.\n"
            f"Mawasiliano ya kupandisha suala: {SUPERVISOR_CONTACT}"
        )
        if emergency:
            return (
                "Hili linaweza kuwa jambo la dharura. Tafuta msaada wa kitaalamu mara moja.\n"
                + base
            )
        return base

    base = (
        "CLINICAL SAFETY GATEWAY\n"
        "AfyaIntel is an operational support assistant. It does not diagnose conditions, "
        "prescribe medicines, or provide treatment instructions.\n"
        "Please contact a qualified health professional or the nearest health facility.\n"
        f"Escalation contact: {SUPERVISOR_CONTACT}"
    )
    if emergency:
        return "This may be an emergency. Seek qualified medical assistance immediately.\n" + base
    return base
