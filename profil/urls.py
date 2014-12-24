from django.conf.urls import patterns, url

from profil.views import DaftarProfil, DetailProfil

urlpatterns = patterns('',
    url(r'^$', DaftarProfil.as_view(), name='daftar-profil'),
    url(r'^(?P<slug>\S+)$', DetailProfil.as_view(), name='detail-profil'),
)