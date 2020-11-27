import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'tdu#qtq8bx^smn8at^6btbaw=sd8!wv25m@ldjy6c7a%7euwpq'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = []

DEBUG = True
