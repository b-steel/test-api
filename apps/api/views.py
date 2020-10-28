from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import json
from datetime import datetime, timezone, timedelta
from .models import SolarProject, Sensor, Data


def create_random_value():
    maximum = 100
    return random.random()*maximum


def get_next_interval(interval):
    BASE_TIME = datetime.fromisoformat('2020-10-28T09:30:00.000000')
    now = datetime.now()
    td = now - BASE_TIME
    
    n = td // timedelta(seconds=interval)
    return BASE_TIME + n * timedelta(seconds=interval)



def api_call(request):
    if request.method == 'GET':
        name = request.GET['id']
        
        # Get timestamp
        ts = get_next_interval(300).isoformat().replace('+00:00', 'Z')
        JSONdata = {
            name: {
                'timestamp': ts,
            }
        }
        
        project, created = SolarProject.objects.get_or_create(name=name)
        
        # Make Sensors
        if created:
            number_of_fields = random.randint(0, 10)
            for i in range(number_of_fields):
                f = Sensor(name='sensor'+str(i), project=project)
                f.save()

        # Create Random Data
        for sensor in project.sensors.all():
            d = Data.objects.create(timestamp=ts, sensor=sensor, value=create_random_value())
            sensor.data.add(d)

            JSONdata[name][sensor.name] = d.value
        
        # Save
        project.save()

        return JsonResponse(JSONdata)
    else:
        return render(request, 'api/post.html', {})
