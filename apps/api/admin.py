from django.contrib import admin
from .models import SolarProject, Sensor, Data

admin.site.register(SolarProject)
admin.site.register(Sensor)
admin.site.register(Data)


