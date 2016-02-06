from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^events$', views.events, name='events'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^contact$', views.contact, name='contact'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

