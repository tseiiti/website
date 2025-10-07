from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

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
  '_essential',
  'example'
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

ROOT_URLCONF = '_core.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ "_templates", "templates" ],
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

WSGI_APPLICATION = '_core.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("POSTGRES_DATABASE"),
    'USER': os.getenv("POSTGRES_USER"),
    'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
    'HOST': os.getenv("POSTGRES_HOST"),
    'PORT': os.getenv("POSTGRES_DB_PORT") if "POSTGRES_DB_PORT" in os.environ.keys() else 5432,
  }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
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
STATIC_ROOT =  os.path.join(BASE_DIR, "static_files", "static")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIDENAV = [
  { "type": "item", "name": "Home", "icon": "home", "link": "/" },
  { "type": "item", "name": "Admin", "icon": "cogs", "link": "/admin" },
  { "type": "item", "name": "Example", "icon": "tachometer-alt", "link": "/example/list" },
  { "type": "dropdown", "name": "Media", "icon": "photo-video", "links": [
    { "desc": "All", "link": "#" }, 
    { "desc": "Recent", "link": "#" }, 
    { "desc": "Images", "link": "#" }, 
    { "desc": "Video", "link": "#" }, 
  ]},
  { "type": "dropdown", "name": "Dashboards", "icon": "tachometer-alt", "links": [
    { "desc": "Frame", "link": "/example/dashboard" }, 
    { "desc": "New Tab", "link": "https://app.powerbi.com/view?r=eyJrIjoiZDNkNjRjMmMtZGE2Mi00YmZhLTkzMzAtYWJkYzQzNmM4NDgyIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9" }, 
  ]},
  { "type": "dropdown", "name": "Temas", "icon": "sun i-theme", "links": [
    { "desc": "Light<i class=\"fas fa-sun ms-2\"></i>", "link": "javascript: setTheme('light')" }, 
    { "desc": "Dark<i class=\"fas fa-moon ms-2\"></i>", "link": "javascript: setTheme('dark')" }, 
  ]}, 
]
