from .base import *
#SECRET_KEY='byu%f0^45pzqb(3rj(_^r3!d=g9jl!n^1#4g)8#8br)(f4h3zo'

DEBUG = False
ALLOWED_HOSTS = ['localhost',
                'portal.ldr.sg',
                'ldrportalapp.ap-southeast-1.elasticbeanstalk.com',
                'http://ldrportalapp.ap-southeast-1.elasticbeanstalk.com/',
                'http://portal.ldr.sg/',
                '13.229.158.225',
                ]


SITE_ID = 1
ADMINS = (
	('maherrub', 'ruban@ldr.sg'),
)

#aws prod database
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'mysql.connector.django',
        'OPTIONS': {'charset': 'utf8mb4'},
        'NAME': 'ldrportaldb',
		'USER': 'ldrportaladmin',
		'PASSWORD': 'ldr$app$admin',
		'HOST': 'sgldrportaldbinstance.cwx1ekdurpdu.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',  
    }
}


# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'ldrportalapp.ap-southeast-1.elasticbeanstalk.com:11211',
    }
}

# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/ec2-user/eb-virt/ebdjango/ebsrc/static'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ec2-user/eb-virt/ebdjango/ebsrc/media'

ADMIN_SITE_HEADER = "PROD ADMINISTRATOR"