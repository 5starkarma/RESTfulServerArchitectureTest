from django.urls import path, include

from apps.trucks.views import TruckAPIView

urlpatterns = [
    path('trucks/', include([
        path('', TruckAPIView.as_view(), name='trucks_list_api'),
        path('<int:id>/', TruckAPIView.as_view(), name='truck_detail_api'),
    ])),
]
