from django.urls import path, include
from .api_view import api_weather

app_name = 'api'

urlpatterns = [

    path('weather_api', api_weather, name='weather_api'),
]
