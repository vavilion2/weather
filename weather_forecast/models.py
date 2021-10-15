from django.db import models


class WeatherInfo(models.Model):
    city = models.CharField(max_length=50,blank=True,null=True)
    tempirature= models.SmallIntegerField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    pass
