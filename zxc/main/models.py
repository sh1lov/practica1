from django.db import models


class Task(models.Model):
    title = models.CharField('Задачи', max_length=100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'