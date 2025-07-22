from django.urls import path
from categories.views import index


app_name = "categories"

urlpatterns = [path("", index)]
