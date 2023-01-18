from django.contrib import admin
from django.contrib.auth.models import User


admin.site.unregister(User)


class AuthorAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
        'user_permissions')


admin.site.register(User, AuthorAdmin)
