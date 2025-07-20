from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    BooleanField,
    IntegerField,
)


class Category(Model):
    name = CharField(max_length=50)
    description = TextField()
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    stock = IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.is_active and self.stock > 0
