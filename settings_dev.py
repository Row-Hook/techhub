from .settings_common import *

#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='django-insecure-jhc+)t-i_=h0km55!b&0schh8=rx16z4z*+a_mhi3kl9*b#+3z'

#SECURITY WARNING: don't run with debug turned on in production
DEBUG=True

ALLOWED_HOSTS=[]

#ロギング設定
LOGGING={
    'version': 1,
    'disable_existing_loggers': False,

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'pages':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND= 'django.core.mail.backends.console.EmailBackend'