from django.shortcuts import render
from django.views import generic
from django.db.models import Max
from profil.models import Profil
from berita.models import Berita


def home(request, *args, **kwargs):
    daftar_profil = Profil.objects.order_by('created')
    berita = Berita.objects.filter(featured=True)
    berita_terbaru = Berita.objects.order_by('-created')[:4]
    context = {
        'daftar_berita': berita,
        'daftar_profil': daftar_profil,
        'berita_terbaru': berita_terbaru,

    }
    return render(request, 'homepage/index.html', context)