from django.contrib import admin
<<<<<<< Updated upstream
from django.urls import path, include
from Django_learning.views import index

=======
from django.urls import include, path
>>>>>>> Stashed changes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("categories/", include("categories.urls")),
]
