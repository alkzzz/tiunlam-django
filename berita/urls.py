from django.conf.urls import patterns, url
from berita.views import DaftarBerita, DetailBerita

urlpatterns = patterns('',
	url(r'^$', DaftarBerita.as_view(), name='daftar-berita'),
	url(r'^(?P<slug>\S+)$', DetailBerita.as_view(), name='detail-berita'),
)