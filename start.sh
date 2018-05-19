#!/bin/sh

echo "Creating migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Running server"
python3 manage.py runserver 0.0.0.0:8000
