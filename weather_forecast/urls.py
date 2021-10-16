from django.urls import path, include
from .views import landing

# from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'weather_forecast'

urlpatterns = [

    path('landing', landing, name='landing')

]
