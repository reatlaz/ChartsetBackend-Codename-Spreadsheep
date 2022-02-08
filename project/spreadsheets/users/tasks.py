from time import ctime
from celery import shared_task

from application import celery_app #спросить про имя celery_app
from .models import User
from django.core.mail import send_mail
from application.celery import app

#@shared_task
@app.task
def amount_of_users_rn():
    amount_of_users = len(User.objects.filter())
    f = open("users/unique_users_logs.txt", "a")
    f.write('\n')
    f.write(f'{amount_of_users} users at {ctime()}')
    f.close()

    return amount_of_users
