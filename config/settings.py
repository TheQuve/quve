import os
import environ

from configurations import Configuration

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = 'qphl#testme&jjbraqxe63%k=)#+q^5*=5ixl$wh82#('

    ALLOWED_HOSTS = ['*']

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.postgres',
    ]

    THIRD_PARTY_APPS = [
        'channels',
        'sslserver',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        'rest_framework',
        'rest_framework.authtoken',
        'rest_auth',
        'rest_auth.registration',
        'corsheaders',
    ]

    LOCAL_APPS = [
        'quve.webrtc.apps.WebrtcConfig',
        'quve.api.apps.ApiConfig',
    ]

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    SITE_ID = 1

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

    WSGI_APPLICATION = 'config.wsgi.application'
    ASGI_APPLICATION = 'config.routing.application'
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': [('127.0.0.1', 6379)],
            },
        },
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Asia/Seoul'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # SITE_URL = 'http://0.0.0.0:8000'

    DEBUG = True
    APPEND_SLASH = True

    # AUTHENTICATION
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]
    # https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
    AUTH_USER_MODEL = 'api.User'

    # django-allauth
    # ------------------------------------------------------------------------------
    ACCOUNT_ALLOW_REGISTRATION = env.bool(
        'DJANGO_ACCOUNT_ALLOW_REGISTRATION',
        True
    )
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_AUTHENTICATION_METHOD = 'username'
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_EMAIL_REQUIRED = False
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_EMAIL_VERIFICATION = None
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_ADAPTER = 'quve.api.adapters.AccountAdapter'
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    SOCIALACCOUNT_ADAPTER = 'quve.api.adapters.SocialAccountAdapter'

    # Your common stuff: Below this line define 3rd party library settings

    # rest setting
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        ),
    }

    # REST_AUTH SETTING
    REST_USE_JWT = True
    ACCOUNT_LOGOUT_ON_GET = True

    # django cors header setting
    CORS_ORIGIN_ALLOW_ALL = True

    SOCIALACCOUNT_QUERY_EMAIL = True

    JWT_AUTH = {
        'JWT_VERIFY_EXPIRATION': False
    }

    SOCIALACCOUNT_PROVIDERS = {
        'facebook': {
            'SCOPE': [
                'email',
                'public_profile',
                'user_friends'
            ],
            'FIELDS': [
                'id',
                'email',
                'name',
                'first_name',
                'last_name',
                'verified',
                'locale',
                'timezone',
                'link',
                'gender',
                'updated_time',
                'picture'
            ],
            'AUTH_PARAMS': {
                # 'auth_type': 'reauthenticate'
            },
            'METHOD': 'oauth2',
            # 'LOCALE_FUNC': 'path.to.callable',
            'VERIFIED_EMAIL': True,
            'VERSION': 'v2.4'
        }
    }

    REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'quve.api.serializers.SignUpSerializer'
    }


class Dev(BaseConfiguration):
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    # SITE_URL = 'https://0.0.0.0'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # STATIC_URL = '/static/'
    # # SITE_URL = 'https://webrtc.com'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # STATICFILES_FINDERS = [
    #     'django.contrib.staticfiles.finders.FileSystemFinder',
    #     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # ]

    # print(STATIC_ROOT)
