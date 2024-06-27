# Generated by Django 5.0.4 on 2024-05-01 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_groupnprojectassoc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupnprojectassoc',
            name='members',
        ),
        migrations.AddField(
            model_name='groupnprojectassoc',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]