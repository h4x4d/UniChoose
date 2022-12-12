#!/bin/bash

echo "Waiting for postgres..."
python UniChoose/manage.py collectstatic --no-input --clear

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python UniChoose/manage.py migrate

exec "$@"