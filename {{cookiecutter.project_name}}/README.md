# {{cookiecutter.project_name}}

## Installation

```
pip install poetry
poetry install
```

## Run

```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Run with docker-compose

```
docker-compose up -d
```

And navigate to localhost:4242

## Setup git hooks

Install a pre-commit hook with black and flake8 check
```
pre-commit install
```
