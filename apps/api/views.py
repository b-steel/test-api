from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import json
from datetime import datetime, timezone, timedelta
from .models import SolarProject


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

        project, created = SolarProject.objects.get_or_create(name=name)
        if created:
            project.number_of_fields = random.randint(0, 10)

        data = {
            name: {
                'timestamp': get_next_interval(300).isoformat().replace('+00:00', 'Z')
            }
        }

        for i in range(project.number_of_fields):
            fieldname = 'field'+str(i)
            data[name][fieldname] = create_random_value()

        project.data = data
        project.save()

        return JsonResponse(data)
    else:
        return render(request, 'api/post.html', {})
