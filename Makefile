typehint:
	mypy src/ tests/

test:
	pytest tests/ -v

pep8:
	flake8 src/ tests/

lint:
	pylint src/ tests/

black:
	black src/ tests/

isort:
	isort src/ tests/ -v

doc:
	mkdocs serve

build-doc:
	mkdocs build

clean:
	rm -rf .*_cache

checklist: typehint lint pep8 black isort test clean

.PHONY: checklist