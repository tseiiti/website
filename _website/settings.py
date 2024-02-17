from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"] if "SECRET_KEY" in os.environ.keys() else "django-insecure-django-insecure-django-insecure-django-insecure-dj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"] == "True" if "DEBUG" in os.environ.keys() else True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".vercel.app"]


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django_bootstrap5',
  'website'
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

ROOT_URLCONF = 'auxiliar.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ["templates"],
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

WSGI_APPLICATION = 'auxiliar.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
  # 'default': {
  #   'ENGINE': 'django.db.backends.sqlite3',
  #   'NAME': BASE_DIR / 'db.sqlite3',
  # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ]
STATIC_ROOT =  os.path.join(BASE_DIR, "static_files")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIDENAV = [
  { "type": "head", "name": "Configuração" },
  { "type": "item", "name": "Admin", "icon": "cog", "link": "/admin" },
  { "type": "menu", "name": "Temas", "icon": "palette", "links": [
    { "desc": "Dark", "link": "javascript:document.querySelector('#layoutSidenav_nav nav').classList.remove('sb-sidenav-light');document.querySelector('#layoutSidenav_nav nav').classList.add('sb-sidenav-dark');" }, 
    { "desc": "Light", "link": "javascript:document.querySelector('#layoutSidenav_nav nav').classList.remove('sb-sidenav-dark');document.querySelector('#layoutSidenav_nav nav').classList.add('sb-sidenav-light');" }, 
  ]},
  { "type": "divi" },
  { "type": "head", "name": "Minhas páginas" },
  { "type": "menu", "name": "Páginas", "icon": "folder", "links": [
    { "desc": "Modelo", "link": "/modelo/list" }, 
    { "desc": "Geeks", "link": "#" }, 
    { "desc": "Polls", "link": "#" }, 
  ]},
  { "type": "menu", "name": "Icones", "icon": "grin", "links": [
    { "desc": "Regular", "link": "#" }, 
    { "desc": "Solid", "link": "#" }, 
    { "desc": "Brands", "link": "#" }, 
  ]},
  { "type": "divi" },
]
