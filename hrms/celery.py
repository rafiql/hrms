import os
#pushing to dev
from celery import Celery
from celery.schedules import crontab
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms.settings')
app = Celery("Celery App")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: [app.name for app in apps.get_app_configs()])

app.conf.beat_schedule = {
    
    'deactivate_expired_resources': {
        'task': 'employee.tasks.deactive_expired_objects',
        'schedule': 10
    },

}
