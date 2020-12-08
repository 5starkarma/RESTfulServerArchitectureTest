from rest_framework import serializers

from apps.boats.models import Boat


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = '__all__'
