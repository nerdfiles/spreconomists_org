# -*- coding: utf-8 -*-

#from django import forms
from django.contrib import admin
import imagestore.admin
from mini_charge.models import Charge
from mini_charge.models import MiniChargeImage
from mini_charge.models import MiniChargeAlbum


admin.site.register(Charge)


class MiniChargeImageAdmin(imagestore.admin.ImageAdmin):

    def __init__(self, *args, **kwargs):
        super(MiniChargeImageAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = MiniChargeImage

admin.site.register(MiniChargeImage, MiniChargeImageAdmin)

class MiniChargeAlbumAdmin(imagestore.admin.AlbumAdmin):

    def __init__(self, *args, **kwargs):
        super(MiniChargeAlbumAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = MiniChargeAlbum

admin.site.register(MiniChargeAlbum, MiniChargeAlbumAdmin)
