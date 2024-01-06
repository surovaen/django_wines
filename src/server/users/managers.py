from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Класс менеджера работы с пользователями."""

    def create_user(
            self,
            username: str,
            password: str = None,
    ):
        """Метод создания пользователя."""
        if username is None:
            raise TypeError('Не указан логин пользователя.')

        if password is None:
            raise TypeError('Не указан пароль.')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
            self,
            username: str,
            password: str,
    ):
        """Метод создания суперпользователя."""
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
