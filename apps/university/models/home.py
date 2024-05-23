from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Home(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    title = models.CharField(_("Title"), max_length=255)
    subtitle = models.CharField(_("Subtitle"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    location = models.CharField(_("Location"), max_length=255, blank=True, null=True)
    logo = models.ImageField(_("Logo"), upload_to="home/", blank=True, null=True)
    icon = models.ImageField(_("Icon"), upload_to="home/", blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="home/", blank=True, null=True)
    instagram = models.URLField(_("Instagram"), blank=True, null=True)
    facebook = models.URLField(_("Facebook"), blank=True, null=True)
    twitter = models.URLField(_("Twitter"), blank=True, null=True)
    linkedin = models.URLField(_("Linkedin"), blank=True, null=True)
    youtube = models.URLField(_("Youtube"), blank=True, null=True)
    telegram = models.URLField(_("Telegram"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Home")
        db_table = "home"
        ordering = ["id"]
