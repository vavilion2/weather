import json
import urllib.request


def base(city):
    #city = request.POST['city']
    url = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=en&units=metric&appid=cc6fe4f29cdb3623b64b1efb2da93f53'
    ).read()
    unpack = json.loads(url)
    full_name = str(unpack['name'])
    temp = str(unpack['main']['temp'])
    city_short = str(unpack['sys']['country'])
    humidity = str(unpack['main']['humidity'])
    forecast = {
        'city_full': full_name,
        'city_short': city_short,
        'temp': temp,
        'humidity': humidity,
    }
    return forecast
    #landing(city)
