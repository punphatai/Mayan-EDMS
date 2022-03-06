# Generated by Django 2.2.24 on 2022-03-06 12:18

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0006_remove_theme_maincolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='dd_menu',
            field=colorful.fields.RGBColorField(default='ffffff', help_text='The RGB color values for drop down text menu.', verbose_name='Drop down menu text color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='hl_color',
            field=colorful.fields.RGBColorField(default='ffffff', help_text='The RGB color values for highlight.', verbose_name='Highlight color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='tx_menu',
            field=colorful.fields.RGBColorField(default='ffffff', help_text='The RGB color values for menu text color.', verbose_name='Menu text color'),
            preserve_default=False,
        ),
    ]
