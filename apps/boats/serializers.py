from rest_framework import serializers

from apps.boats.models import Boat
from apps.utils.validators import VehicleYearValidator


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = '__all__'

    year = serializers.IntegerField(validators=[VehicleYearValidator()])


