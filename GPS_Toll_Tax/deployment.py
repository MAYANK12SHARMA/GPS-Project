import os
from .settings import *
from .settings import BASE_DIR

# Use a fallback secret key for development

# Define the hostname without a trailing slash
WEBSITE_DEFAULT_HOSTNAME = os.getenv("WEBSITE_DEFAULT_HOSTNAME")

ALLOWED_HOSTS = [WEBSITE_DEFAULT_HOSTNAME, "localhost"]

CSRF_TRUSTED_ORIGINS = ["https://" + WEBSITE_DEFAULT_HOSTNAME]

DEBUG = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Use the correct spelling for WhiteNoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

database = os.getenv('AZURE_POSTGRESQL_CONNECTIONSTRING' )


db = dict(item.split("=") for item in database.split(" "))

# Use environment variables for sensitive database credentials
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db["dbname"],
        "USER": db["user"],
        "PASSWORD": db["password"],
        "PORT": db["port"],
        "HOST": db["host"],
        "OPTIONS": {"sslmode": "require"},
    }
}
