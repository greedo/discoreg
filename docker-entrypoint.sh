#!/bin/bash

# Collect static files
echo "Collect static files"
python3 discoreg/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 discoreg/manage.py migrate

# Start server
echo "Starting server"
gunicorn --pythonpath discoreg discoreg.wsgi --bind 0.0.0.0:8000 --log-file -
