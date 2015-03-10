"""
WSGI config for dns_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
##For integrating with apache
sys.path.append('/home/girish.g/mygit/dns_api/api/')
sys.path.append('/home/girish.g/mygit/dns_api')
sys.path.append('/home/girish.g/mygit/dns_api/api/ui')
##
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dns_api.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
