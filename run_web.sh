#!/bin/sh

sleep 5
python manage.py makemigrations

sleep 5
python manage.py migrate

sleep 2
python populate_db.py

sleep 2
python manage.py runserver 0.0.0.0:8000