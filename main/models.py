from django.db import models

from utils.models import AbstractModel


class SomeString(AbstractModel):
    string = models.CharField(max_length=255)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Строка'
        verbose_name_plural = 'Строки'

    def __str__(self):
        return f'{self.string}'
