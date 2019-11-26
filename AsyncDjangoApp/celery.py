from __future__ import absolute_import
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncDjangoApp.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
CELERY_RESULT_BACKEND = 'rpc'

app = Celery('AsyncDjangoApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
