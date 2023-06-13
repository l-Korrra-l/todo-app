.PHONY build:
build:
	docker compose up --build

.PHONY logs:
logs:
	docker compose logs --follow

.PHONY: lint-black
lint-black:
	black --check --diff ./src

.PHONY: lint-flake8
lint-flake8:
	flake8 ./src --max-line-length 120 --per-file-ignores="__init__.py: F401" --exclude="__pycache__, alembic"

.PHONY: lint-isort
lint-isort:
	isort --check-only --diff --profile black ./src

.PHONY: lint
lint: lint-black lint-isort lint-flake8

.PHONY: fmt
fmt:
	black .
	isort . --profile black

.PHONY: migration
migration:
	docker compose exec todo_service alembic --config src/alembic.ini revision --autogenerate --message auto

.PHONY: migrate
migrate:
	docker compose exec todo_service alembic --config src/alembic.ini upgrade head
