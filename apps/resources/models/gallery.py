from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Gallery(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="gallery/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")
        db_table = "gallery"
        ordering = ["id"]
