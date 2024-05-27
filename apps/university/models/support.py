from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Support(AbstractBaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    subject = models.CharField(max_length=255, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))
