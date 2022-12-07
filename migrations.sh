#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python UniChoose/manage.py migrate

exec "$@"