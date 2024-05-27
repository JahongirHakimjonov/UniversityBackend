from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.models import AbstractBaseModel


class PtikStory(AbstractBaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = CKEditor5Field(
        _("Description"), blank=True, null=True, config_name="extends"
    )
    image = models.ImageField(
        _("Image"), upload_to="ptik_story/", blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("PTIK Story")
        verbose_name_plural = _("PTIK Stories")
        db_table = "ptik_story"
        ordering = ["id"]
