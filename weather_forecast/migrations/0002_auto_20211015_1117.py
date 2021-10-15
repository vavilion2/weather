# Generated by Django 3.2.8 on 2021-10-15 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather_forecast', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherinfo',
            name='tempirature',
        ),
        migrations.RemoveField(
            model_name='weatherinfo',
            name='town',
        ),
        migrations.AddField(
            model_name='weatherinfo',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weatherinfo',
            name='humidity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weatherinfo',
            name='temperature',
            field=models.CharField(blank=True, max_length=23, null=True),
        ),
        migrations.AlterField(
            model_name='weatherinfo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]