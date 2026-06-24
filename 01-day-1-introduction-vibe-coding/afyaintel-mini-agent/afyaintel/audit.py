from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from .config import AUDIT_PATH


def hash_query(query: str) -> str:
    return hashlib.sha256(query.encode("utf-8")).hexdigest()[:16]


def record_event(
    *,
    query: str,
    language: str,
    execution_path: str,
    blocked: bool,
    emergency: bool,
    path: Path = AUDIT_PATH,
) -> None:
    """Write privacy-preserving metadata; never store raw user text."""
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "query_hash": hash_query(query),
        "language": language,
        "execution_path": execution_path,
        "blocked": blocked,
        "emergency": emergency,
    }
    try:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    except OSError:
        # Audit failure must not break read-only operational support.
        pass
