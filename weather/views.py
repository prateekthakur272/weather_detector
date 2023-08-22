from django.shortcuts import render, redirect
import json
import urllib.request
from constants import api_key


# Create your views here.
def index(req):
    data = {}
    if req.method == 'POST':
        city = req.POST['city']
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
        res_data = json.loads(res)
        data = {
            'country_code': str(res_data['sys']['country']),
            'coordinate': f"{res_data['coord']['lon']} {res_data['coord']['lat']}",
            'temp': f"{res_data['main']['temp']}k",
            'pressure': str(res_data['main']['pressure']),
            'humidity': str(res_data['main']['humidity']),
        }
        return render(req, 'index.html', {'data': data, 'city': city})
    return render(req, 'index.html')
