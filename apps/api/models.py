from django.db import models

# Create your models here.

class SolarProject(models.Model):
    name = models.CharField(max_length=20)
    data = models.JSONField(null=True, blank=True)
    number_of_fields = models.IntegerField(default=1)


    class Meta:
        ordering = ('name', )