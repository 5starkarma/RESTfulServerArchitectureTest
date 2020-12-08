from django.db import models


class Boat(models.Model):
    make = models.CharField(max_length=64, null=True)
    model = models.CharField(max_length=64, null=True)
    year = models.PositiveSmallIntegerField(null=True)
    length = models.PositiveSmallIntegerField(null=True)
    width = models.PositiveSmallIntegerField(null=True)
    hin = models.CharField(max_length=128, null=True)
    current_hours = models.PositiveIntegerField(null=True)
    service_interval = models.PositiveIntegerField(null=True)
    next_service = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.make} {self.model}, VIN: {self.hin}'
