from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50)
