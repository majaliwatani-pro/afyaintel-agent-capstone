# Errors and Fixes Log

## 1. Python, pip, and uv setup

**Date:** June 15, 2026  
**Issue:** Python and package-management commands were initially unavailable.  
**Resolution:** Installed Python 3.12, verified pip, installed uv, and confirmed execution with a small project.  
**Status:** Fixed

## 2. Antigravity Windows sandbox access to NUL

**Date:** June 15, 2026  
**Issue:** Sandboxed command execution returned an access-denied error while opening the Windows `NUL` device.  
**Resolution:** Used the approved host-execution bypass for the local codelab environment and documented the limitation.  
**Status:** Mitigated

## 3. Missing `python-dotenv`

**Date:** June 15, 2026  
**Issue:** Running global Python produced `ModuleNotFoundError: No module named 'dotenv'`.  
**Cause:** The script was executed outside the uv-managed project environment.  
**Resolution:** Entered the project folder, added dependencies with uv, and ran the script through `uv run`.  
**Status:** Fixed

## 4. Wrong PowerShell working directory

**Date:** June 15, 2026  
**Issue:** Python attempted to open `C:\Users\cohema\main.py`, and `cd /d` failed in PowerShell.  
**Cause:** The command was run from the home directory, and `/d` is CMD syntax rather than PowerShell syntax.  
**Resolution:** Used `Set-Location -Path` with the full project path.  
**Status:** Fixed

## 5. Gemini free-tier quota exhaustion

**Date:** June 15, 2026  
**Issue:** Gemini returned `429 RESOURCE_EXHAUSTED` during repeated interactive and evaluation calls.  
**Cause:** The original agent delegated common stock operations and multi-step evaluation to the model.  
**Engineering resolution:**

- Moved greetings, help, inventory, shortage, expiry, reporting, language routing, and clinical safety to deterministic local tools.
- Added `--evaluate-local`, which makes zero Gemini calls.
- Limited `--evaluate-live` to two requests.
- Added caching and clean quota fallback.
- Removed raw provider error payloads from user-facing output.

**Status:** Architecturally resolved for core workflows

## 6. Secret included in the original ZIP archive

**Date:** June 16, 2026  
**Issue:** The uploaded archive contained a root `.env` file.  
**Risk:** A private API key can be exposed when an archive is shared or published even when `.gitignore` is configured.  
**Resolution:** Removed `.env` from the professional archive, retained only `.env.example`, and added `SECURITY.md`.  
**Required user action:** Revoke and replace the key that was included in the original archive before publishing the project.  
**Status:** Removed from revised archive; key rotation still required

## 7. uv lock file referenced an inaccessible internal package mirror

**Date:** June 17, 2026  
**Issue:** `uv sync` attempted to download `websockets` from an internal package host and timed out.  
**Cause:** A lock file generated in a different execution environment preserved that environment's package source.  
**Resolution:** Removed the foreign `uv.lock` and `.venv`, regenerated dependencies from public PyPI, and excluded environment-specific lock files from the final transferable archive.  
**Verification:** `uv sync`, local evaluation, and PyPI connectivity tests succeeded on the learner's computer.  
**Status:** Fixed
