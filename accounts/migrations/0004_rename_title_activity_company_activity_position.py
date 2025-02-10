# Generated by Django 5.1.4 on 2025-02-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20250210_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='title',
            new_name='company',
        ),
        migrations.AddField(
            model_name='activity',
            name='position',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]
