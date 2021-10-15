import urllib.request
from urllib import request
from django.shortcuts import render
from django.views import generic
import requests, json
from .forms import WeatherForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def landing(request):
    if request.method == 'POST':
        form=WeatherForm
        city = request.POST['city']
        url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=en&units=metric&appid=cc6fe4f29cdb3623b64b1efb2da93f53'
        ).read()
        unpack = json.loads(url)
        full_name=str(unpack['name'])
        temp=str(unpack['main']['temp'])
        city_short=str(unpack['sys']['country'])
        humidity=str(unpack['main']['humidity'])
        forecast = {
            'city_full':full_name,
            'city_short': city_short,
            'temp': temp,
            'humidity':humidity ,
        }
        if form.is_valid():
            xd = form.save(commit=False)
            xd.city = full_name
            xd.save()
        print(forecast)
    else:
        forecast = {}
    return render(request, 'weather/landing.html', forecast)

