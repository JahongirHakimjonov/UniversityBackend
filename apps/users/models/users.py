from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from apps.shared.models import AbstractBaseModel
from apps.users.managers.users import UserManager


class User(auth_models.AbstractUser, AbstractBaseModel):
    phone = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = "phone"
    objects = UserManager()

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.email

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="custom_user_groups",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="custom_user_permissions",
        related_query_name="user",
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "base_users"
