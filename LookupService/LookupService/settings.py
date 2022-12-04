import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

## TEST MODE
# LOCAL_TEST : TEST CODE 작성시
# LOCAL : 로컬 서버 돌릴 때 
# PRODUCTION : 배포용
MODE = "LOCAL" 

# SECURITY WARNING: keep the secret key used in production secret!
if MODE=="LOCAL_TEST" or MODE=='LOCAL':
    SECRET_KEY = "django-insecure-h!ojgwre1e58)16&bmuve3mn#dnll#dt&eoo14!rq2s3bffkn2"
else: # MODE = PRODUCTION
    SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if MODE == 'PRODUCTION':
    ALLOWED_HOSTS = ["*"]
else: # MODE = LOCAL or LOCAL_TEST
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sharedb',
    "consumer",
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE' : 2,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Django DEBUG TOOLBAR
if MODE == 'PRODUCTION':
    pass
else: # MODE = LOCAL or LOCAL_TEST
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_CONFIG = { "SHOW_TOOLBAR_CALLBACK": lambda request: True, }
    INTERNAL_IPS = ['127.0.0.1',]
    
ROOT_URLCONF = 'LookupService.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LookupService.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

''' # sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}
'''

# PostgreSQL
if MODE == 'LOCAL_TEST' or MODE == 'LOCAL':
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("DB_ENGINE"),
            'NAME': os.environ.get("DB_NAME"), # Schema Name
            'USER': os.environ.get("DB_USER"),
            'PASSWORD': os.environ.get("DB_PASSWORD"), # PASSWORD NAME
            'HOST':os.environ.get("DB_HOST"),
            'PORT':os.environ.get("DB_PORT"),
        }
    }
elif MODE == 'PRODUCTION':
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("PRODUCTION_ENGINE"),
            'NAME': os.environ.get("PRODUCTION_NAME"), # Schema Name
            'USER': os.environ.get("PRODUCTION_USER"),
            'PASSWORD': os.environ.get("PRODUCTION_PASSWORD"), # PASSWORD
            'HOST':os.environ.get("PRODUCTION_HOST"),
            'PORT':os.environ.get("PRODUCTION_PORT"),
        }
    }
    
CACHES = {
    'default':{
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://'+ os.environ.get("AWS_HOST") +':6379',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_I18N = True

USE_TZ = False  # 원래 True KOREA Time을 위한 False 설정


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "sharedb.User"

