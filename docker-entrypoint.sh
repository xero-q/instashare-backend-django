#!/usr/bin/env bash
set -e

uv run python manage.py migrate
uv run python manage.py collectstatic --no-input

# Run Celery worker and beat in background
uv run celery -A djangobackend worker --loglevel=info &
uv run celery -A djangobackend beat --loglevel=info &

# Wait for background processes and start Django
uv run python manage.py runserver 0.0.0.0:8000
