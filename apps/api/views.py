from django.shortcuts import render
from django.views import View
import random, json
from datetime import datetime, timezone

def create_random_field():
    maximum = 100
    return random.random()*maximum

class ApiView(View):
    def get(self, request):
        n = datetime.now(tz=timezone.utc)
        
        obj = {
            'timestamp': n.isoformat().replace('+00:00', 'Z')
        }
        for i in range(random.randint(0,10)):
            obj[str(i)] = create_random_field()

        return json.dumps(obj)
