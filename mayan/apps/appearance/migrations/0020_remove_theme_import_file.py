# Generated by Django 2.2.24 on 2022-03-19 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0019_auto_20220319_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='import_file',
        ),
    ]
