#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")
    from django.conf import settings
    settings.configure(DEBUG=True)
    settings.ALLOWED_HOSTS = ['*']
    settings.TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [os.path.join(os.getcwd(), 'todo')],'APP_DIRS': True}]
    settings.ROOT_URLCONF = 'todo.urls'
    #settings.DATABASES = {'default':{'ENGINE':'django.db.backends.mysql'}}
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
