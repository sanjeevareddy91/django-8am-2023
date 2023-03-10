"""
Django settings for FilmIndustry project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from datetime import timedelta

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_7y851&tqzq&$j_kj*=r(n^x3tv34kvwh3e_@!$($lc(uv3u7$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filmapp',
    'crispy_forms',
    'rest_framework',
    'drf_yasg', # latest version for swagger..,
    'rest_framework.authtoken',
    # 'rest_framework_simplejwt'
    # 'oauth2_provider',
    # 'social_django',
    # 'drf_social_oauth2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'FilmIndustry.custom_middleware.SampleMiddleware'
]

ROOT_URLCONF = 'FilmIndustry.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'FilmIndustry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'filmapp',
#         'USER' : 'postgres',
#         'PASSWORD':'P@ssw0rd123'
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_URL = "/"
MEDIA_ROOT = BASE_DIR




EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your email id'
EMAIL_HOST_PASSWORD = 'yur app password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),
    # 'DEFAULT_PERMISSION_CLASSES':(
    #             'rest_framework.permissions.IsAuthenticated',
    # ),

}


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
#         'drf_social_oauth2.authentication.SocialAuthentication',
#     ),
# }
# JWT_AUTH = {
#     # how long the original token is valid for
#     'JWT_EXPIRATION_DELTA': timedelta(days=2),

#     # allow refreshing of tokens
#     'JWT_ALLOW_REFRESH': True,

#     # this is the maximum time AFTER the token was issued that
#     # it can be refreshed.  exprired tokens can't be refreshed.
#     'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
# }

# AUTHENTICATION_BACKENDS = (
#     # Others auth providers (e.g. Google, OpenId, etc)
#     # Facebook OAuth2
#     # 'social_core.backends.facebook.FacebookAppOAuth2',
#     # 'social_core.backends.facebook.FacebookOAuth2',

#     # # drf_social_oauth2
#     # 'drf_social_oauth2.backends.DjangoOAuth2',

#     # Django
#     'django.contrib.auth.backends.ModelBackend',
# )


# # Facebook configuration
# SOCIAL_AUTH_FACEBOOK_KEY = 'facebook-key'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'facebook-secret'

# # Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# # Email is not sent by default, to get it, you must request the email permission.
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email'
# }