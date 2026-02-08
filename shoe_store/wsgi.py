import os
import sys
import pymysql

# 1. PyMySQL ko MySQLdb ki jagah install karna
pymysql.install_as_MySQLdb()

# 2. Django ke version check ko bewakoof banana
# Hum manually bata rahe hain ki mysqlclient ka version 2.2.1+ hai
sys.modules["MySQLdb"] = pymysql
pymysql.version_info = (2, 2, 7, "final", 0)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')

application = get_wsgi_application()
app = application # Vercel ke liye alias