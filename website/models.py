from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from html_field import HTMLField


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


class Member(UserProfile):

    '''
    Member Extensions to User Profile
    '''

    title = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=100)


class GalleryItem(models.Model):

    '''
    '''

    title = models.CharField(max_length=255)
    content = models.HTMLField(max_length=1000)


class Gallery(models.Model):

    '''
    '''

    title = models.CharField(max_length=255)
    gallery_item = models.ForeignKey(GalleryItem, on_delete=models.CASCADE)

