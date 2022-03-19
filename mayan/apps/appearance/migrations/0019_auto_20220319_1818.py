# Generated by Django 2.2.24 on 2022-03-19 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0018_theme_import_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='import_file',
            field=models.FileField(default=None, upload_to='', validators=[django.core.validators.FileExtensionValidator(['css'])], verbose_name='CSS File'),
        ),
    ]
