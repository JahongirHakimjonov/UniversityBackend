from django.contrib import admin

from apps.users.admin.users import CustomUserAdmin
from apps.users.models import User

admin.site.register(User, CustomUserAdmin)
