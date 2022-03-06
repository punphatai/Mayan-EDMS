from django import forms

from mayan.apps.views.forms import DetailForm

from .models import Theme, UserThemeSetting ,CurrentTheme #add CurrentTheme model


class ThemeForm(forms.ModelForm):
    class Meta:
        fields = ('label','bg_Main_Menu','bg_Main_Menu_at','ct_bg_color','sc_bt_button','tx_main',
        'hl_color','tx_menu','dd_menu','bg_bd','sc_tx_color',)
        model = Theme


class UserThemeSettingForm(forms.ModelForm):
    class Meta:
        fields = ('theme',)
        model = CurrentTheme ##to change all theme | original model is UserThemeSetting
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
