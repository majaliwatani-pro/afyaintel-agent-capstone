# AfyaIntel Safety Rules

## Operational Scope

Allowed:

- Stock quantities and thresholds
- Expiry and FEFO-related alerts
- Draft operational reports
- English/Swahili operational explanations
- Human escalation and contact guidance

Prohibited:

- Diagnosis
- Treatment selection
- Prescription or dosage advice
- Autonomous procurement or payment
- Real identifiable patient data

## Safety Execution Order

1. Detect language.
2. Evaluate clinical and emergency intent.
3. If blocked, return a referral response before any model call.
4. Otherwise route the request to deterministic operational tools.
5. Use Gemini only for safe, open-ended operational explanations.

## Emergency Escalation

Potential emergency language produces an urgent message and directs the user to qualified medical assistance and the configured supervisor contact.

The sample contact is synthetic and must be replaced with an authorized local contact before any controlled field test.

## Data Integrity

- Quantities must be non-negative integers.
- Expiry dates must use ISO `YYYY-MM-DD` format.
- Missing columns or invalid values cause a clean data-validation error.
- The agent must not invent missing inventory values.

## Human Authority

All procurement, redistribution, record modification, and external communication require explicit approval from authorized facility staff.
