
from django.conf.urls import patterns, url, include
from django.contrib import admin
import views

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.home, name='home'),
    url(r'^events$', views.events, name='events'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^contact$', views.contact, name='contact'),

    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),

]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

