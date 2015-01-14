from django.db import models

# Create your models here.
class Truck(models.Model):
    comments = models.CharField(max_length=200)
    maintenance_date = models.DateTimeField('TÜV Datum')

class Wheels(models.Model):
    truck = models.ForeignKey(Truck)
    position = models.CharField(max_length=32)
    distance = models.IntegerField(default=0)