.PHONY: run test

run:
	python -m src.cli.main "*/15 0 1,15 * 1-5 /usr/bin/find"

logs:
	python -m src.cli.main "*/15 0 1,15 * 1-5 /usr/bin/find" --log

test:
	pytest

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

docs:
	python -m pydoc -w src

lint:
	flake8 src

autofix:
	autoflake8 --in-place --recursive src

format:
	black src
