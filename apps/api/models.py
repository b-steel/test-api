from django.db import models

# Create your models here.

class SolarData(models.Model):
    data = models.JSONField()

    class Meta:
        verbose_name_plural = 'SolarData'