from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

urlpatterns = patterns('',
   	url(r'^$', 'elena.views.home', name='home'),
	url(r'^calendar/$', 'elena.views.calendar', name='calendar'),
)


urlpatterns += staticfiles_urlpatterns()
