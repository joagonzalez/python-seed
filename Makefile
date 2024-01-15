run:
	python run.py

build:
	docker build -t joagonzalez/calculator:0.0.1 .

install:
	pip install -r requirements.txt

typehint:
	mypy src/ tests/

test:
	pytest tests/ -v --cov

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
	rm -rf .*_cache .*coverage

checklist: typehint lint pep8 black isort test clean

.PHONY: checklist