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

checklist: typehint lint pep8 black isort test

.PHONY: checklist