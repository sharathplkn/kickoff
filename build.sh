#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Run migrations (This creates the DB tables)
python manage.py migrate

# Collect static files (Required for CSS/JS to work)
python manage.py collectstatic --no-input