from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.models import AbstractBaseModel


class EducationSubjectsCategory(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Education Subject Category")
        verbose_name_plural = _("Education Subject Categories")
        db_table = "education_subjects_category"
        ordering = ["id"]


class EducationSubjects(AbstractBaseModel):
    full_name = models.CharField(_("Full Name"), max_length=255)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=255, blank=True, null=True)
    subject = models.CharField(_("Title"), max_length=255)
    problem = models.TextField(_("Problem"), blank=True, null=True)
    category = models.ForeignKey("EducationSubjectsCategory", verbose_name=_("Category"), on_delete=models.SET_NULL,
                                 blank=True, null=True)

    title = models.CharField(_("Title"), max_length=255)
    short_title = models.CharField(_("Short Title"), max_length=255)
    description = CKEditor5Field(_("Description"), blank=True, null=True)
    short_description = models.TextField(_("Short Description"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="education_subjects/", blank=True, null=True)
    video = models.FileField(_("Video"), upload_to="education_subjects/", blank=True, null=True)
    file = models.FileField(_("File"), upload_to="education_subjects/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Education Subject")
        verbose_name_plural = _("Education Subjects")
        db_table = "education_subjects"
        ordering = ["id"]
