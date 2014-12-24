from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', include('homepage.urls', namespace="homepage")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^berita/', include('berita.urls', namespace="berita")),
    url(r'^profil/', include('profil.urls', namespace="profil")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Administrator"
admin.site.site_title="TI UNLAM"
admin.site.index_title="Admin Dashboard"
