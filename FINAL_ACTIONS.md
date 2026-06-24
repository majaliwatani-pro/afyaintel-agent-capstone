# Final Actions Before Kaggle Capstone Submission

The professional project files are ready. Complete these user-side actions in order.

## 1. Replace the local workspace

Back up the current folder, then use the final professional ZIP.

## 2. Verify the application

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\01-day-1-introduction-vibe-coding\afyaintel-mini-agent"
uv sync
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
uv run python main.py --demo
```

Expected:

- `14/14 checks passed`
- `Ran 10 tests ... OK`

## 3. Verify the local API

```powershell
uv run python server.py
```

In another PowerShell window:

```powershell
Invoke-RestMethod http://localhost:8080/health
Invoke-RestMethod "http://localhost:8080/api/summary?lang=en"
```

## 4. Open the portfolio

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\portfolio"
python -m http.server 8000
```

Open `http://localhost:8000`.

## 5. Close course evidence gaps

- Antigravity CLI screenshot
- Google Developer Knowledge MCP grounded answer
- Agent Skill trigger and non-trigger
- Official remaining Day 4/5 task evidence

## 6. Prepare the submission

Use:

- `capstone-afyaintel-agent/submission-copy.md`
- `capstone-afyaintel-agent/final-writeup.md`
- `capstone-afyaintel-agent/demo-script.md`
- Portfolio screenshot or public URL

## 7. Submit officially

When Kaggle releases the capstone portal or final instructions:

1. Read the eligibility and deadline.
2. Submit through the official Kaggle mechanism.
3. Confirm the submission is visible or accepted.
4. Save the confirmation screenshot.

Do not assume that possessing a ZIP automatically counts as participation.
