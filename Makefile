run:
	python run.py

build:
	docker build -t joagonzalez/calculator:0.0.1 .

install:
	pip install -r requirements.txt

typehint:
	mypy src/ tests/

test-local:
	pytest tests/ -v --cov

test:
	pytest tests/ -v --cov --cov-report=xml:coverage.xml

pep8:
	flake8 src/ tests/ --config pyproject.toml

lint:
	pylint src/ tests/

black:
	black src/ tests/

isort:
	isort src/ tests/ -v

doc:
	mkdocs serve

build-doc:
	docker-compose build documentation && make clean

build-jenkins-builder:
	docker build -t joagonzalez/jenkins_builder:python-3.11.4 build/jenkins_builder/ && docker push joagonzalez/jenkins_builder:python-3.11.4

deploy-local:
	export GIT_COMMIT_SHORT=0.0.1 && \
	export CURRENT_BUILD_NUMBER=666 && \
	export REGISTRY_IMAGE=joagonzalez/python-seed-doc && \
	docker stack deploy -c docker-compose.yml calculator

deploy:
	docker stack deploy -c docker-compose.yml calculator

clean:
	rm -rf .*_cache coverage.xml .*coverage site report

checklist: typehint lint pep8 black isort test clean

code-quality: typehint lint pep8 black isort clean

.PHONY: checklist