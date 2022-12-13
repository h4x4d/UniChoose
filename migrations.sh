#!/bin/bash

echo "Waiting for postgres..."
python UniChoose/manage.py collectstatic --no-input --clear

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python UniChoose/manage.py migrate
docker compose exec web python -Xutf8 UniChoose/manage.py loaddata UniChoose/fixtures/fixture.json

exec "$@"