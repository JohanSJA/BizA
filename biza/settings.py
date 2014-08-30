"""
Django settings for biza project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

import django.conf.global_settings as DEFAULT_SETTINGS

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jz!@i6(3%pdmb5()7**-cg!nmmh3*hcot=f@t1r#t^s1$q(#&$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Heroku recommended
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    "south",
    "widget_tweaks",
    "crispy_forms",
    # Own apps
    "utils",
    "products",
    "prices",
    "balances",
    #"purchases",
    #"wholesales",
    #"retails",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'biza.urls'

WSGI_APPLICATION = 'biza.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Heroku recommended
DATABASES = {
    "default": dj_database_url.config(),
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Heroku recommended
STATIC_ROOT = "staticfiles"

# Heroku recommended
STATIC_URL = '/static/'

# Heroku recommended
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# Heroku recommended
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Template directory
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)


# User authentication related
LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)


# Crispy form related
CRISPY_TEMPLATE_PACK = "bootstrap3"
