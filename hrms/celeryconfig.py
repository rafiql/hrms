from hrms.settings import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT


broker_url = result_backend = 'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/'.format(
    REDIS_PASSWORD=REDIS_PASSWORD, REDIS_HOST=REDIS_HOST, REDIS_PORT=REDIS_PORT)

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'

task_routes = {

    'base.tasks.generate_trip_report':
        {'queue': 'enterprise-command'},
    'base.tasks.generate_arm_disarm_alert':
        {'queue': 'enterprise-command'},
    'base.tasks.generate_update_journey':
        {'queue': 'enterprise-command'},
    'apps.sms.tasks.send_alarm_sms':
        {'queue': 'sms-queue'},
    'apps.notification_management.tasks.send_push_notification':
        {'queue': 'sms-queue'},
    'apps.notification_management.tasks.send_email_notification':
        {'queue': 'sms-queue'},
    'apps.sms.tasks.send_sms_notification':
        {'queue': 'sms-queue'},
    'apps.notification_management.tasks.send_alarm_alert_notification':
        {'queue': 'sms-queue'},
}
