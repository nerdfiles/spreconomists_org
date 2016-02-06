from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from imagestore.models.bases.image import BaseImage

#from django.core.urlresolvers import reverse
from cms.models import CMSPlugin
from django.conf import settings

from livesettings.functions import config_value


from html_field.db.models import HTMLField
from html_field import html_cleaner

c = html_cleaner.HTMLCleaner(allow_tags=['a', 'img', 'em', 'strong', 'iframe'])



class UserProfile(models.Model):

    '''
    User Profile
    '''

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)

    def get_username(self):
        return self.username

    class Meta:
        abstract = True
        app_label = 'website'


class Member(UserProfile):

    '''
    Member Extensions to User Profile
    '''

    create_date = models.DateField(blank=True, null=True)
    # For storing Stripe Customer ID after purchase is made
    # @see https://stripe.com/docs/api#customer_object
    customer_id = models.CharField(max_length=64)

    class Meta:
        app_label = 'website'



class MemberPluginModel(CMSPlugin):

    '''
        Member Plugin Model
    '''
    member = models.ForeignKey(
        Member,
        related_name='plugins'
    )

    def __unicode__(self):
        return self.member.customer_id

    class Meta:
        app_label = 'website'


class GalleryItem(models.Model):

    '''
    Gallery Items are essentially deferred. Users will be expected to upload
    their media to a third-party host which might provide for hosting or a
    hosted embed.
    '''

    name = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    # Embeddable content from YouTube, etc.
    content = HTMLField(c, blank=True)

    class Meta:
        app_label = 'website'

class GalleryItemPluginModel(CMSPlugin):

    '''
        GalleryItem Plugin Model
    '''
    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'



class Gallery(models.Model):

    '''
    Galleries are groups of Items with arbitrary HTML chunks. Simpler than django-snippets.
    '''

    name = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    gallery_item = models.ForeignKey(GalleryItem, on_delete=models.CASCADE)

    class Meta:
        app_label = 'website'


class GalleryPluginModel(CMSPlugin):

    '''
        Gallery Plugin Model
    '''
    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'


