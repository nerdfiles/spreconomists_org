# -*- coding: utf-8 -*-

from django.db import models
from imagestore.models.bases.image import BaseImage
from imagestore.models.bases.album import BaseAlbum

#from django.core.urlresolvers import reverse
from cms.models import CMSPlugin
from django.conf import settings

from livesettings.functions import config_value

class MiniChargeImage(BaseImage):

    class Meta(BaseImage.Meta):
        abstract = False
        app_label = 'mini_charge'
        db_table = 'mini_charge_image'


class MiniChargeAlbum(BaseAlbum):

    class Meta(BaseAlbum.Meta):
        abstract = False
        app_label = 'mini_charge'
        db_table = 'mini_charge_album'



class Charge(models.Model):

    '''
        Charge Model
        @see https://stripe.com/docs/api#create_charge
    '''

    def __init__(self, *args, **kwargs):
        super(Charge, self).__init__(*args, **kwargs)
        #import stripe
        #DEBUG = settings.DEBUG
        #STRIPE_TEST_MODE = config_value('laurenmcmanus', 'STRIPE_TEST_MODE')
        #if DEBUG == True or STRIPE_TEST_MODE == True:
        #    stripe.api_key = config_value('laurenmcmanus', 'STRIPE_TEST_PUBLIC_KEY')
        #else:
        #    stripe.api_key = config_value('laurenmcmanus', 'STRIPE_LIVE_PUBLIC_KEY')
        #self.stripe = stripe

    name = models.CharField(max_length=50)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        null=True,
        blank=True)
    currency = models.CharField(
        max_length=10,
        help_text='"USD", "EUR", etc. Review https://support.stripe.com/questions/which-currencies-does-stripe-support for more detail.'
    )
    description = models.CharField(max_length=300)

    # Expect user to create a price specification before attaching
    # a work of art or product.
    work = models.ManyToManyField(MiniChargeImage)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'mini_charge'


class MiniChargePluginModel(CMSPlugin):

    '''
        MiniCharge Plugin Model
    '''
    charge = models.ForeignKey(
        Charge,
        related_name='plugins'
    )

    def __unicode__(self):
        return self.charge.name

    class Meta:
        app_label = 'mini_charge'

