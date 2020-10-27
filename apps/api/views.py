from django.shortcuts import render
from django.http import JsonResponse
import random
import json
from datetime import datetime, timezone
from .models import SolarData


def create_random_field():
    maximum = 100
    return random.random()*maximum


def api(request):
    if request.method == 'GET':
        n = datetime.now(tz=timezone.utc)
        id = request.GET['id']

        data = {
            id: {
                'timestamp': n.isoformat().replace('+00:00', 'Z')
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
