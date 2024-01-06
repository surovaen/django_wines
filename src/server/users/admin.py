from django.contrib import admin
from django.contrib.auth.models import Group

from server.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('is_active', 'is_staff', 'is_superuser',)
    search_fields = ('username',)
    fieldsets = (
        (
            None, {
                'fields': ('username', 'password'),
            },
        ),
        (
            'Признаки',
            {
                'fields': (
                    ('is_active', 'is_staff', 'is_superuser',),
                ),
            },
        ),
        (
            'Даты',
            {
                'fields': ('last_login',),
            },
        ),
    )


admin.site.unregister(Group)
