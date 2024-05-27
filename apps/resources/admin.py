from django.contrib import admin

from apps.resources.models import File, Gallery, Video


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("title", "file")
    search_fields = ("title", "file")
    list_filter = ("title", "file")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "video")
