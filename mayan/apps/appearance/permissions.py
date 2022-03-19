from django.utils.translation import ugettext_lazy as _

from mayan.apps.permissions import PermissionNamespace

namespace = PermissionNamespace(label=_('Appearance'), name='appearance')

permission_theme_create = namespace.add_permission(
    label=_('Create new themes'), name='theme_create'
)
#import new theme
permission_theme_import = namespace.add_permission(
    label=_('Import new themes'), name='theme_import'
)

permission_theme_delete = namespace.add_permission(
    label=_('Delete themes'), name='theme_delete'
)
permission_theme_edit = namespace.add_permission(
    label=_('Edit themes'), name='theme_edit'
)
permission_theme_view = namespace.add_permission(
    label=_('View existing themes'), name='theme_view'
)
