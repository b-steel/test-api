from django.shortcuts import render
from django.http import JsonResponse
import random
import json
from datetime import datetime, timezone, timedelta
from .models import SolarData


def create_random_field():
    maximum = 100
    return random.random()*maximum


def get_next_interval(interval):
    BASE_TIME = datetime.fromisoformat('2020-10-28T09:30:00.000000')
    now = datetime.now()
    td = now - BASE_TIME
    
    n = td // timedelta(seconds=interval)
    return BASE_TIME + n * timedelta(seconds=interval)



def api(request):
    if request.method == 'GET':
        id = request.GET['id']

        data = {
            id: {
                'timestamp': get_next_interval(300).isoformat().replace('+00:00', 'Z')
            }
            }

        for i in range(random.randint(0, 10)):
            name = 'field'+str(i)
            data[id][name] = create_random_field()

        s = SolarData.objects.create(data=data)
        s.save()

        return JsonResponse(data)
    else:
        return render(request, 'api/post.html', {})
