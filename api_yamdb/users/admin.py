from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'bio',
        'role',
    )
    search_fields = ('username', 'email')
    list_filter = ('role',)
    empty_value_display = '-empty-'
