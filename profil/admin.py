from django.contrib import admin
from profil.models import Profil

class AdminProfil(admin.ModelAdmin):

	prepopulated_fields = {'slug':('judul',)}

admin.site.register(Profil, AdminProfil)
# Register your models here.
