from .base import *

#SECRET_KEY='9xbc&jl&&krl@5gps*dk=&2f-$@+jfme+rqb+5w#d918e*!93b'

DEBUG = True
ALLOWED_HOSTS = ['*']

SITE_ID = 1

#Databases
#Dev
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Cache backend is optional, but recommended to speed up user agent parsing
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}
# cache alias will be used. Set to `None` to disable caching.
#USER_AGENTS_CACHE = 'default'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
	('css', os.path.join(STATIC_ROOT , 'css')),
	('js', os.path.join(STATIC_ROOT , 'js')),
	('images', os.path.join(STATIC_ROOT , 'images')),
    ('video', os.path.join(STATIC_ROOT , 'video')),
    ('audio', os.path.join(STATIC_ROOT , 'audio')),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




ADMIN_SITE_HEADER = "DEV ADMINISTRATOR"