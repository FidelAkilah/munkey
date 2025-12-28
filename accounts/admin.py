from .models import User  # Import your custom User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # This ensures your custom 'role' field shows up in the admin panel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'is_restricted')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'is_restricted')}),
    )
    list_display = ['email', 'username', 'role', 'is_staff']