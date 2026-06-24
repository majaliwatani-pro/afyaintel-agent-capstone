# AfyaIntel Tool Contracts

## Read-only deterministic tools

- `load_stock_data`: validates and reads a single-facility CSV.
- `get_low_stock`: returns records below their minimum threshold.
- `get_expiring_items`: returns records in an expiry window.
- `build_weekly_report`: drafts a bilingual operational report.
- `evaluate_clinical_safety`: blocks diagnosis, prescription, treatment, and emergency prompts.

## Optional generative tool

- `call_gemini`: may explain non-clinical operational concepts only.

## Prohibited actions

- Changing stock records
- Ordering medicines
- Sending messages externally
- Processing payments
- Diagnosing or prescribing

All action-allowed extensions require authentication, authorization, logging, and human approval.
