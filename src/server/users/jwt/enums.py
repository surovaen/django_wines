import enum


class JWTTokenTypeEnum(enum.Enum):
    """Перечисление типов jwt токенов."""

    ACCESS_TOKEN = 'access_token'
    REFRESH_TOKEN = 'refresh_token'
