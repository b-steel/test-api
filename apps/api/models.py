from django.db import models

# Create your models here.

class SolarProject(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name', )

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(SolarProject, related_name='sensors', on_delete=models.CASCADE)
    

class Data(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    
    