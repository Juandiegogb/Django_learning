from django.contrib import admin
from django.urls import path, include
from Django_learning.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("categories/", include("categories.urls")),
]
