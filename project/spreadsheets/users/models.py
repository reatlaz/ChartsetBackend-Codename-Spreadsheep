from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=254, verbose_name='Почта')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
