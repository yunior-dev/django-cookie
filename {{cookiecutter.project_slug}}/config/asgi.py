"""
ASGI config for {{ cookiecutter.project_name }} project.
This module contains the ASGI application used by Django's development server
and any production ASGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``ASGI_APPLICATION`` setting.
Usually you will have the standard Django ASGI application here, but it also
might make sense to replace the whole Django ASGI application with a custom one
that later delegates to the Django one. For example, you could introduce ASGI
middleware here, or combine a Django application with an application of another
framework.
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# apps directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / 'apps'))

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_asgi process. To fix this, use
# mod_asgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "settings.production"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

# This application object is used by any ASGI server configured to use this
# file. This includes Django's development server, if the ASGI_APPLICATION
# setting points here.
application = get_asgi_application()

# Apply ASGI middleware here.
# from helloworld.asgi import HelloWorldApplication
# application = HelloWorldApplication(application)
