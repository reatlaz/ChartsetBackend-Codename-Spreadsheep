import time
from celery import shared_task

from application import celery_app #спросить про имя celery_app

from django.core.mail import send_mail
from application.celery import app

#@celery_app.task()
#@shared_task
@app.task
def email_admin(info):
    send_mail(
        'Subject here',
        'object created:' + str(info),
        'from@example.com',
        ['playatlas@yandex.ru'],
        fail_silently=False,
        )

#@shared_task
#def some_sleep(seconds):
#    time.sleep(seconds)


#@shared_task
#def increment(num):
#    return num + 1
