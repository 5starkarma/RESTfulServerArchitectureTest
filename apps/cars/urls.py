from django.urls import path, include

from apps.cars.views import CarAPIView

urlpatterns = [
    path('cars/', include([
        path('', CarAPIView.as_view(), name='cars_list_api'),
        path('<int:pk>/', CarAPIView.as_view(), name='car_detail_api'),
    ])),
]
