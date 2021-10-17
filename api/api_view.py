from rest_framework.decorators import api_view
import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .api_serializer import WeatherSerializer
from weather_forecast.my_def import base
from weather_forecast.models import WeatherInfo

@api_view(['POST','GET' ])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def api_weather(request):
    if request.method == 'GET':
        result = WeatherInfo.objects.all()
        serialize = WeatherSerializer(result, many=True)
        return Response(serialize.data)
    try:
        serializer = WeatherSerializer(data=request.POST)
        data = {}
        city = request.POST['city']
        x=base(city)


        if serializer.is_valid():
            wet = serializer.save()
            wet.city = x['city_full']
            wet.temperature = x['temp']
            wet.humidity = x['humidity']
            wet.save()
            data['city'] = x['city_full']
            data['temperature'] = x['temp']
            data['humidity'] = x['humidity']
    except Exception:
        return Response('wrong input')
    else:
        return Response(data)







