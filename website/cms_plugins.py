# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from website import *

_ = lambda s: s



'''
class MemberProfilePlugin(CMSPluginBase):
    model = MemberProfilePluginModel
    name = _("Member Profile")
    render_template = "profile.tmpl"

    def render(self, context, instance, placeholder):
        #self.render_template = instance.template
        context.update({
            'instance': instance
        })
        return context

plugin_pool.register_plugin(MemberProfilePlugin)
'''

