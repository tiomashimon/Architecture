import os
from celery import Celery
from celery import shared_task
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.main.settings')
settings.configure()
app = Celery('core.main')


app.config_from_object('core.main.settings.celery_settings')

app.autodiscover_tasks()

@shared_task
def test():
    print('WORKING_________________________---------------------------------------------------------')


app.conf.beat_schedule = {
    'test':
    {
        'task': 'core.main.celery.test',
        'schedule': crontab(minute='*/1')
    }
}