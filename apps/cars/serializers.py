from rest_framework import serializers

from apps.cars.models import Car
from apps.utils.validators import VehicleYearValidator


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    year = serializers.IntegerField(validators=[VehicleYearValidator()])
