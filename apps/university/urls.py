from django.urls import path

from apps.university.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
