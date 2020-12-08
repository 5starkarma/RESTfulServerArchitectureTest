from rest_framework import generics

from apps.cars.models import Car
from apps.cars.serializers import CarSerializer
from apps.utils.mixins import VehicleAPIViewMixin


class CarAPIView(generics.GenericAPIView, VehicleAPIViewMixin):

    serializer_class = CarSerializer
    queryset = Car.objects.all()

