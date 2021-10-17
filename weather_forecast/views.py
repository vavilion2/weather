import json
import urllib.request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import WeatherForm


from .my_def import base
# from .my_def import base

@csrf_protect
def landing(request):
    if request.method == 'POST':
        # form = WeatherForm
        form = WeatherForm(request.POST, request.FILES)
        try:
            city = request.POST['city']

            x=base(city)

            if form.is_valid():
                data = form.save(commit=False)
                data.city = x['city_full']
                data.humidity = x['temp']
                data.temperature = x['humidity']
                data.save()
        # print(forecast)
        except Exception:
            return render(request, 'weather/landing2.html')
    else:
        x = {}
    return render(request, 'weather/landing.html', x)
