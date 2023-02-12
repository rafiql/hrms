import os
#import test again
from celery import Celery
from celery.schedules import crontab
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms.settings')
app = Celery("Celery App")
app.config_from_object('hrms.celeryconfig')
app.autodiscover_tasks(lambda: [app.name for app in apps.get_app_configs()])

app.conf.beat_schedule = {
    
    'deactivate_expired_resources': {
        'task': 'employee.tasks.deactive_expired_objects',
        'schedule': crontab(minute=57, hour='09'),
        'options': {'queue': 'attendance_periodic'}
    },

}
