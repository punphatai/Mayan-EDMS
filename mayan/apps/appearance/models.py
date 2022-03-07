import bleach

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mayan.apps.events.classes import EventManagerSave
from mayan.apps.events.decorators import method_event

from .events import event_theme_created, event_theme_edited

#import RGBColorFie to create GUI select color
from colorful.fields import RGBColorField

class Theme(ExtraDataModelMixin, models.Model):
    #All font
    font_list = [('Arial','Arial'),('Verdana','Verdana'),('Helvetica','Helvetica'),('Tahoma','Tahoma'),
    ('Trebuchet MS','Trebuchet MS'),('Times New Roman','Times New Roman'),('Georgia','Georgia'),
    ('Garamond','Garamond'),('Courier New','Courier New'),('Brush Script MT','Brush Script Mt'),]

    label = models.CharField(
        db_index=True, help_text=_('A short text describing the theme.'),
        max_length=128, unique=True, verbose_name=_('Label')
    )
    # add logo with link
    logo = models.CharField(
        db_index=True, help_text=_('Change Logo Website.'),
        max_length=128, unique=True, verbose_name=_('Logo')
    )
    font = models.CharField(
        db_index=True, help_text=_('Change Font'),
        max_length=128, unique=True, verbose_name=_('Font'),
        choices = font_list
    )
    #add color code to model
    bg_Main_Menu = RGBColorField(
        help_text=_('RGB color value for main menu background.'),
        verbose_name=_('Background main menu')
    )
    bg_Main_Menu_at = RGBColorField(
        help_text=_('RGB color values for main menu when active or hover.'),
        verbose_name=_('Second color background main menu')
    )
    ct_bg_color = RGBColorField(
        help_text=_('RGB color values for background content box.'),
        verbose_name=_('Content box background')
    )
    sc_bt_button = RGBColorField(
        help_text=_('RGB color values for second button.'),
        verbose_name=_('Second button background')
    )
    tx_main = RGBColorField(
        help_text=_('RGB color values for main text.'),
        verbose_name=_('Main text color')
    )
    bg_bd = RGBColorField(
        help_text=_('RGB color values for background body.'),
        verbose_name=_('Background body')
    )
    sc_tx_color = RGBColorField(
        help_text=_('RGB color values for second text.'),
        verbose_name=_('Second text color')
    )
    hl_color = RGBColorField(
        help_text=_('The RGB color values for highlight or when hover menu top bar.'),
        verbose_name=_('Highlight color')
    )
    tx_menu = RGBColorField(
        help_text=_('RGB color values for text in list of menu.'),
        verbose_name=_('Menu text color')
    )
    dd_menu = RGBColorField(
        help_text=_('RGB color values for text in drop down menu.'),
        verbose_name=_('Drop down menu text')
    )
    stylesheet = models.TextField(
        blank=True, help_text=_(
            'The CSS stylesheet to change the appearance of the different '
            'user interface elements.'
        ), verbose_name=_('Stylesheet')
    )

    class Meta:
        ordering = ('label',)
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return force_text(s=self.label)

    def get_absolute_url(self):
        return reverse(
            viewname='appearance:theme_edit', kwargs={
                'theme_id': self.pk
            }
        )

    @method_event(
        event_manager_class=EventManagerSave,
        created={
            'event': event_theme_created,
            'target': 'self',
        },
        edited={
            'event': event_theme_edited,
            'target': 'self',
        }
    )
    def save(self, *args, **kwargs):
        bg_Main_Menu = self.bg_Main_Menu
        bg_Main_Menu_at = self.bg_Main_Menu_at
        ct_bg_color = self.ct_bg_color
        sc_bt_button = self.sc_bt_button
        tx_main = self.tx_main
        bg_bd = self.bg_bd
        sc_tx_color = self.sc_tx_color
        hl_color = self.hl_color
        tx_menu = self.tx_menu
        dd_menu = self.dd_menu
        logo = self.logo
        font = self.font
        css = f"""
        .navbar.navbar-default.navbar-fixed-top, .panel-primary .panel-heading{{
            background: {bg_Main_Menu};
        }}
        #menu-main {{
            background-color: {bg_Main_Menu};
        }}
        #accordion-sidebar .panel-heading {{
            background-color: {bg_Main_Menu};
        }}
        #accordion-sidebar  .panel  div  .panel-body{{
            background-color: {bg_Main_Menu};
            transition: .1s ease;
        }}
        .navbar.navbar-default.navbar-fixed-top .dropdown-menu li a:hover{{
            background: {bg_Main_Menu};
        }}
        .btn-block{{
            background-color: {bg_Main_Menu};
        }}
        .navbar.navbar-default.navbar-fixed-top .dropdown-menu li a:hover{{
            background: {bg_Main_Menu};
        }}
        .well .panel-heading, .well .svg, .well div > i svg{{
            color: {bg_Main_Menu};
        }}
        .panel-primary .panel-body{{
            color: {bg_Main_Menu};
        }}
        .btn-primary{{
            background: {bg_Main_Menu};
            border: 1px solid {bg_Main_Menu};
        }}
        .well .panel-primary .panel-heading{{
            background: {bg_Main_Menu};
        }}
        .nav.navbar-nav.navbar-right li.dropdown.open a[aria-expanded="true"] {{
            background: {bg_Main_Menu_at};
        }}
        #accordion-sidebar  .panel  div  .panel-body  ul  li:hover {{
            background-color: {bg_Main_Menu_at};
            transition: .1s ease;
        }}
        #accordion-sidebar a[aria-expanded="true"]{{
            background-color: {bg_Main_Menu_at};
        }}
        #accordion-sidebar  .panel  div  .panel-body  ul  li.active {{
            background: {bg_Main_Menu_at};
        }}
        #accordion-sidebar  .panel  div  .panel-body  ul  li:active {{
            background: {bg_Main_Menu_at};
        }}
        .btn-block:hover, .btn-block:focus{{
            background-color: {bg_Main_Menu_at};
        }}
        #accordion-sidebar .panel-heading:hover {{
            background-color: {bg_Main_Menu_at};
            transition: .1s ease;
        }}
        .input-group-btn a.btn-primary{{
            background: {bg_Main_Menu_at};
        }}
        #sidebar ul.list-group > li a:hover{{
            background: {bg_Main_Menu_at};
        }}
        .well, .well div.panel-footer{{
            background: {ct_bg_color};
        }}
        .btn-default:not(.btn-danger){{
            background: {sc_bt_button};
        }}
        h3#content-title,h4, p small, p.small, .well label:not(.btn), .well td:not(.last), .well li::marker,li,th,.form-group{{
            color: {tx_main};
        }}
        body, .well.center-block tr td,.pull-right.btn-group.open ul, .form-control, .navbar.navbar-default.navbar-fixed-top .dropdown-menu, .well div.panel-body,.panel-primary .panel-body, .well .panel-secondary > .panel-heading,#sidebar ul.list-group > li a{{
          background: {bg_bd};  
        }}
        .well p.help-block{{
            color: {sc_tx_color};
        }}
        .well a:not(.btn), .navbar.navbar-default.navbar-fixed-top #navbar > ul > li > a:hover{{
            color: {hl_color};
        }}
        .navbar.navbar-default.navbar-fixed-top #navbar > ul > li > a,.navbar.navbar-default.navbar-fixed-top #navbar > li > a,#accordion-sidebar  .panel  div  .panel-body  ul  li a, #accordion-sidebar  .panel-title, .btn,.well .panel-primary .panel-heading span{{
            color: {tx_menu};
        }}
        .well .panel-primary .panel-heading span{{
            color: {tx_menu} !important;
        }}
        #sidebar ul.list-group > li.dropdown-header, #sidebar ul.list-group > li a,.navbar.navbar-default.navbar-fixed-top .dropdown-menu li a{{
            color: {dd_menu};
        }}
        *{{
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif !important;
        }}
        img.web-logo{{
            background-image: url("{logo}");
            background-size: 150px;
            background-repeat: no-repeat;
        }}
        *{{
            font-family: '{font}', sans-serif !important;
        }}
        """
        self.stylesheet = css
        # self.stylesheet = bleach.clean(
        #     text=self.stylesheet, tags=('style',)
        # )
        super().save(*args, **kwargs)


class UserThemeSetting(models.Model):
    user = models.OneToOneField(
        on_delete=models.CASCADE, related_name='theme_settings',
        to=settings.AUTH_USER_MODEL, verbose_name=_('User')
    )
    theme = models.ForeignKey(
        blank=True, null=True, on_delete=models.CASCADE,
        related_name='user_setting', to=Theme, verbose_name=_('Theme')
    )

    class Meta:
        verbose_name = _('User theme setting')
        verbose_name_plural = _('User theme settings')

    def __str__(self):
        return force_text(s=self.user)

# Create CurrentTheme to make all page same theme
class CurrentTheme(models.Model):
    theme = models.ForeignKey(
        blank=True, null=True, on_delete=models.CASCADE,
        related_name='CurrentTheme', to=Theme, verbose_name=_('CurrentTheme')
    )

    class Meta:
        verbose_name = _('CurrentTheme')
        verbose_name_plural = _('CurrentTheme')

    def __str__(self):
        return force_text(s=self.theme)

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)