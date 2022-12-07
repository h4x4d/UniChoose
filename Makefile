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

.PHONY: up
up: update
	docker compose up -d --build