from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']



SITE_ID = 1

#Databases
# MySQL Database Connections
#import codecs
#codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#Test database
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'mysql.connector.django',
        'OPTIONS': {'charset': 'utf8mb4'},
        'NAME': 'ldrportaltestdb',
		'USER': 'ldrportaladmin',
		'PASSWORD': 'ldr@app@admin',
		'HOST': 'localhost',
        'PORT': '3306',  
    }
}

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'


#static files
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








ADMIN_SITE_HEADER = "TEST ADMINISTRATOR"