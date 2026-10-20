# Customer Accounts Microservice

![Build Status](https://github.com/<YOUR-USERNAME>/<YOUR-REPO>/actions/workflows/ci-build.yaml/badge.svg)

RESTful Customer Accounts service built with Flask, tested with nose, secured with Flask-Talisman and CORS,
containerized with Docker, and deployed to Kubernetes via a Tekton pipeline.

## Endpoints
| Method | Path | Purpose |
|---|---|---|
| POST | /accounts | Create |
| GET | /accounts | List |
| GET | /accounts/<id> | Read |
| PUT | /accounts/<id> | Update |
| DELETE | /accounts/<id> | Delete |
| GET | /health | Health check |

## Run locally
```bash
python3.9 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
nosetests
flask --app service run --port 5000
```
