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
build-action: copy_migration down
	docker compose up -d --build


.PHONY: build
build: build-action
	docker compose cp /root/UniChoose/UniChoose/fixtures/fixture.json  web:/code/UniChoose/fixtures/fixture.json

.PHONY: up
up:
	docker compose up -d --build

.PHONY: clear
clear:
	cd ./UniChoose && rd /s /q "allure-results/"

.PHONY: test
test: clear
	cd ./UniChoose && pytest --alluredir=allure-results -s -v

.PHONY: generate
generate: test
	cd ./UniChoose && allure generate --clean
