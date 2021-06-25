# {{cookiecutter.project_name}}

## Installation

```
pip install poetry
poetry install
cp .env.example .env
```

## Run

```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Setup git hooks

Install a pre-commit hook with black and flake8 check
```
pre-commit install
```
