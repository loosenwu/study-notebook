"""
Django settings for swiper project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$gybxt1($!)w=0=(7+@-f(wz&9t*z7joo41jike@3me6wm!nx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'corsheaders',
    'user',
    'social',
    'vip',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'common.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.LogicErrorMiddleware',
    'common.middleware.AuthMiddleware',
]

ROOT_URLCONF = 'swiper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'swiper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Redis
REDIS = {
    'Master': {
        'host': 'localhost',
        'port': 6379,
        'db': 15
    },
    'Slave': {
        'host': 'localhost',
        'port': 6379,
        'db': 15
    },
}


# Email 配置
ADMINS = [
    ('John', 'john@example.com'),
    ('Mary', 'mary@example.com')
]
EMAIL_SUBJECT_PREFIX = '[Swiper] '


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG'
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/info.log',
            'when': 'D',  # 每天切割日志
            'backupCount': 30,  # 日志保留 30 天
            'formatter': 'simple',
            'level': 'DEBUG'
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/error.log',
            'when': 'W0',  # 每周一切割日志
            'backupCount': 4,  # 日志保留 4 周
            'formatter': 'verbose',
            'level': 'DEBUG'
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            # 'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'DEBUG' if DEBUG else 'ERROR',
        }
    }
}
