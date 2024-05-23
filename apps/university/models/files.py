from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class File(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    file = models.FileField(upload_to='files/', verbose_name=_('File'))

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return self.title
