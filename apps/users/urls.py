from django.urls import path, include

from apps.users.views import CreateUserView

urlpatterns = [
    path('users/', include([
        path('create/', CreateUserView.as_view(), name='create_user'),
    ])),
]
