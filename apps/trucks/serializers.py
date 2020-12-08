from rest_framework import serializers

from apps.trucks.models import Truck
from apps.utils.validators import VehicleYearValidator


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

    year = serializers.IntegerField(validators=[VehicleYearValidator()])
