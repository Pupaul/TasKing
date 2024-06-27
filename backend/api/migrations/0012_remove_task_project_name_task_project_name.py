# Generated by Django 5.0.4 on 2024-05-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_project_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_name',
        ),
        migrations.AddField(
            model_name='task',
            name='project_name',
            field=models.ManyToManyField(default=None, to='api.project'),
        ),
    ]
