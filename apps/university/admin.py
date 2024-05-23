from django.contrib import admin

from apps.university.models import (
    PtikStory, Gallery, Video, EducationSubjects, EducationSubjectsCategory, AcademicHours, EducationServices, News,
    Projects, ScientificBase
)


@admin.register(PtikStory)
class PtikStoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "video")


@admin.register(EducationSubjects)
class EducationSubjectsAdmin(admin.ModelAdmin):
    list_display = ("subject", "short_title", "category")
    search_fields = ("subject", "short_title", "category", "full_name")
    list_filter = ("category",)


@admin.register(EducationSubjectsCategory)
class EducationSubjectsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(AcademicHours)
class AcademicHoursAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")


@admin.register(EducationServices)
class EducationServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "short_title", "description", "short_description", "image")
    search_fields = ("title", "short_title", "description", "short_description", "image")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "short_title", "description", "short_description", "image")
    search_fields = ("title", "short_title", "description", "short_description", "image")


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "short_title", "description", "short_description", "image")
    search_fields = ("title", "short_title", "description", "short_description", "image")


@admin.register(ScientificBase)
class ScientificBaseAdmin(admin.ModelAdmin):
    list_display = ("title", "short_title", "description", "short_description", "image")
    search_fields = ("title", "short_title", "description", "short_description", "image")
