# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from models import UserProfile
#from django import forms
import imagestore.admin
from mini_charge.models import Charge
from mini_charge.models import MiniChargeImage
#from mini_charge.models.album import MiniChargeAlbum

class UserProfileAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
    #def __init__(self, *args, **kwargs):
        #super(UserProfileAdmin, self).__init__(*args, **kwargs)

    #class Meta:
        #model = UserProfile

#admin.site.register(UserProfile, UserProfileAdmin)



admin.site.register(Charge)


class MiniChargeImageAdmin(imagestore.admin.ImageAdmin):

    def __init__(self, *args, **kwargs):
        super(MiniChargeImageAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = MiniChargeImage

admin.site.register(MiniChargeImage, MiniChargeImageAdmin)

