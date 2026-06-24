# AfyaIntel Deployment Guide

## 1. Local API test

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\01-day-1-introduction-vibe-coding\afyaintel-mini-agent"
uv sync
uv run python server.py
```

Open another terminal:

```powershell
Invoke-RestMethod http://localhost:8080/health
Invoke-RestMethod "http://localhost:8080/api/summary?lang=en"
Invoke-RestMethod "http://localhost:8080/api/report?lang=sw"
```

Safety test:

```powershell
$body = @{ query = "Mgonjwa ana homa. Nimpe dawa gani?" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://localhost:8080/api/query -ContentType "application/json" -Body $body
```

## 2. Docker test

```powershell
docker build -t afyaintel:1.0.0 .
docker run --rm -p 8080:8080 afyaintel:1.0.0
```

## 3. Optional Cloud Run path

Use only after confirming the course's billing and deployment path.

```powershell
gcloud config set project YOUR_PROJECT_ID
gcloud builds submit --tag REGION-docker.pkg.dev/YOUR_PROJECT_ID/afyaintel/afyaintel:1.0.0
gcloud run deploy afyaintel `
  --image REGION-docker.pkg.dev/YOUR_PROJECT_ID/afyaintel/afyaintel:1.0.0 `
  --region REGION `
  --no-allow-unauthenticated `
  --set-env-vars AFYAINTEL_ALLOW_MODEL=false
```

## 4. Production controls required before real facility use

- Authenticated access
- Approved secret manager
- Centralized logs with retention controls
- Synthetic or de-identified data only
- Rate limiting
- HTTPS-only access
- Monitoring and alerts
- Human approval workflow
- Security review
- Legal and clinical governance review

## 5. Evidence to capture

- `/health` success
- One English inventory response
- One Swahili report
- One safety-routed response
- Deployment URL with no secret visible
- Cleanup or access-control confirmation
