# weather
To start app:
docker-compose up

Preparation for usage:

Firsly: create superuser
docker-compose run web python manage.py createsuperuser

Check setting.py and adjust DEBUG= True/ False for your purposes

Use these hosts: ALLOWED_HOSTS = ['localhost','0.0.0.0','127.0.0.1']


Usage:

Enter the main page:
http://0.0.0.0:9000/weather/landing
input in form name of the city: app will show some weather info <<All requests are saved in database>>

Enter the admin as superuser:
http://0.0.0.0:9000/admin/
in 'Weather infos' there will be instances of your requests


Using rest api:

To test api use Postman (url-http://0.0.0.0:9000/weather/landing)
Go to the body, use form-data and input:
KEY: city  VALUE: <name of the city>

To check if it is working: go to admin and find your saved request instance

