.PHONY: install test lint type check run clean

install:
	pip install -e ".[dev]"

test:
	pytest --cov=src --cov-report=term-missing

lint:
	flake8 src tests

type:
	mypy src

check: test lint type

run:
	python -m src.main

clean:
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
