# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from imagestore.models.bases.image import BaseImage
import swapper
from sorl.thumbnail import ImageField, get_thumbnail
from django.utils.translation import ugettext_lazy as _
#from imagestore.utils import FilePathGenerator
#from imagestore.compat import get_user_model_name
#from django.db.models.signals import class_prepared

'''
def modify_fields(**kwargs):
    def wrap(cls):
        for field, prop_dict in kwargs.items():
            for prop, val in prop_dict.items():
                setattr(cls._meta.get_field(field), prop, val)
        return cls
    return wrap
'''

class ExtendedBaseImage(BaseImage):

  album_field = models.ForeignKey(swapper.get_model_name('imagestore', 'Album'),
      verbose_name=_('Mini Charge Album'),
      null=True,
      blank=True,
      related_name='mci_images')

  user_field = models.ForeignKey(get_user_model_name(),
      verbose_name=_('Mini Charge User'),
      null=True,
      blank=True,
      related_name='mci_images')

  class Meta(BaseImage.Meta):
    abstract = True
'''
def add_field(sender, **kwargs):
  if sender.__name__ == 'ExtendedBaseImage':
    album_field.contribute_to_class(sender, 'album')
    user.contribute_to_class(sender, 'user')
'''

'''
@modify_fields(album={
    'related_name': 'mci_images',
    'help_text': 'Mini charge album!'},
    user={
    'related_name': 'mci_images',
    'help_text': 'Mini charge user!'})
'''
class MiniChargeImage(ExtendedBaseImage):

    class Meta(ExtendedBaseImage.Meta):
        abstract = False
        app_label = 'mini_charge'
        db_table = 'mini_charge_image'

#class_prepared.connect(add_field)
