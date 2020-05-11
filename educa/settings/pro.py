from .base import *


DEBUG = False


ADMINS = (
    ('Ayman Abd El-Hadi', 'hunter.me33@gmail.com'),
)


ALLOWED_HOSTS = ['.educa-prj.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True