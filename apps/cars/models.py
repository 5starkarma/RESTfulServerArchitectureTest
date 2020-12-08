from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=64, null=True)
    model = models.CharField(max_length=64, null=True)
    year = models.PositiveSmallIntegerField(null=True)
    seats = models.PositiveSmallIntegerField(null=True)
    color = models.CharField(max_length=64, null=True)
    vin = models.CharField(max_length=128, null=True)
    current_mileage = models.PositiveIntegerField(null=True)
    service_interval = models.PositiveIntegerField(null=True)
    next_service = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.make} {self.model}, VIN: {self.vin}'
