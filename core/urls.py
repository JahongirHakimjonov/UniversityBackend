from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("apps.university.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "apps.university.views.exceptions.handler404"
handler400 = "apps.university.views.exceptions.handler400"
handler403 = "apps.university.views.exceptions.handler403"
handler500 = "apps.university.views.exceptions.handler500"
