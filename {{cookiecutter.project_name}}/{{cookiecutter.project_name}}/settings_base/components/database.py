from os import environ

DATABASES = {
    "default": {
        "ENGINE": "psqlextra.backend",
        "NAME": environ.get("DB_NAME", "{{cookiecutter.project_name}}"),
        "USER": environ.get("DB_USER", "{{cookiecutter.project_name}}"),
        "PASSWORD": environ.get("DB_PASSWORD", "{{cookiecutter.project_name}}"),
        "HOST": environ.get("DB_HOST", "127.0.0.1"),
        "PORT": environ.get("DB_PORT", "5432"),
        "CONN_MAX_AGE": 600,
    }
}
