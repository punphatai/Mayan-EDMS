from django import forms

from mayan.apps.views.forms import DetailForm

from .models import Theme, UserThemeSetting ,CurrentTheme #add CurrentTheme model


class ThemeForm(forms.ModelForm):
    class Meta:
        fields = ('label','logo','font','bg_Main_Menu','bg_Main_Menu_at','ct_bg_color','sc_bt_button',
        'hl_color','tx_main','tx_menu','sc_tx_color','dd_menu','bg_bd','sc_tx_color',)
        model = Theme
        widgets = {
            'font': forms.Select(
                attrs={
                    'class': 'select2'
                }
            ),
        }


class UserThemeSettingForm(forms.ModelForm):
    class Meta:
        fields = ('theme',)
        model = CurrentTheme
        widgets = {
            'theme': forms.Select(
                attrs={
                    'class': 'select2'
                }
            ),
        }


class UserThemeSettingForm_view(DetailForm):
    class Meta:
        fields = ('theme',)
        model = UserThemeSetting



