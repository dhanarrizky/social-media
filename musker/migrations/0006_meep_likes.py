# Generated by Django 4.2 on 2023-05-08 07:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musker', '0005_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
