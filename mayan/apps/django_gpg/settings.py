from __future__ import unicode_literals

import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from mayan.apps.smart_settings.classes import Namespace

namespace = Namespace(label=_('Signatures'), name='django_gpg')

setting_gpg_home = namespace.add_setting(
    global_name='SIGNATURES_GPG_HOME',
    default=os.path.join(settings.MEDIA_ROOT, 'gpg_home'),
    help_text=_(
        'Home directory used to store keys as well as configuration files.'
    ),
    is_path=True
)
setting_gpg_path = namespace.add_setting(
    global_name='SIGNATURES_GPG_PATH', default='/usr/bin/gpg1',
    help_text=_('Path to the GPG binary.'), is_path=True
)
setting_keyserver = namespace.add_setting(
    global_name='SIGNATURES_KEYSERVER', default='pool.sks-keyservers.net',
    help_text=_('Keyserver used to query for keys.')
)
