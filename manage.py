#!/usr/bin/env python
from django.core.management.commands.runserver import Command as runserver
import os
import sys

if __name__ == "__main__":
    from django.conf import settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
#    settings.configure(DEBUG=True)
#    settings.ALLOWED_HOSTS = ['*']
#    settings.TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [os.path.join(os.getcwd(), 'todo')],'APP_DIRS': True}]
#    settings.ROOT_URLCONF = 'todo.urls'
#    settings.INSTALLED_APPS = ['django.contrib.contenttypes','django.contrib.auth','django.contrib.sessions']
#    settings.MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware']
#    settings.DATABASES = {'default':{'NAME':'mydb','ENGINE':'mysql.connector.django','USER':'root','PASSWORD':'Welcome1','HOST':'172.18.0.1'}}
    runserver.default_port = int(os.environ.get('PORT', 8000))
    print('Port var: %s' % os.environ.get('PORT'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
