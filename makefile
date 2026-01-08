# Makefile
.PHONY: bootstrap format lint test run migrate airflow-up

bootstrap:
    poetry install
    pre-commit install

format:
    poetry run black src tests && poetry run isort src tests

lint:
    poetry run ruff check src tests && poetry run mypy src

test:
    poetry run pytest -q

migrate:
    poetry run alembic upgrade head

run:
    python src/runner/main.py

airflow-up:
    docker compose up -d airflow db
