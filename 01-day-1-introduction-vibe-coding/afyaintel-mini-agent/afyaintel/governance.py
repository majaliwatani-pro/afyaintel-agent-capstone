from __future__ import annotations

APPROVAL_MATRIX = {
    "view_stock_summary": "facility_staff",
    "generate_report": "facility_staff",
    "clinical_triage_review": "licensed_clinician",
    "approve_procurement": "facility_manager_or_pharmacist",
    "share_external_data": "data_governance_officer",
    "pilot_real_patient_data": "ethics_committee_and_facility_authority",
}


def format_approval_matrix(language: str) -> str:
    if language == "sw":
        lines = ["# Jedwali la Idhini za Binadamu"]
        for action, approver in APPROVAL_MATRIX.items():
            lines.append(f"- {action}: {approver}")
        lines.append("AfyaIntel haitoi uamuzi wa mwisho kwa tiba, manunuzi, au kubadilishana data.")
        return "\n".join(lines)
    lines = ["# Human Approval Matrix"]
    for action, approver in APPROVAL_MATRIX.items():
        lines.append(f"- {action}: {approver}")
    lines.append("AfyaIntel does not autonomously finalize clinical, procurement, or data-sharing decisions.")
    return "\n".join(lines)
