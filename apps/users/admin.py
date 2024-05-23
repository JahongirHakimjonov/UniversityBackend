from django.contrib import admin

from apps.users.forms.users import CustomUserCreationForm
from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    list_display = ["id", "phone", "first_name", "last_name", "email"]
    search_fields = ["phone", "first_name", "last_name", "email"]
    fieldsets = (
        (None, {"fields": ("username", "phone", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "avatar")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2"),
            },
        ),
    )
