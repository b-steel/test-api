from django.db import models
import random

# Create your models here.

class SolarProject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Project: {self.name}'
        
    class Meta:
        ordering = ('name', )
    

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(SolarProject, related_name='sensors', on_delete=models.CASCADE)
    value_baseline = models.IntegerField(null=True, blank=True)
    value_stdev = models.IntegerField(null=True, blank=True)
    

class Data(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    
    