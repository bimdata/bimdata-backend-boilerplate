from os import environ

from corsheaders.defaults import default_headers

from {{cookiecutter.project_name}}.settings_base.components import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ENV = environ.get("ENV", "development")
ADMIN_INTERFACE = environ.get("ADMIN_INTERFACE", False)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("SECRET_KEY", "y^1o_0dz-vi7omq$6e@7%mhnj*mc4v+n8+3pvcxwcx-y#p50ty")

ADMIN_URL = environ.get("ADMIN_URL", "http://localhost:8000/admin")

if environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS").split(",")


INSTALLED_APPS = [
    "user",
    "webhook",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "health_check",
    "health_check.db",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = default_headers + ("Content-Encoding",)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


ROOT_URLCONF = "{{cookiecutter.project_name}}.urls"
WSGI_APPLICATION = "{{cookiecutter.project_name}}.wsgi.application"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = "statics"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
            ]
        },
    }
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("oidc_auth.authentication.JSONWebTokenAuthentication",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

BCF_DATE_FORMAT = ("%m/%d/%Y",)

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False


WEBHOOKS_SECRET = environ.get("WEBHOOKS_SECRET", "123")
