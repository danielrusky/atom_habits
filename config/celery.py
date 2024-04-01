import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('habits')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_habits_daily': {
        'task': 'habits.tasks.check_habits_and_send_reminders',
        'schedule': timedelta(minutes=1),
    }
}
