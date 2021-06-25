from os import environ
from os.path import dirname
from os.path import join

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv(join(dirname(__file__), "../../.env"))

ENV = environ.get("ENV", "development")

_base_settings = [
    "../settings_base/components/common.py",
    "../settings_base/components/database.py",
    "../settings_base/components/email.py",
    "../settings_base/components/logging.py",
    "../settings_base/components/provider.py",
    "common.py",
    "urls.py",
]

if "development" in ENV:
    _base_settings += ["../settings_base/environments/development.py"]
else:
    _base_settings += ["../settings_base/environments/production.py"]


# Include settings:
include(*_base_settings)
