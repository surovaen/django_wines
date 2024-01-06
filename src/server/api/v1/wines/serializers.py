from rest_framework import serializers


class WineMarkerSerializer(serializers.Serializer):
    """Сериализатор виномаркетов."""

    name = serializers.CharField(
        read_only=True,
    )
    city = serializers.CharField(
        read_only=True,
    )


class WineSerializer(serializers.Serializer):
    """Сериализатор вин."""

    name = serializers.CharField(
        read_only=True,
    )
    country = serializers.CharField(
        read_only=True,
    )
    price = serializers.IntegerField(
        read_only=True,
    )
    bottling_date = serializers.DateField(
        read_only=True,
    )
    description = serializers.CharField(
        read_only=True,
    )
    markets = WineMarkerSerializer(
        many=True,
        read_only=True,
    )
