# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class ResponsiveWrapperPlugin(CMSPlugin):
    desktop = models.BooleanField(_('Visible on desktops'), help_text=_('higher than 860px'), default=True)
    tablet = models.BooleanField(_('Visible on tablets'), help_text=_('520px to 860px'), default=True)
    phone = models.BooleanField(_('Visible on phones'), help_text=_('520px and below'), default=True)

    def __unicode__(self):
        return u'Desktop: %s, Tablets: %s, Phones: %s' % (self.desktop, self.tablet, self.phone)

    def get_class(self):
        classes = {
            # Phone, Tablet, Desktop: class
            '100': 'visible-phone',
            '010': 'visible-tablet',
            '001': 'visible-desktop',
            '011': 'hidden-phone',
            '101': 'hidden-tablet',
            '110': 'hidden-desktop',
            '000': '',
            '111': '',
        }

        return classes['%i%i%i' % (self.phone, self.tablet, self.desktop)]
