# Generated by Django 3.2.8 on 2021-10-15 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather_forecast', '0004_delete_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherinfo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]