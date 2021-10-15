# Generated by Django 3.2.8 on 2021-10-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=50)),
                ('tempirature', models.SmallIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]