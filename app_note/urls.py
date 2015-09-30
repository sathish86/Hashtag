from django.conf.urls import patterns, url
from app_note import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))