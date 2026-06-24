---
name: afyaintel-stock-operations
description: Use this skill when the user asks to validate AfyaIntel inventory CSV data, identify low stock, inspect expiry risk, generate English or Swahili facility operations reports, review tool contracts, or run local AfyaIntel evaluations. Do not use it for diagnosis, prescriptions, patient-specific advice, unrelated software questions, or autonomous procurement.
---

# AfyaIntel Stock Operations

## Purpose

Provide a repeatable, safety-governed workflow for reviewing the AfyaIntel inventory prototype.

## Preconditions

1. Work inside the Kaggle course workspace.
2. Do not inspect or reveal `.env`.
3. Use synthetic inventory data only.
4. Keep all operations read-only unless the user explicitly approves a file change.

## Workflow

### 1. Validate the data

Run:

```powershell
python .agents\skills\afyaintel-stock-operations\scripts\validate_stock.py
```

Stop if required columns, dates, quantities, or facility consistency checks fail.

### 2. Select the correct deterministic tool

- Inventory overview → `format_inventory_summary`
- Shortage analysis → `get_low_stock`
- Expiry analysis → `get_expiring_items`
- Weekly report → `build_weekly_report`
- Clinical or emergency prompt → `evaluate_clinical_safety`

Read `references/tool-contracts.md` before changing a tool boundary.

### 3. Preserve safety

- Never provide diagnosis, dosage, prescription, or treatment advice.
- Route emergency or clinical prompts to qualified human review.
- Do not pass identifiable patient data to a model, MCP server, or log.
- Procurement and redistribution require human approval.

### 4. Run local evaluation

Run:

```powershell
python .agents\skills\afyaintel-stock-operations\scripts\run_local_eval.py
```

The skill is not complete unless all local checks pass.

### 5. Report the result

Return:

- Data validation status
- Low-stock count
- Expiry-risk count
- Evaluation result
- Safety or human-review issues
- Files changed, if any

## Output quality

Use concise, management-ready language. Respond in Swahili when the user asks in Swahili. Do not invent inventory values.
