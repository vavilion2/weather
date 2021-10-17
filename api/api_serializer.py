from rest_framework import serializers
from weather_forecast.models import WeatherInfo


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherInfo
        fields = ['city', 'temperature', 'humidity','date']

