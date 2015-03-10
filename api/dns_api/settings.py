"""
Django settings for dns_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
myhost = socket.gethostname() ##This is to use as ALLOWED HOST. Change to your vhost or domain name where this is run.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sk2dg289&=9n%j&7w4(ypkzgs#&nvc0=6a63a+7#4z7=@#509c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [myhost] ##Change to your vhostname 


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'getdata',
    'ui'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dns_api.urls'

WSGI_APPLICATION = 'dns_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
				'ENGINE': 'django.db.backends.mysql',
				'NAME': 'ddns_search',
				'USER': 'root',
				'PASSWORD': 'qazplm123',
				'HOST': ''
    },
    'users': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'userdata',
        'USER': 'root',
        'PASSWORD': 'qazplm123',
        'HOST': ''
    }
}
	

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'




