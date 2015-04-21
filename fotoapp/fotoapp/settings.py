"""
Django settings for fotoapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fotos',
    'eventos'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fotoapp.urls'

WSGI_APPLICATION = 'fotoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if ON_OPENSHIFT:
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fotoapp',
            'USER': os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
            'PASSWORD': os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
            'HOST': os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST'),
            'PORT': os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT'),
        }
    }
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # If you want to use MySQL
            'NAME': 'fotoapp',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',  # this will be the case for MySQL
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zui_4ca4^&b!+5vam@pj@dn1q__79+^zcke*hn==8e02640y^r'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static', 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, '', 'static'),)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, '', 'templates'),)



AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_COOKIE_AGE = 86400 # sec
# SESSION_COOKIE_DOMAIN = None
# SESSION_COOKIE_NAME = 'DSESSIONID'
# SESSION_COOKIE_SECURE = False
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.messages.context_processors.messages',
#     )