from os.path import dirname
from os.path import join

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv(join(dirname(__file__), "../../.env"))

_base_settings = [
    "../settings_base/components/*.py",
    "./*.py",
]

# Include settings:
include(*_base_settings)
