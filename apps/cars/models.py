from django.db import models
# from django.utils.functional import cached_property
#
# from datetime import datetime, timedelta


class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    year = models.PositiveIntegerField(max_length=4, null=True)
    seats = models.PositiveSmallIntegerField(null=True)
    color = models.CharField(max_length=64)
    vin = models.CharField(max_length=128)
    current_mileage = models.PositiveIntegerField(null=True)
    service_interval = models.IntegerField()
    next_service = models.DateTimeField()

    # @cached_property
    # def contingency_end_date(self):
    #     return datetime.now() + timedelta(days=self.service_interval)
