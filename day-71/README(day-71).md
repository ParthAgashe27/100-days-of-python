# Day 71 — Deploying the Blog Capstone to Production

Deployed the Flask blog capstone (Days 68-69) to a live web service using Render.

🔗 Live: https://one00-days-of-python-cs6z.onrender.com

## What this covers
- Configured a WSGI server (gunicorn) via a Procfile
- Moved sensitive config (SECRET_KEY, database URI) to environment variables instead of hardcoding
- Pushed the project to GitHub and connected it to Render for deployment
- Migrated from local SQLite to a managed PostgreSQL database, since SQLite's file storage doesn't persist reliably on hosting platforms (files get wiped periodically)

## Stack
- Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-CKEditor
- Gunicorn (WSGI server)
- PostgreSQL (production DB) / SQLite (local dev fallback)
- Hosted on Render (free tier)

## Notes
- Free-tier Render Postgres expires after 30 days — will need reprovisioning if this stops working after that window.
- Free-tier web service spins down after inactivity, so first load after idle time can be slow (~50s).
