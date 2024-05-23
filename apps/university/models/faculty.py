from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.models import AbstractBaseModel


class Faculty(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    description = CKEditor5Field(_("Description"), blank=True, null=True)
    logo = models.ImageField(_("Logo"), upload_to="faculty/", blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    dekan = models.CharField(_("Dekan"), max_length=255, blank=True, null=True)
    dekan_photo = models.ImageField(_("Dekan Photo"), upload_to="faculty/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")
        db_table = "faculty"
        ordering = ["id"]
