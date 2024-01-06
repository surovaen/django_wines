from django.conf import settings
from django.utils import timezone
import jwt
from jwt import ExpiredSignatureError

from server.users.jwt.enums import JWTTokenTypeEnum
from server.users.jwt.exceptions import JWTException
from server.users.models import CustomUser


class JWTManager:
    """Класс-менеджер работы с jwt-токенами."""

    jwt_algorithm = 'PS256'
    access_token = JWTTokenTypeEnum.ACCESS_TOKEN.value
    refresh_token = JWTTokenTypeEnum.REFRESH_TOKEN.value
    access_token_expiration = settings.JWT_EXPIRATION_DELTA[access_token]
    refresh_token_expiration = settings.JWT_EXPIRATION_DELTA[refresh_token]

    @classmethod
    def get_token_data(cls, user: CustomUser) -> dict:
        """Получение access и refresh токенов."""
        data = {
            'access_token': cls._get_access_token(user),
            'refresh_token': cls._get_refresh_token(user),
        }
        return data

    @classmethod
    def verify_token(
            cls,
            token: str,
            token_type: str,
    ):
        """Валидация токена."""
        try:
            payload = jwt.decode(
                jwt=token,
                key=settings.JWT_PUBLIC_KEY,
                algorithms=[cls.jwt_algorithm],
            )
        except ExpiredSignatureError:
            raise JWTException(
                'Токен просрочен',
            )

        if payload['sub'] != token_type:
            raise JWTException(
                'Передан некорректный тип токена',
            )

        user = CustomUser.objects.get(pk=payload['id'])

        if not user:
            raise JWTException(
                'Пользователя не существует',
            )

        if not user.is_active:
            raise JWTException(
                'Пользователь неактивен',
            )

        return user

    @classmethod
    def _get_access_token(cls, user: CustomUser):
        """Получение access токена."""
        payload = {
            'id': user.pk,
            'sub': cls.access_token,
            'exp': timezone.now() + cls.access_token_expiration,
        }
        return cls._generate_jwt_token(payload=payload)

    @classmethod
    def _get_refresh_token(cls, user: CustomUser):
        """Получение refresh токена."""
        payload = {
            'id': user.pk,
            'sub': cls.refresh_token,
            'exp': timezone.now() + cls.refresh_token_expiration,
        }
        return cls._generate_jwt_token(payload=payload)

    @classmethod
    def _generate_jwt_token(cls, payload: dict) -> str:
        """Метод генерации JWT-токена."""
        jwt_token = jwt.encode(
            payload=payload,
            key=settings.JWT_PRIVATE_KEY,
            algorithm=cls.jwt_algorithm,
        )
        return jwt_token
