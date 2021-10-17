from rest_framework.decorators import api_view
import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .api_serializer import WeatherSerializer


@api_view(['POST', ])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def api_weather(request):
    try:
        serializer = WeatherSerializer(data=request.POST)
        data = {}
        city = request.POST['city']
        url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=en&units=metric&appid=cc6fe4f29cdb3623b64b1efb2da93f53'
        ).read()
        unpack = json.loads(url)
        full_name = str(unpack['name'])
        temp = str(unpack['main']['temp'])
        city_short = str(unpack['sys']['country'])
        humidity = str(unpack['main']['humidity'])

        if serializer.is_valid():
            wet = serializer.save()
            wet.city = full_name
            wet.temperature = temp
            wet.humidity = humidity
            wet.save()
            data['city'] = full_name
            data['temperature'] = temp
            data['humidity'] = humidity
    except Exception:
        return Response('wrong input')
    else:
        return Response(data)
