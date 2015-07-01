from settings import *


DEBUG = True
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'python',
        'USER': 'adminx8ms3ih',
        'PASSWORD': 'WqLD1uKvFzAB',
        'HOST': '',
        'PORT': '',
    }
}



SECRET_KEY = 'your-super-secret-key'


MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')


from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())

