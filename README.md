# python-seed-project
![Python](https://img.shields.io/badge/python-v3.12.x-orange)
![Python](https://img.shields.io/badge/platform-linux-blue)

---
**Content**
- [Getting started](#getting-started)
- [Branch strategy](#branch-strategy)
- [Documentation](#documentation)
- [CICD Pipeline ](#cicd-pipeline)
- [Build](#build)
- [Run](#run)
    - [Local development](#local-development)
    - [Production](#production)
- [References](#references)
---

## Getting started

This project tries to implement an end to end python repository that includes CI/CD pipeline using Jenkins, code quality tools integration like pylint, mypy, flake8, isort, black and mkdocs for documentation using docstrings and typing within project source code.

Also, the template project is a REST API using FastAPI framework with SQLModel for DB manipulation and versioning and Celery for asynchronous tasks support.

- Users CRUD and Calculator API: FastAPI + SQLModel
- Async tasks: Celery with Redis as message broker
- Documentation: mkdocs with docstrings and typing
- CI CD: Jenskins pipeline using telegram integration and custom branch strategy described below
- Deployment: Docker and Docker Swarm
- Code Quality: isort, black, mypy, pylint, flake8
- Testing: pytest