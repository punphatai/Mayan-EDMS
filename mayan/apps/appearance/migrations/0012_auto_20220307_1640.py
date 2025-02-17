# Generated by Django 2.2.24 on 2022-03-07 16:40

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0011_theme_font'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='bg_Main_Menu',
            field=colorful.fields.RGBColorField(help_text='RGB color value for main menu background.', verbose_name='Background main menu'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='bg_Main_Menu_at',
            field=colorful.fields.RGBColorField(help_text='RGB color values for main menu when active or hover.', verbose_name='Second color background main menu'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='bg_bd',
            field=colorful.fields.RGBColorField(help_text='RGB color values for background body.', verbose_name='Background body'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='ct_bg_color',
            field=colorful.fields.RGBColorField(help_text='RGB color values for background content box.', verbose_name='Content box background'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='dd_menu',
            field=colorful.fields.RGBColorField(help_text='RGB color values for text in drop down menu.', verbose_name='Drop down menu text'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='font',
            field=models.CharField(choices=[('Arial', 'Arial'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Tahoma', 'Tahoma'), ('Trebuchet MS', 'Trebuchet MS'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Garamond', 'Garamond'), ('Courier New', 'Courier New'), ('Brush Script MT', 'Brush Script Mt')], db_index=True, help_text='Change Font', max_length=128, unique=True, verbose_name='Font'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='hl_color',
            field=colorful.fields.RGBColorField(help_text='The RGB color values for highlight or when hover menu top bar.', verbose_name='Highlight color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo',
            field=models.CharField(db_index=True, help_text='Change Logo Website.', max_length=300, unique=True, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='sc_bt_button',
            field=colorful.fields.RGBColorField(help_text='RGB color values for second button.', verbose_name='Second button background'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='sc_tx_color',
            field=colorful.fields.RGBColorField(help_text='RGB color values for second text.', verbose_name='Second text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='tx_main',
            field=colorful.fields.RGBColorField(help_text='RGB color values for main text.', verbose_name='Main text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='tx_menu',
            field=colorful.fields.RGBColorField(help_text='RGB color values for text in list of menu.', verbose_name='Menu text color'),
        ),
    ]
