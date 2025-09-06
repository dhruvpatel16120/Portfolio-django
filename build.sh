#!/bin/bash
set -e

echo "Installing dependencies..."
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip setuptools wheel
python3.9 -m pip install -r requirements.txt

echo "Running migrations..."
python3.9 manage.py migrate --noinput

echo "Collecting static..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
