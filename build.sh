#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
uv pip install --system --no-deps

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

celery -A djangobackend worker --loglevel=info &
celery -A djangobackend beat --loglevel=info &