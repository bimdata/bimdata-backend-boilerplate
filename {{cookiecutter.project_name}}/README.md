# {{cookiecutter.project_name}}

## Install

- Download poetry: https://python-poetry.org/docs/#installation
- `poetry shell`
- `poetry install` : install all requirements

## Usage

- `./manage.py migrate`
- `./manage.py createsuperuser`
- `./manage.py runserver`
- `./manage.py test`

NB: `ENV` env-var can be used to customize `runserver` behaviour:

- `ENV="development"` enable logs and debug=True

NB: `ADMIN_INTERFACE` is a boolean for whether or not to run the django admin interface:

- `ADMIN_INTERFACE=True` to activate the admin interface on the same server.
- Otherwise, admin interface is not accessible directly. You have to run it manually on an other port with:

```sh
./manage.py runserver 8002 --settings={{cookiecutter.project_name}}.settings_admin
```

## The .env file

The `.env` file is a representation of additionnal ENV variable in order to override default config.
You can duplicate `.env.example` in `.env` and customize your config

## Setup git hooks

Install a pre-commit hook with black and flake8 check
```
pre-commit install
```
