import os
import sys
import pymysql

# Django ko bewakoof banane ke liye
pymysql.version_info = (2, 2, 7, "final", 0)
pymysql.install_as_MySQLdb()
sys.modules["MySQLdb"] = pymysql

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')

application = get_wsgi_application()
app = application