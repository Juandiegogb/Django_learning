# Generated by Django 5.2.4 on 2025-07-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_remove_category_custom_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
