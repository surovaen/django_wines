from rest_framework import serializers


class BaseUserSerializer(serializers.Serializer):
    """Базовый сериализатор работы с пользователем."""

    username = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True,
        required=True,
    )
    access_token = serializers.CharField(
        max_length=255,
        read_only=True,
    )
    refresh_token = serializers.CharField(
        max_length=255,
        read_only=True,
    )

    class Meta:
        fields = (
            'username',
            'password',
            'access_token',
            'refresh_token',
        )
