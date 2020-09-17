from {{cookiecutter.project_name}} import settings_admin as settings


def from_settings(request):
    return {
        "ENVIRONMENT_NAME": settings.ENV,
        "ENVIRONMENT_COLOR": settings.ENV_COLOR,
    }
