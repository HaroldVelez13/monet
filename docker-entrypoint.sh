#!/bin/sh

sleep 0.1
echo "Init makemigrations alls"
python manage.py makemigrations

echo "Init makemigrations alls"
python manage.py makemigrations api

sleep 0.1
echo "Init migrate "
python manage.py migrate

sleep 0.1
echo "Init migrate api"
python manage.py migrate api

sleep 0.1
echo "Init Super Admin Start Basic Configuration"
python manage.py monet_init

sleep 0.1
echo "Init Testing"
python manage.py test

exec "$@"