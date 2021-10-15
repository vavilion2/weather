from django.db import models
from django.utils.timezone import now

class WeatherInfo(models.Model):
    city = models.CharField(max_length=50,blank=True,null=True)
    temperature= models.CharField(max_length=23,blank=True,null=True)
    humidity=models.CharField(max_length=50,blank=True,null=True)

    date = models.DateTimeField(default=now)

    pass