# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import EventItem, EventItemPluginModel
from .models import GalleryItem, GalleryItemPluginModel
from .models import Gallery, GalleryPluginModel
from .models import UserProfile, Member, MemberPluginModel

class ItemInlineAdmin(admin.StackedInline):
    model = EventItem

class GalleryItemInlineAdmin(admin.StackedInline):
    model = GalleryItem

class GalleryInlineAdmin(admin.StackedInline):
    model = Gallery

class EventsPlugin(CMSPluginBase):
    model = EventItemPluginModel
    name = _("Events Plugin")
    render_template = "events_plugin.html"
    inlines = (ItemInlineAdmin,)
    cache = False

    def render(self, context, instance, placeholder):
        context = super(EventsPlugin, self).render(context, instance, placeholder)
        #context.update({
            #'instance': instance,
        #})
        return context

plugin_pool.register_plugin(EventsPlugin)


class GalleryItemPlugin(CMSPluginBase):
    model = GalleryItemPluginModel
    #model = GalleryItem
    name = _("Gallery Item Plugin")
    render_template = "galleryitem_plugin.html"
    inlines = (GalleryItemInlineAdmin,)

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
    inlines = (GalleryInlineAdmin,)

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

    cache = False
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(MemberPlugin)
'''
