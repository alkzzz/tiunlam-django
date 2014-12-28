from django.shortcuts import render, render_to_response, RequestContext
from django.views import generic
from django.db.models import Max
from profil.models import Profil
from berita.models import Berita


def home(request, *args, **kwargs):
    daftar_profil = Profil.objects.order_by('created')
    berita = Berita.objects.filter(featured=True)
    berita_terbaru = Berita.objects.order_by('-created')[:4]
    semua_berita = Berita.objects.order_by('created')
    context = {
    	'semua_berita' : semua_berita,
        'daftar_berita': berita,
        'daftar_profil': daftar_profil,
        'berita_terbaru': berita_terbaru,

    }
    return render(request, 'homepage/index.html', context)