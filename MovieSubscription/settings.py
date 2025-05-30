import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--eg4#b%k8o45e_#4-lfel%vdxa8ytd%+qj14y*sxb&lwm$)^k9'
DEBUG = False
ALLOWED_HOSTS = ['37.60.235.197']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movie.apps.MovieConfig',
    'user_profile.apps.UserProfileConfig',
    'review.apps.ReviewConfig',
    'subscription.apps.SubscriptionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MovieSubscription.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Agar kerak bo‘lsa templates papkasi
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

WSGI_APPLICATION = 'MovieSubscription.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'movies:movie_list'
LOGOUT_REDIRECT_URL = 'account:login'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ STATIC SETTINGS
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Must be str (not Path)

# ✅ MEDIA SETTINGS
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # optional but recommended separate from static

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ PAYPAL SETTINGS
PAYPAL_MODE = os.getenv('PAYPAL_MODE', default='sandbox')
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', default='YOUR_SANDBOX_CLIENT_ID')
PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', default='YOUR_SANDBOX_CLIENT_SECRET')
