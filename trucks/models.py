from django.db import models

class Truck(models.Model):
    plate_number = models.CharField(primary_key=True,max_length=32,default="RW SH ..")
    comments = models.CharField(max_length=200)
    maintenance_date = models.DateTimeField('Maintenance Date')
    trailer = models.ForeignKey(Trailer)

    def __str__(self):
        return self.plate_number

class Trailer(models.Model):
    plate_number = models.CharField(primary_key=True,max_length=32,default="RW SH ..")
    comments = models.CharField(max_length=200)
    maintenance_date = models.DateTimeField('Maintenance Date')

    def __str__(self):
        return self.plate_number


class WheelTruck(models.Model):
    truck = models.ForeignKey(Truck)
    position = models.CharField(max_length=64)
    distance = models.IntegerField(default=0)

class WheelTrailer(models.Model):
    trailer = models.ForeignKey(Trailer)
    position = models.CharField(max_length=64)
    distance = models.IntegerField(default=0)