import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DIRNAME = os.path.dirname(os.path.abspath(__file__))
_ = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# @see https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

SECRET_KEY = 'ywf8ld_@!hk+yfp@*o-yzu^lzc*394a621(lk_*1r=+^-+ynb0'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '*']

CMS_TEMPLATES = (
    ('core.html', 'Core'),
    #('page.tmpl', 'Page'),
    #('page-detail.tmpl', 'Page Detail'),

)

INSTALLED_APPS = (
    'djangocms_admin_style',

    'dal',
    'dal_select2',
    'html_field',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'mptt',
    'sekizai',
    'treebeard',
    'django.contrib.messages',

    'django_extensions',
    'sorl.thumbnail',
    'tagging',

    'easy_thumbnails',
    'djangocms_text_ckeditor',


    'imagestore',
    'imagestore.imagestore_cms',
    'mini_charge',
    'website',

)


IMAGESTORE_SHOW_USER = False
IMAGESTORE_IMAGE_MODEL = 'mini_charge.MiniChargeImage'
IMAGESTORE_ALBUM_MODEL = 'mini_charge.MiniChargeAlbum'
IMAGESTORE_IMAGE_FORM = 'mini_charge.forms.ImageForm'
IMAGESTORE_ALBUM_FORM = 'mini_charge.forms.AlbumForm'

# IMAGESTORE_TEMPLATE = 'base.html'
# IMAGESTORE_LOAD_CSS = True
#MIDDLEWARE_CLASSES = [
    ##'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
#]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


ROOT_URLCONF = 'spreconomists_org.urls'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'assets')
MEDIA_URL = '/assets/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


WSGI_APPLICATION = 'spreconomists_org.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#AUTH_PASSWORD_VALIDATORS = [
    #{
        #'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
#]
LANGUAGES = [
    ('en', 'English'),
]
LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


