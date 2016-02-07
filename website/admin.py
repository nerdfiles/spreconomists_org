# -*- coding: utf-8 -*-
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin
#from django import forms
import imagestore.admin

from .models import EventItem, EventItemPluginModel
from .models import GalleryItem, GalleryItemPluginModel
from .models import Gallery, GalleryPluginModel
from .models import UserProfile
from .models import Member, MemberPluginModel


class UserProfileAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
    # def __init__(self, *args, **kwargs):
        #super(UserProfileAdmin, self).__init__(*args, **kwargs)

    # class Meta:
        #model = UserProfile

#admin.site.register(UserProfile, UserProfileAdmin)


class MemberAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(MemberAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = Member

admin.site.register(Member, MemberAdmin)


class GalleryAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(GalleryAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = Gallery

admin.site.register(GalleryPluginModel, GalleryAdmin)


class EventItemAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(EventItemAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = EventItem

admin.site.register(EventItemPluginModel, EventItemAdmin)


class GalleryItemAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(GalleryItemAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = GalleryItem

admin.site.register(GalleryItemPluginModel, GalleryItemAdmin)
