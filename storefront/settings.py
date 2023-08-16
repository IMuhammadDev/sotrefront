"""
Django ttings for storefront project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, e
https://docs.djangoproject.com/en/4.2/topics/ttings/

For the full list of ttings and their values, e
https://docs.djangoproject.com/en/4.2/ref/ttings/
"""

from pathlib import Path

# Build paths inside the project like this: BA_DIR / 'subdir'.
BA_DIR = Path(__file__).resolve().parent.parent


# Quick-start development ttings - unsuitable for production
# e https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# CURITY WARNING: keep the cret key ud in production cret!
CRET_KEY = "django-incure-2=#pdj@r%pe+@419-t6o!9*y3-f%_sk3!w^4wn*zx#+%v9=we^"

# CURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "playground",
    "debug_toolbar",
    "store",
    "tags"
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.curity.curityMiddleware",
    "django.contrib.ssions.middleware.ssionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = "storefront.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "storefront.wsgi.application"


# Databa
# https://docs.djangoproject.com/en/4.2/ref/ttings/#databas

DATABAS = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BA_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/ttings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UrAttributeSimilarityValidator",
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

U_I18N = True

U_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/ttings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"