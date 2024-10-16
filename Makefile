.PHONY: run test

run:
	python -m src.cli.main "*/15 0 1,15 * 1-5 /usr/bin/find"

test:
	pytest

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

docs:
	python -m pydoc -w src
