from django.db import models
#
# from datetime import datetime, timedelta


class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField(null=True)
    seats = models.PositiveSmallIntegerField(null=True)
    color = models.CharField(max_length=64)
    vin = models.CharField(max_length=128)
    current_mileage = models.PositiveIntegerField(null=True)
    service_interval = models.PositiveIntegerField(null=True)
    next_service = models.PositiveIntegerField(null=True)
