import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50)
    is_active = models.BooleanField()

    class Meta:
        db_table = "projects"
