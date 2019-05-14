from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tools',
        'USER' : 'jinqunlong',
        'PASSWORD' : 'jinqunlong123$%^',
        'HOST' : '120.78.70.205',
        'PORT' : '33306',
    }
}