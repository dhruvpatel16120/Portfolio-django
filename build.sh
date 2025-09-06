#!/bin/bash
set -e  # stop on first error

echo "Installing pip if missing..."
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip setuptools wheel

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Applying migrations..."
python3.9 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
