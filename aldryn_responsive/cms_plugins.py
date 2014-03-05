# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ResponsiveWrapperPlugin


class ResponsiveWrapperCMSPlugin(CMSPluginBase):
    model = ResponsiveWrapperPlugin
    name = _("Responsive Wrapper")
    render_template = 'aldryn_responsive/plugins/wrapper.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ResponsiveWrapperCMSPlugin)
