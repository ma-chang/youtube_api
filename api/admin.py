from django.contrib import admin
from .models import Video, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "username"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("username",)}),
        (_("Permission"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Inportant_dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Video)
