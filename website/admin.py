# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from models import UserProfile
#from django import forms
import imagestore.admin
from models import GalleryItem
from models import Gallery
from models import Member

class UserProfileAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
    #def __init__(self, *args, **kwargs):
        #super(UserProfileAdmin, self).__init__(*args, **kwargs)

    #class Meta:
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

admin.site.register(Gallery, GalleryAdmin)


class GalleryItemAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(GalleryItemAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = GalleryItem

admin.site.register(GalleryItem, GalleryItemAdmin)

