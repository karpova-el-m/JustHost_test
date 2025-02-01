from django.db import models

from core.constants import STATUS_CHOICES


class VPS(models.Model):
    uid = models.AutoField(primary_key=True)
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='stopped'
    )

    class Meta:
        verbose_name = 'Виртуальный сервер (VPS)'
        verbose_name_plural = 'Виртуальные сервера (VPS)'

    def __str__(self):
        return f'VPS {self.uid}'
