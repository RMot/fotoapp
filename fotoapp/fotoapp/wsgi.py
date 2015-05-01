"""
WSGI config for plataforma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
#
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fotoapp.settings")
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

#!/usr/bin/python
import os
import sys

PROJECT_NAME = "fotoapp.fotoapp"


#sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', PROJECT_NAME))

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.environ['PROJECT_HOME'])
sys.path.append(os.path.join(os.environ['PROJECT_HOME'],'fotoapp/fotoapp'))
os.environ['DJANGO_SETTINGS_MODULE'] = os.path.join(os.environ['PROJECT_HOME'],'fotoapp/fotoapp','settings.py')
virtenv = os.environ['WORKON_HOME'] + '/development/'


os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

# add the virtualenv site-packages path to the sys.path
sys.path.append(os.path.join(virtenv, 'lib/python2.7/site-packages'))

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#from plataforma.plataforma.wsgi import baseapp