from django.db import models


class WeatherImage(models.Model):
    image = models.ImageField()
    id = models.IntegerField(primary_key=True)
