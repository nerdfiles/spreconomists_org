# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from models import UserProfile

class UserProfileAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
    #def __init__(self, *args, **kwargs):
        #super(UserProfileAdmin, self).__init__(*args, **kwargs)

    #class Meta:
        #model = UserProfile

#admin.site.register(UserProfile, UserProfileAdmin)

