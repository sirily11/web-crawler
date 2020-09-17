import django
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = [
    'website'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'website.db',
    }
}

settings.configure(
    INSTALLED_APPS=INSTALLED_APPS,
    DATABASES=DATABASES,
)
SECRET_KEY = "huiashiduhasui"

django.setup()
