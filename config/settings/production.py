from .base import *

DEBUG = config("DEBUG")

ALLOWED_HOSTS = [config("ALLOWED_HOST")]

INSTALLED_APPS += [
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT"),
    }
}
