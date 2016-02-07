from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
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


class MemberPluginModel(CMSPlugin):

    '''
    Member Extensions to User Profile
    '''

    create_date = models.DateField(blank=True, null=True)
    # For storing Stripe Customer ID after purchase is made
    # @see https://stripe.com/docs/api#customer_object
    customer_id = models.CharField(max_length=64)

    def __unicode__(self):
        return self.first_name

    class Meta:
        app_label = 'website'


class Member(UserProfile):
    '''
        Member Plugin Model
    '''
    member = models.ForeignKey(
        MemberPluginModel,
        related_name='plugins'
    )

    def __unicode__(self):
        return self.member.customer_id

    class Meta:
        app_label = 'website'


class Action(models.Model):

    '''
    Event Items are essentially deferred. They are non-normative, highly descriptive,
    and maybe even virulently supplied. Heaven's sake, it's a Russellian nominalism.
    '''

    name = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    actionStatus = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'


class EventItemPluginModel(CMSPlugin):
    '''
    Event Items are essentially deferred. They are non-normative, highly descriptive,
    and maybe even virulently supplied. Heaven's sake, it's a Russellian nominalism.
    '''

    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    canonical_date = models.CharField(max_length=255)
    canonical_location = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    url = models.CharField(max_length=255)
    registration_url = models.CharField(max_length=255)
    content = HTMLField(c, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'


class EventItem(models.Model):
    '''
        EventItem Plugin Model
    '''
    plugin = models.ForeignKey(
        EventItemPluginModel,
        related_name='event_item'
    )


class GalleryPluginModel(CMSPlugin):
    '''
    Galleries are groups of Items with arbitrary HTML chunks. Simpler than django-snippets.
    '''

    name = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)

    def get_items(self):
        q = GalleryItemPluginModel.objects.all()
        return q

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'


class Gallery(models.Model):

    '''
        Gallery Plugin Model
    '''
    plugin = models.ForeignKey(
        GalleryPluginModel,
        related_name='gallery'
    )


class GalleryItemPluginModel(CMSPlugin):
    '''
    Gallery Items are essentially deferred. Users will be expected to upload
    their media to a third-party host which might provide for hosting or a
    hosted embed.
    '''

    name = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    # Embeddable content from YouTube, etc.
    address = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    youtube_url = models.CharField(max_length=255)
    content = HTMLField(c, blank=True)
    gallery = models.ForeignKey(GalleryPluginModel, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'website'


class GalleryItem(models.Model):
    '''
        GalleryItem Plugin Model
    '''
    plugin = models.ForeignKey(
        GalleryItemPluginModel,
        related_name='gallery_item'
    )
