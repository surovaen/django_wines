from rest_framework.mixins import CreateModelMixin

from server.api.v1.auth.base.views import BaseUserView
from server.api.v1.auth.serializers import (
    UserLoginSerializer,
    UserRefreshTokenSerializer,
    UserRegistrationSerializer,
)


class UserRegistrationAPIView(CreateModelMixin, BaseUserView):
    """Вью регистрации пользователя."""

    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserLoginAPIView(BaseUserView):
    """Вью входа пользователя."""

    serializer_class = UserLoginSerializer


class UserRefreshTokenAPIView(BaseUserView):
    """Вью обмена refresh токена."""

    serializer_class = UserRefreshTokenSerializer
