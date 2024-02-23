from pathlib import Path
from split_settings.tools import include, optional
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")

DEVELOPMNET_SETTINGS = BASE_DIR / 'core/main/settings/templates/settings.dev.py'

CELERY_CONFIG_MODULE = 'main.settings.celery_settings'


include(
    'base.py',
    'swagger.py',
    'celery_settings.py',
    'logging.py',

    DEVELOPMNET_SETTINGS,)