from django.contrib.auth.forms import UserCreationForm
from apps.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("id", "email")
