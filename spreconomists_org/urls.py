# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
import views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^$', views.home, name='home'),
    #url(r'^about$', views.about, name='about'),
    #url(r'^events$', views.events, name='events'),
    #url(r'^gallery$', views.gallery, name='gallery'),
    #url(r'^contact$', views.contact, name='contact'),

    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),

]

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

urlpatterns = patterns('',
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

