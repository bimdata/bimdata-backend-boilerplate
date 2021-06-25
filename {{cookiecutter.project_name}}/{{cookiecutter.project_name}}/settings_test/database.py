from os import environ


DATABASES = {
    "default": {
        "ENGINE": "psqlextra.backend",
        "NAME": environ.get("TEST_DB_NAME", "{{cookiecutter.project_name}}test"),
        "USER": environ.get("TEST_DB_USER", "{{cookiecutter.project_name}}"),
        "PASSWORD": environ.get("TEST_DB_PASSWORD", "{{cookiecutter.project_name}}"),
        "HOST": environ.get("TEST_DB_HOST", "127.0.0.1"),
        "PORT": environ.get("TEST_DB_PORT", "5432"),
    }
}
