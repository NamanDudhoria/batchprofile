# Generated by Django 5.1.4 on 2025-02-06 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_placementactivity_user_alter_project_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='domain',
            new_name='domains',
        ),
    ]
