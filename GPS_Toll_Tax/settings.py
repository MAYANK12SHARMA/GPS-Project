import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "9m@5up$+f%39=3&i#9*1pw+d&h4^2*2v#axm%9#ft&0^o+(f!v"

DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 3  # Update with your site ID from Django admin


MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "GPS_Toll_app",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "CLIENT_ID": "315395298304-ltb9djmc1p2qcvebenee4c6rrr6ndvap.apps.googleusercontent.com",
        "SECRET": "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",
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]



ROOT_URLCONF = "GPS_Toll_Tax.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ],  # Adjust templates directory path
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

WSGI_APPLICATION = "GPS_Toll_Tax.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Adjust static files directory path
    os.path.join(BASE_DIR, "static/Routes"),  # Adjust static files directory path
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# # Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'live.smtp.mailtrap.io'  # Update with your email host
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'api'  # Update with your email host user
# EMAIL_HOST_PASSWORD = '41a94483113e0f93cb4a42b88d0eb3cd'  # Update with your email host password
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

# Authentication backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Redirect URLs
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


#!  --------------------------------------- Email settings-------------------------------------------------


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = 'b46ce973875c14'
# EMAIL_HOST_PASSWORD = 'c8e598f88f69f7'
# EMAIL_PORT = '2525'


# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )


# LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/'  # Adjust this URL according to your project structure


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "live.smtp.mailtrap.io"
EMAIL_HOST_USER = "api"
EMAIL_HOST_PASSWORD = "41a94483113e0f93cb4a42b88d0eb3cd"
EMAIL_PORT = "587"
EMAIL_USING_TLS = True
EMAIL_USE_SSL = False


# ? ---------------------------------- Media Folder --------------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = [
    os.path.join(BASE_DIR, "media"),
    os.path.join(BASE_DIR, "media/Coordinates"),
]


SOCIALACCOUNT_ADAPTER = "GPS_Toll_app.adapters.MySocialAccountAdapter"

