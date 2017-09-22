from __future__ import unicode_literals

from django.db import models

# Create your models here.
class cars(models.Model):
    car_name = models.CharField(max_length= 50)
    car_year = models.IntegerField()
    car_ratings = models.IntegerField()
    car_score = models.FloatField()

    def __str__(self):
        return self.car_name + " - " + str(self.car_year)



