from settings import *


DEBUG = True
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kandi',
        'USER': 'admindvckfkw',
        'PASSWORD': 't1_prCqX9e6W',
        'HOST': '',
        'PORT': '',
    }
}



SECRET_KEY = 'your-super-secret-key'


MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')


from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())

