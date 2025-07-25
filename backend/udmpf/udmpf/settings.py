import os

from dotenv import load_dotenv
from pathlib import Path
from split_settings.tools import include

from django.core.management.utils import get_random_secret_key


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&4dqo!$lklar&q6z4_jthm64@w$^zcx%s)t1)94j-g@$_trzgc'

DEBUG = True

ALLOWED_HOSTS = []

include(
    'components/apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/databases.py',
    'components/auth_password_validators.py'
)

ROOT_URLCONF = 'udmpf.urls'


WSGI_APPLICATION = 'udmpf.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
