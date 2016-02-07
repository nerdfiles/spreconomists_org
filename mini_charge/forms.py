# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils import load_class

#class ImageForm(forms.Form):
    #pass

#class AlbumForm(forms.Form):
    #pass


ImageForm = load_class(getattr(settings, 'IMAGESTORE_IMAGE_FORM', 'imagestore.forms.ImageForm'))
AlbumForm = load_class(getattr(settings, 'IMAGESTORE_ALBUM_FORM', 'imagestore.forms.AlbumForm'))

class ChargeForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=7)
