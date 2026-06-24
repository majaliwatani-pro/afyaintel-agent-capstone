# AfyaIntel Skill Evaluation

## Target

The `afyaintel-stock-operations` skill should trigger for inventory validation, low-stock analysis, expiry alerts, bilingual operations reporting, and local evaluation.

It must not trigger for diagnosis, prescriptions, unrelated coding tasks, or personal patient questions.

## Evaluation gates

- Positive trigger accuracy: 3/3
- Negative trigger accuracy: 3/3
- Local script execution: successful
- Main project evaluation: all checks pass
- No raw prompt or secret stored
- No model call required

## Local commands

```powershell
python .agents\skills\afyaintel-stock-operations\scripts\validate_stock.py
python .agents\skills\afyaintel-stock-operations\scripts\run_local_eval.py
```

## Antigravity evidence still required

1. Restart Antigravity after placing the skill.
2. Ask: `Validate the AfyaIntel stock data and summarize the risks.`
3. Confirm the skill appears in the trace.
4. Ask a negative prompt such as `Explain a CSS grid.`
5. Confirm the skill does not trigger.
