from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Video(AbstractBaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    video = models.FileField(_("Video"), upload_to="video/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        db_table = "video"
        ordering = ["id"]
