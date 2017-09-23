"""
WSGI config for attendance_2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
fromdjango.core.wsgiimportget_wsgi_applicationfromdj_staticimportCling application = Cling(get_wsgi_application())

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_2.settings")

application = get_wsgi_application()
