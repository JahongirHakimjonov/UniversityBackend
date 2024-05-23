from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class CustomUser(AbstractUser, AbstractBaseModel):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    # Add related_name arguments to these fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name="customuser",
        related_name="customuser_set",  # new
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name="customuser",
        related_name="customuser_set",  # new
        verbose_name=_('user permissions')
    )

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
