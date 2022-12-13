.PHONY: install
install:
	poetry install

.PHONY: install-dev
install-dev:
	make install-dev

.PHONY: pip-install
pip-install:
	pip install -r requirements.txt

.PHONY: pip-install-dev
pip-install-dev:
	pip install -r requirements-dev.txt

.PHONY: use
use: install
	poetry run python manage.py runserver

.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: pip-run
pip-run:
	python manage.py runserver

.PHONY: update
update:
	git pull

.PHONY: down
down:
	docker compose down -v

.PHONY: create_migration
create_migration:
	docker compose exec web python -Xutf8 UniChoose/manage.py dumpdata departments users universities -o UniChoose/fixtures/fixture.json


.PHONY: copy_migration
copy_migration: create_migration
	docker compose cp web:/code/UniChoose/fixtures/fixture.json /root/UniChoose/UniChoose/fixtures/fixture.json


.PHONY: build-action
build-action: update down
	docker compose up -d --build

.PHONY: copy_migration_to_server
copy_migration_to_server: build-action
	docker compose cp /root/UniChoose/UniChoose/fixtures/fixture.json  web:/code/UniChoose/fixtures/fixture.json


.PHONY: build
build: copy_migration_to_server
	docker compose exec web python -Xutf8 UniChoose/manage.py loaddata UniChoose/fixtures/fixture.json

.PHONY: up
up: update
	docker compose up -d --build