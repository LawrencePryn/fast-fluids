$(VERBOSE).SILENT:

update:
	poetry install --sync

run:
	poetry run python -m fast_fluids

ruff:
	@echo === Ruff ===
	-(poetry run ruff format) && echo "\033[92mSuccess!\033[0m"

black:
	@echo === Black ===
	-poetry run black .

mypy:
	@echo === Mypy ===
	-poetry run mypy

test:
	@echo === Pytest ===
	-poetry run pytest

lint: ruff black mypy
