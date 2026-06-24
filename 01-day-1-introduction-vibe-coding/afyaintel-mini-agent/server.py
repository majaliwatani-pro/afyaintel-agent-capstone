from __future__ import annotations

import json
import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from afyaintel.config import ALLOW_MODEL_IN_SERVER
from afyaintel.data import load_stock_data, parse_reference_date
from afyaintel.orchestrator import process_query
from afyaintel.tools import build_weekly_report, format_inventory_summary
from afyaintel.forecasting import format_forecast
from afyaintel.fhir import inventory_to_fhir_bundle
from afyaintel.dashboard import build_dashboard_payload


class AfyaIntelHandler(BaseHTTPRequestHandler):
    server_version = "AfyaIntelHTTP/1.0"

    def _send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:
        # Keep output concise and avoid echoing request bodies.
        print(f"{self.address_string()} - {format % args}")

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        if parsed.path == "/health":
            self._send_json(
                {
                    "status": "ok",
                    "service": "afyaintel",
                    "mode": "local-first",
                    "model_enabled": ALLOW_MODEL_IN_SERVER,
                }
            )
            return

        if parsed.path == "/api/summary":
            language = query.get("lang", ["en"])[0]
            if language not in {"en", "sw"}:
                self._send_json({"error": "lang must be en or sw"}, HTTPStatus.BAD_REQUEST)
                return
            try:
                items = load_stock_data()
                response = format_inventory_summary(items, language)
            except Exception as exc:
                self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            self._send_json({"response": response, "path": "LOCAL_TOOL", "language": language})
            return


        if parsed.path == "/api/forecast":
            language = query.get("lang", ["en"])[0]
            if language not in {"en", "sw"}:
                self._send_json({"error": "lang must be en or sw"}, HTTPStatus.BAD_REQUEST)
                return
            try:
                items = load_stock_data()
                response = format_forecast(items, parse_reference_date(), language)
            except Exception as exc:
                self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            self._send_json({"response": response, "path": "LOCAL_TOOL", "language": language})
            return

        if parsed.path == "/api/fhir/inventory":
            try:
                items = load_stock_data()
                payload = inventory_to_fhir_bundle(items)
            except Exception as exc:
                self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            self._send_json(payload)
            return

        if parsed.path == "/api/dashboard":
            try:
                items = load_stock_data()
                payload = build_dashboard_payload(items, parse_reference_date())
            except Exception as exc:
                self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            self._send_json(payload)
            return

        if parsed.path == "/api/report":
            language = query.get("lang", ["en"])[0]
            if language not in {"en", "sw"}:
                self._send_json({"error": "lang must be en or sw"}, HTTPStatus.BAD_REQUEST)
                return
            try:
                items = load_stock_data()
                response = build_weekly_report(items, language, parse_reference_date())
            except Exception as exc:
                self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            self._send_json({"response": response, "path": "LOCAL_TOOL", "language": language})
            return

        self._send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:  # noqa: N802
        if urlparse(self.path).path != "/api/query":
            self._send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 10000:
                raise ValueError("Request body must be between 1 and 10000 bytes")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            query = str(payload.get("query", "")).strip()
            if not query:
                raise ValueError("query is required")
        except (ValueError, json.JSONDecodeError, UnicodeDecodeError) as exc:
            self._send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)
            return

        result = process_query(query, allow_model=ALLOW_MODEL_IN_SERVER)
        self._send_json(
            {
                "response": result.response,
                "path": result.execution_path,
                "language": result.language,
                "blocked": result.blocked,
                "emergency": result.emergency,
            }
        )


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), AfyaIntelHandler)
    print(f"AfyaIntel HTTP service listening on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
