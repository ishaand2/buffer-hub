"""
Django settings for buffer_hub project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ki#f^y50-0-*u16#$4n!a8vyb5t1p+=y92&zihy5-#$1r)zdk6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'buffer_hub',
    'admin',
    'admin.login',
    'admin.dashboard',
    'admin.genre',
    'admin.mood',
    'admin.artist',
    'admin.song',
    'admin.user',
    'admin.favorite',
    'admin.homepage',
    'api',
    'rest_framework',
    'temp'
]

AUTH_USER_MODEL = "user.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buffer_hub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'buffer_hub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'i0i2syopai9pjbtu',
#         'USER': 'ap74tui5ygxnn8fc',
#         'PASSWORD': 'qzgpa8662t9k06p8',
#         'HOST': 'a5s42n4idx9husyc.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buffer_hub',
        'USER': 'djangoInterface',
        'PASSWORD': 'Django123!',
        'HOST': 'SG-bufferhub-36641.servers.mongodirector.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static/'),
)



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS Configuration

# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = 'django-files-bucket'

# AWS_S3_FILE_OVERWRITE = False

# AWS_DEFAULT_ACL = None

# # AWS_S3_SIGNATURE_VERSION = 's3v4'

# AWS_S3_REGION_NAME = 'us-east-2'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




# DropBox Configuration

# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

# DROPBOX_OAUTH2_TOKEN = '6CvkSojDEyAAAAAAAAAAN_h31MKLLmumYWDC5j0j8smqafT01OYrC7lUdr1uY_IW'

# DROPBOX_TIMEOUT = None

django_heroku.settings(locals())