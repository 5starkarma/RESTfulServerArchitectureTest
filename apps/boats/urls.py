from django.urls import path, include

from apps.boats.views import BoatAPIView

urlpatterns = [
    path('boats/', include([
        path('', BoatAPIView.as_view(), name='boats_list_api'),
        path('<int:id>/', BoatAPIView.as_view(), name='boat_detail_api'),
    ])),
]

