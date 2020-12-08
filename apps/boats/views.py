from rest_framework import generics

from apps.boats.models import Boat
from apps.boats.serializers import BoatSerializer
from apps.utils.mixins import VehicleAPIViewMixin


class BoatAPIView(generics.GenericAPIView, VehicleAPIViewMixin):

    serializer_class = BoatSerializer
    queryset = Boat.objects.all()
