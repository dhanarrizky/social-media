# Generated by Django 4.2 on 2023-05-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0004_alter_meep_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]