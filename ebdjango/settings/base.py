"""
Django settings for ebdjango project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__,os.pardir))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e45*=5v5q=f9_op$i!)e+_3d25r-n2nw4kh^q63eevj16*i!!g' 

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS moved to subfolders

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'multiselectfield',
    'django_user_agents',
    'rest_framework',
    'crispy_forms',
    'registration',
    'portal.apps.PortalConfig',
    'helpdesk.apps.helpdeskConfig',
    'userapp.apps.userappConfig',
    'project.apps.ProjectConfig',
    'api.apps.ApiConfig',
    #'helloworld',
]

#SITE_ID is moved to sub folders

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'ebdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'ebdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


#Database moved to local and prod





# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = '/home/ec2-user/eb-virt/ebdjango/ebsrc/static'

LOGIN_REDIRECT_URL = '/apps_list/'
LOGIN_URL = '/accounts/login/'

#crispy form settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#Django Registration redux settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[LDR Portal User Account Registration]'
SEND_ACTIVATION_EMAIL = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

#Settings for Email Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'itservices@ldr.sg'
EMAIL_HOST_PASSWORD = '7()fullfold'
SERVER_EMAIL = 'itservices@ldr.sg'
DEFAULT_FROM_EMAIL = 'itservices@ldr.sg'


#REST framework webservice page size
#REST_FRAMEWORK = {
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#    'PAGE_SIZE': 5
#}

# message tags for bootstrap3
#try:
#    from django.contrib.messages import constants as messages
#except Exception as e:
#    pass
#    MESSAGE_TAGS = {
#    messages.DEBUG: 'alert-info',
#    messages.INFO: 'alert-info',
#    messages.SUCCESS: 'alert-success',
#    messages.WARNING: 'alert-warning',
#    messages.ERROR: 'alert-danger',
#}

#API return records
#API_LIMIT_PER_PAGE = 50
#API_LIMIT_PER_PAGE = 0
#TASTYPIE_ALLOW_MISSING_SLASH = True
#TASTYPIE_ABSTRACT_APIKEY = True


#AUTO_LOGOUT_DELAY = 30

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum number of GET/POST parameters that will be read before a
# SuspiciousOperation (TooManyFieldsSent) is raised.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

