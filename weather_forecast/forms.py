from django import forms
from .models import WeatherInfo


class WeatherForm(forms.ModelForm):
    WeatherInfo.objects.filter()

    class Meta:
        model = WeatherInfo

        fields = ('city','temperature','humidity')
        wigets={'city':forms.TextInput(attrs={})}
