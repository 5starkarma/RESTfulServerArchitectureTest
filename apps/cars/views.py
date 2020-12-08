from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from apps.cars.models import Car
from apps.cars.serializers import CarSerializer


class CarAPIView(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

