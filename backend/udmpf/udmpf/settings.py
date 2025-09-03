import os

from dotenv import load_dotenv
from pathlib import Path
from split_settings.tools import include

from django.core.management.utils import get_random_secret_key


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS',
    'localhost, 127.0.0.1'
).split(', ')

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

STATIC_URL = '/staticfiles/'

STATIC_ROOT = Path('/backend_static')

# STATIC_URL = '/static/'
#
# STATIC_ROOT = BASE_DIR / 'collected_static'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

LOGIN_REDIRECT_URL = 'phonebook:index'
