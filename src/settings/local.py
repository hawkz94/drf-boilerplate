from .base import *


ALLOWED_HOSTS = []
DEBUG = True
### DATABASE LOCAL ####
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teste',
        'USER': 'newuser',
        'PASSWORD': 'passsword',
        'HOST': '127.0.0.1',
        'PORT': '', # 8000 is default
    }
}