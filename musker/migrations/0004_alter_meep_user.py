# Generated by Django 4.2 on 2023-05-05 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musker', '0003_meep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meep',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeps', to=settings.AUTH_USER_MODEL),
        ),
    ]