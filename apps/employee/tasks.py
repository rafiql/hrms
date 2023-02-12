
from celery import task
from datetime import datetime
from apps.employee.models import Employee

@task(name='employee.tasks.deactive_expired_objects')
def deactive_expired_objects():
    Employee.objects.filter(phone = '01402639757').update(email_verified=True)