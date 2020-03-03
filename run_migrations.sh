#!/usr/bin/env bash
python manage.py makemigrations MembersServiceApp
python manage.py migrate MembersServiceApp