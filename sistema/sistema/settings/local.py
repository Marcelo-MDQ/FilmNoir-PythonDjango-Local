from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# vuelvo a MySql
# DATABASES = {  
#    'default': {  
#      'ENGINE': 'django.db.backends.sqlite3',  
#      'NAME': 'db.sqlite3',  
#    }  
#  }

DATABASES = {  
   'default': {  
     'ENGINE': 'django.db.backends.mysql',  
     'NAME': 'filmnoir',  
     'USER': 'root',
     'PASSWORD': '',
     'HOST': 'localhost',
     'PORT': 3306,
   }  
 }
