from rest_framework import generics

from apps.trucks.models import Truck
from apps.trucks.serializers import TruckSerializer
from apps.utils.mixins import VehicleAPIViewMixin


class TruckAPIView(generics.GenericAPIView, VehicleAPIViewMixin):

    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
