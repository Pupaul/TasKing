# Generated by Django 5.0.4 on 2024-05-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_groupnprojectassoc_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='projects',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', to='api.project'),
        ),
    ]