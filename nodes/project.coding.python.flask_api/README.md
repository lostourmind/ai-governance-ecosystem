# Flask API Node — Validation Test

Path: `nodes/project.coding.python.flask_api`  
Last updated: 2025-08-31T18:02:32-05:00

## Purpose
Validates the node template system with real Flask API knowledge. Covers config, auth, DB, validation, CORS, logging.

## Files
1. `knowledge_base.yaml` — authoritative guidance and criteria.
2. `supplement_prompt.md` — injection text for handoffs.
3. `constraints.yaml` — enforceable limits and deps.
4. `README.md` — usage.

## Usage
1. Place this folder under your repository’s `nodes/` directory.
2. Ensure your framework scans `nodes/**/knowledge_base.yaml` for `node_info.path` and merges `supplement_prompt.md` into the universal wrapper when the query matches Flask API intents.
3. Export `FLASK_ENV`, `SECRET_KEY`, `DATABASE_URL`, and `JWT_SECRET_KEY` in environment.

### Minimal App Skeleton (reference)
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL"),
        SECRET_KEY=os.getenv("SECRET_KEY"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if os.getenv("ENABLE_CORS", "1") == "1":
        CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})
    db.init_app(app)
    # register blueprints here
    return app
```

### Validation Runbook
- Environment variables present and loaded.
- Auth middleware wired (JWT or flask-login).
- Marshmallow or Pydantic schemas applied at endpoints.
- Errors return sanitized JSON; stack traces only in logs.
- ORM used with parameters; no string concatenation.
- CORS policy matches deployment target.
- Basic rate limiting in place for public endpoints.

### Common Pitfalls to Check
- `debug=True` in production.
- Missing input validation.
- Secrets hardcoded.
- Leaky error messages.
- Direct SQL strings.

## Handoff Test
Use the test query:
> I need help setting up a basic Python Flask API with user authentication and database connection. What are the key considerations and common pitfalls?

Expected: node detection, knowledge injection, and guidance aligned to `validation_criteria` in `knowledge_base.yaml`.
