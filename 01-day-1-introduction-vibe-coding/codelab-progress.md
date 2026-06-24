# Day 1 Progress — Introduction to Agents and Vibe Coding

**Date:** June 15, 2026  
**Status:** Core technical work completed; Unit 1 podcast and final evidence capture remain

## Assignment Progress

| Assignment | Status | Evidence |
|---|---|---|
| Unit 1 summary podcast | Not yet documented | Add notes and screenshot after listening |
| Whitepaper: *The New SDLC with Vibe Coding* | Completed | `whitepaper-notes.md` |
| Antigravity 2.0 and IDE codelab | Completed | Setup notes and error log; recapture final screenshot if needed |
| AI Studio app and Starter Tier deployment | Reported completed | Deployment screenshot is not present in this archive; add before final submission |
| Day 1 livestream | Completed | `day-1-livestream-notes.md` and screenshots index |
| AfyaIntel mini-agent | Completed and professionalized | Working code and `eval_report.md` |
| Gemini API local test | Completed | `screenshots/04-gemini-api-test-output.png` |

## Technical Achievements

- Installed and verified Python 3.12, pip, and uv.
- Configured the local course workspace.
- Configured Google Cloud CLI and Application Default Credentials without storing credentials in the repository.
- Built a local-first bilingual operations agent.
- Added deterministic stock, expiry, reporting, and safety tools.
- Added an optional Gemini response layer with quota fallback.
- Added a zero-API local evaluation suite.
- Removed `.env` from the shareable project archive.

## AfyaIntel Evaluation

Recommended command:

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\01-day-1-introduction-vibe-coding\afyaintel-mini-agent"
uv run python main.py --evaluate-local
```

Current professionalization result:

- 14/14 local deterministic checks passed
- Zero Gemini API calls used
- Safety routing tested in English and Swahili
- Quota-independent stock reporting confirmed

## Important Errors and Learning

- Correct PowerShell working directory is essential.
- `uv run` should be used to execute the project in its managed environment.
- Antigravity sandbox behavior may differ on Windows.
- Gemini free-tier quota should be treated as an architecture constraint, not only an account limitation.
- `.gitignore` does not remove a secret from a manually created ZIP; `.env` must be excluded explicitly.

## Remaining Day 1 Actions

- [ ] Listen to and document the Unit 1 podcast.
- [ ] Add or recapture the Antigravity codelab screenshot.
- [ ] Add or recapture the AI Studio build screenshot.
- [ ] Add or recapture the Starter Tier deployment screenshot.
- [ ] Capture `14/14 checks passed` from the local evaluation.
- [ ] Capture the scripted AfyaIntel demo and safety response.
