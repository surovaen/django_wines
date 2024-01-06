from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from server.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя."""

    username = models.CharField(
        'Логин',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        'Активен',
        default=True,
    )
    is_staff = models.BooleanField(
        'Персонал',
        default=False,
    )
    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Обновлен',
        auto_now=True,
    )

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}'
