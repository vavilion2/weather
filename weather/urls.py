from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/',include('weather_forecast.urls',namespace='weather')),
    path('api/',include('api.urls',namespace='api')),

]

