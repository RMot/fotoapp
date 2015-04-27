#!/usr/bin/python
import os
import sys

PROJECT_NAME = "fotoapp.fotoapp"

os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'
#sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', PROJECT_NAME))

sys.path.append(os.environ['PROJECT_HOME'])
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
import django.core.handlers.wsgi
import django
django.setup()
application = django.core.handlers.wsgi.WSGIHandler()

#from plataforma.plataforma.wsgi import baseapp

