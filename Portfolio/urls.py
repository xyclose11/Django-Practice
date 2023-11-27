from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("Portfolio/", include("Portfolio.urls")),
    path("admin/", admin.site.urls),
]