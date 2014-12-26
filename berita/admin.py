from django.db import models
from django.contrib import admin
from berita.models import Berita
from customwidget import AdvancedClearableFileInput, AdvancedFileInput


# Register your models here.
class AdminBerita(admin.ModelAdmin):

	fields = ('judul', 'isi', 'featured', 'gambar', 'dokumen')

	formfield_overrides = {
    models.FileField: {'widget': AdvancedFileInput},
    models.ImageField: {'widget': AdvancedClearableFileInput},
    }

admin.site.register(Berita, AdminBerita)