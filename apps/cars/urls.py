from django.urls import path, include

from apps.cars.views import CarAPIView

urlpatterns = [
    path('cars/', include([
        path('<int:id>', CarAPIView.as_view(), name='cars_api'),
    ])),
]
