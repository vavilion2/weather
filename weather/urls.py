from weather_forecast.errors import er
from django.contrib import admin
from django.urls import path,include

handler404=er
urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/',include('weather_forecast.urls',namespace='weather')),
    path('xd/',er)
]

