from django.urls import path

from server.api.v1.auth.views import (
    UserLoginAPIView,
    UserRefreshTokenAPIView,
    UserRegistrationAPIView,
)


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('refresh/', UserRefreshTokenAPIView.as_view()),
]
