"""
Django settings for {{cookiecutter.project_name}} project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import logging
import os
import sys

from corsheaders.defaults import default_headers
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = [("infra", "infra@bimdata.io")]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "y^1o_0dz-vi7omq$6e@7%mhnj*mc4v+n8+3pvcxwcx-y#p50ty")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
CONSOLE_LOG_LEVEL = logging.INFO

ENV = os.getenv("ENV", "development")

if os.getenv("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
else:
    ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = default_headers + ("Content-Encoding",)


# Application definition

INSTALLED_APPS = [
    "user",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
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

ROOT_URLCONF = "{{cookiecutter.project_name}}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "{{cookiecutter.project_name}}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "{{cookiecutter.project_name}}"),
        "USER": os.getenv("DB_USER", "{{cookiecutter.project_name}}"),
        "PASSWORD": os.getenv("DB_PASSWORD", "{{cookiecutter.project_name}}"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", 5432),
        "CONN_MAX_AGE": 600,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },  # noqa E231
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},  # noqa E231
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},  # noqa E231
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},  # noqa E231
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "statics"

OIDC_OP_ISSUER = (
    os.getenv("OIDC_OP_ISSUER", "https://iam-staging.bimdata.io") + "/auth/realms/bimdata"
)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("oidc_auth.authentication.JSONWebTokenAuthentication",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
}


OIDC_AUTH = {
    # Specify OpenID Connect endpoint. Configuration will be
    # automatically done based on the discovery document found
    # at <endpoint>/.well-known/openid-configuration
    "OIDC_ENDPOINT": OIDC_OP_ISSUER,
    # Accepted audiences the ID Tokens can be issued to
    "OIDC_AUDIENCES": ("account",),
    # (Optional) Function that resolves id_token into user.
    # This function receives a request and an id_token dict and expects to
    # return a User object. The default implementation tries to find the user
    # based on username (natural key) taken from the 'sub'-claim of the
    # id_token.
    "OIDC_RESOLVE_USER_FUNCTION": "user.auth.get_user_by_id",
    # (Optional) Number of seconds in the past valid tokens can be
    # issued (default 600)
    "OIDC_LEEWAY": 60 * 60,  # 60 minutes
    # (Optional) Time before signing keys will be refreshed (default 24 hrs)
    "OIDC_JWKS_EXPIRATION_TIME": 24 * 60 * 60,
    # (Optional) Time before bearer token validity is verified again (default 10 minutes)
    "OIDC_BEARER_TOKEN_EXPIRATION_TIME": 10 * 60,
    # (Optional) Token prefix in JWT authorization header (default 'JWT')
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    # (Optional) Which Django cache to use
    "OIDC_CACHE_NAME": "default",
    # (Optional) A cache key prefix when storing and retrieving cached values
    "OIDC_CACHE_PREFIX": "oidc_auth.",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {"format": "[django] %(levelname)s %(asctime)s %(module)s %(message)s"}
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": CONSOLE_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        },
        # Warning messages are sent to admin emails
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django.utils.autoreload": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.security.DisallowedHost": {"handlers": ["null"], "propagate": False},
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# LOGGING EMAIL
SERVER_EMAIL = "bug@bimdata.io"
EMAIL_HOST = "smtp.mandrillapp.com"
EMAIL_HOST_PASSWORD = os.getenv("MANDRILL_SMTP_KEY", False)
EMAIL_HOST_USER = "BIMData.io"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

if "development" in ENV:
    DEBUG = True
    DEBUG_PROPAGATE_EXCEPTIONS = True
    CONSOLE_LOG_LEVEL = logging.DEBUG