from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from server.users.jwt.enums import JWTTokenTypeEnum
from server.users.jwt.exceptions import JWTException
from server.users.jwt.manager import JWTManager


class JWTAuthentication(authentication.BaseAuthentication):
    """Класс аутентификации пользователей."""

    def authenticate(self, request):
        """Метод получения хэдеров с токеном и аутентификации."""
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header:
            return None

        if len(auth_header) > 1:
            return None

        token = auth_header[0].decode('utf-8')

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token: str):
        """Метод аутентификации пользователя."""
        try:
            user = JWTManager.verify_token(
                token=token,
                token_type=JWTTokenTypeEnum.ACCESS_TOKEN.value,
            )
        except JWTException as e:
            raise AuthenticationFailed(e)

        return user, token
