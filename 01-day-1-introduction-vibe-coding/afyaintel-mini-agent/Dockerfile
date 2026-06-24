FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    AFYAINTEL_ALLOW_MODEL=false

WORKDIR /app

COPY pyproject.toml README.md ./
COPY afyaintel ./afyaintel
COPY main.py server.py sample_stock.csv tool_manifest.json ./

RUN pip install --no-cache-dir "google-genai>=2.0.0" "python-dotenv>=1.0.1"

EXPOSE 8080

CMD ["python", "server.py"]
