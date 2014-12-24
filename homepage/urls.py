from django.conf.urls import patterns, url, include

from homepage.views import home

urlpatterns = patterns('',
	url(r'^$', home, name='index'),
)