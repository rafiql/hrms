
from hrms.celery import app
from datetime import datetime
from apps.employee.models import Employee

@app.task(name='employee.tasks.deactive_expired_objects')
def deactive_expired_objects():
    Employee.objects.all().update(email_verified=True)