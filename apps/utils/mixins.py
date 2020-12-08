from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class VehicleAPIViewMixin(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
