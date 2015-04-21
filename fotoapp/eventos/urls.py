from eventos.views import EventList, EventPhotoList

__author__ = 'Mixer'

from django.conf.urls import patterns, url

from eventos import views

urlpatterns = patterns('',
    url(r'^$', EventList.as_view()),
    url(r'^evento/([\w-]+)/$', EventPhotoList.as_view(), name = "EventPhotoListView"),
)