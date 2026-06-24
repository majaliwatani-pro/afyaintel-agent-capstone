# Contributing

## Before a change

1. Confirm the change remains within the operational, non-clinical scope.
2. Add or update an evaluation case.
3. Do not add real patient data or secrets.

## Required checks

```powershell
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
```

## Pull request checklist

- [ ] Behavior is documented
- [ ] Tests cover the change
- [ ] Safety boundaries are preserved
- [ ] No secret or patient identifier is present
- [ ] Human approval remains explicit for action-capable features
