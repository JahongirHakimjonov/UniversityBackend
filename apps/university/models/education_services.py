from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.models import AbstractBaseModel


class EducationServices(AbstractBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
    )
    short_title = models.CharField(
        max_length=255,
        verbose_name=_('Short Title'),
    )
    description = CKEditor5Field(
        verbose_name=_('Description'),
    )
    short_description = models.TextField(
        verbose_name=_('Short Description'),
    )
    image = models.ImageField(
        upload_to='education_services/',
        verbose_name=_('Image'),
    )

    class Meta:
        verbose_name = _('Education Services')
        verbose_name_plural = _('Education Services')
        db_table = 'education_services'

    def __str__(self):
        return self.title
