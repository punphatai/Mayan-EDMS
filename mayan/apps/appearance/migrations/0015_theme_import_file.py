# Generated by Django 2.2.24 on 2022-03-19 11:08

import django.core.validators
from django.db import migrations, models
import mayan.apps.appearance.models
import mayan.apps.storage.classes


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0014_remove_theme_logo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='import_file',
            field=models.FileField(default=None, storage=mayan.apps.storage.classes.DefinedStorageLazy(name='converter__assets'), upload_to=mayan.apps.appearance.models.upload_to, validators=[django.core.validators.FileExtensionValidator(['css'])], verbose_name='File'),
        ),
    ]
