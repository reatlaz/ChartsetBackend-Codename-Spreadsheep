from django.db import models
from users.models import User
from django.utils import timezone

class Chartset(models.Model):
    #Первичный ключ не создаем
    name = models.CharField(max_length=32, verbose_name='Название проекта')
    userschartsets = models.ManyToManyField(User,  verbose_name='Имеют доступ')
    date_modified = models.DateTimeField('Последнее изменение', default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

    class Meta:
        ordering = ('-date_modified',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

