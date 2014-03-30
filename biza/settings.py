"""
Django settings for biza project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '40&n5^2m(in+obf&qbe*b!81rh$94kw29ce))vxxfn)p26_y&4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Allow all host headers
# According to Heroku settings
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    # Third-party add-ons / apps
    'south',
    'crispy_forms',
    # Project apps
    'products',
    'stocks',
    'prices',
    'partners',
    'purchases',
    'wholesales',
    'creators',
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
# According to Heroku settings
import dj_database_url
DATABASES = {"default": dj_database_url.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# According to Heroku settings

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of locations of template source files

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Authentication

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# Messages tags

MESSAGE_TAGS = {
    messages.DEBUG: 'warning',
    messages.ERROR: 'danger',
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# According to Heroku settings

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# For django-crispy-forms app
CRISPY_TEMPLATE_PACK = 'bootstrap3'
