from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import json
from datetime import datetime, timezone, timedelta
from .models import SolarProject, Sensor, Data


def create_random_value(base, stdev):
    
    return random.random()*stdev + base


def get_next_interval(interval):
    
    BASE_TIME = datetime(year=2020, month=10, day=26, hour=9, minute= 30, second= 0, tzinfo=timezone.utc) 
    now = datetime.now(timezone.utc)
    tdelt = now - BASE_TIME
    
    n = tdelt // timedelta(seconds=interval)
    return BASE_TIME + n * timedelta(seconds=interval)



def api_call(request):

    if request.method == 'GET':
        name = request.GET['id']
        i = request.GET['interval']
    
        
        # Get timestamp
        ts = get_next_interval(int(i)).isoformat().replace('+00:00', 'Z')
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
                base = random.randint(0, 10000)
                stdev = random.randint(0, 100) * base / 100
                f = Sensor(name='sensor'+str(i), project=project, value_baseline=base, value_stdev=stdev)
                f.save()

        if project.last_queried == ts:
            for sensor in project.sensors.all():
                d = Data.objects.get(timestamp=ts)
                JSONdata[name][sensor.name] = d.value

        else:
            # Create Random Data
            for sensor in project.sensors.all():
                d = Data.objects.create(
                    timestamp=ts, 
                    sensor=sensor, 
                    value=create_random_value(sensor.value_baseline, sensor.value_stdev)
                    )
                sensor.data.add(d)

                JSONdata[name][sensor.name] = d.value

        # Set last query ts   
        project.last_queried = ts
        # Save
        project.save()

        return JsonResponse(JSONdata)
    else:
        return render(request, 'api/post.html', {})

def home(request):
    if request.method == 'GET':
        return render(request, 'api/home.html', {})
    