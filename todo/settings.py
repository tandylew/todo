import os
from django.utils.crypto import get_random_string
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)
ALLOWED_HOSTS = ['*']
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [os.path.join(os.getcwd(), 'todo')],'APP_DIRS': True}]
ROOT_URLCONF = 'todo.urls'
INSTALLED_APPS = ['django.contrib.contenttypes','django.contrib.auth','django.contrib.sessions']
MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware']
#DATABASES = {'default':{'NAME':'mydb','ENGINE':'mysql.connector.django','USER':'root','PASSWORD':'Welcome1','HOST':'172.18.0.1'}}
