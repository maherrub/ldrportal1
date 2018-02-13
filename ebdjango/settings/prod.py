from .base import *
#SECRET_KEY='byu%f0^45pzqb(3rj(_^r3!d=g9jl!n^1#4g)8#8br)(f4h3zo'

DEBUG = False
ALLOWED_HOSTS = ['localhost',
                'portal.ldr.sg',
                'ldrportalapp.ap-southeast-1.elasticbeanstalk.com',
                'http://ldrportalapp.ap-southeast-1.elasticbeanstalk.com/',
                'http://portal.ldr.sg/',
                'www.portal.ldr.sg/',
                '13.229.158.225',
                'ip-172-30-0-43.ap-southeast-1.compute.internal',
                'https://ldrportal-staticfiles.s3.amazonaws.com',
                'ldrportal-staticfiles.s3.amazonaws.com',
                
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
        'NAME': config('DB_NAME'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST': config('DB_HOST'),
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

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


AWS_LOCATION = 'media'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = "https://%s/%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION, MEDIAFILES_LOCATION)


STATIC_URL = '/static/'
STATIC_ROOT = '/home/ec2-user/eb-virt/ebdjango/ebsrc/static'

STATICFILES_DIRS = [
    ('css', os.path.join(STATIC_ROOT , 'css')),
	('js', os.path.join(STATIC_ROOT , 'js')),
	('images', os.path.join(STATIC_ROOT , 'images')),
    ('video', os.path.join(STATIC_ROOT , 'video')),
    ('audio', os.path.join(STATIC_ROOT , 'audio')),
    ('admin', os.path.join(STATIC_ROOT , 'admin')),

]


ADMIN_SITE_HEADER = "PROD ADMINISTRATOR"