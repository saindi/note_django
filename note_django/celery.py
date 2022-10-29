import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'note_django.settings')

app = Celery('note_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
