from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from server.api.v1.auth.base.serializers import BaseUserSerializer
from server.users.jwt.enums import JWTTokenTypeEnum
from server.users.jwt.exceptions import JWTException
from server.users.jwt.manager import JWTManager
from server.users.models import CustomUser


class UserRegistrationSerializer(BaseUserSerializer):
    """Сериализатор регистрации пользователя."""

    def create(self, data: dict) -> dict:
        """Метод создания пользователя."""
        user = CustomUser.objects.create_user(**data)
        user_data = {
            'username': user.username,
            **JWTManager.get_token_data(user),
        }
        return user_data


class UserLoginSerializer(BaseUserSerializer):
    """Сериализатор аутентификации пользователя."""

    def validate(self, data: dict) -> dict:
        """Метод валидации имени и пароля пользователя."""
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Пользователь не найден',
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Пользователь не активирован',
            )

        data.update(
            JWTManager.get_token_data(user),
        )

        return data


class UserRefreshTokenSerializer(serializers.Serializer):
    """Сериализатор обмена refresh токена."""

    access_token = serializers.CharField(
        read_only=True,
    )
    refresh_token = serializers.CharField(
        required=True,
    )

    class Meta:
        fields = ('refresh_token',)

    def validate(self, data: dict) -> dict:
        """Метод валидации refresh токена."""
        refresh_token = data.get('refresh_token')

        try:
            user = JWTManager.verify_token(
                token=refresh_token,
                token_type=JWTTokenTypeEnum.REFRESH_TOKEN.value,
            )
        except JWTException as e:
            raise AuthenticationFailed(e)

        return JWTManager.get_token_data(user)
