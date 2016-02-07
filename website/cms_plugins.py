# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _


from website import *

_ = lambda s: s


from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import EventItem, EventItemPluginModel
from .models import GalleryItem, GalleryItemPluginModel
from .models import Gallery, GalleryPluginModel
from .models import UserProfile, Member, MemberPluginModel

class EventsPlugin(CMSPluginBase):
    model = EventItemPluginModel
    #model = EventItem
    name = _("Events Plugin")
    render_template = "events_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(EventsPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(EventsPlugin)


class GalleryItemPlugin(CMSPluginBase):
    model = GalleryItemPluginModel
    #model = GalleryItem
    name = _("Gallery Item Plugin")
    render_template = "galleryitem_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(GalleryItemPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(GalleryItemPlugin)


class GalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    #model = Gallery
    name = _("Gallery Plugin")
    render_template = "gallery_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(GalleryPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(GalleryPlugin)


'''
class MemberPlugin(CMSPluginBase):
    model = MemberPluginModel
    #model = Member
    name = _("Member Profile")
    render_template = "profile.tmpl"

    def render(self, context, instance, placeholder):
        #self.render_template = instance.template
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(MemberPlugin)
'''
