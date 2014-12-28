from django.views import generic
from berita.models import Berita
from profil.models import Profil

class DaftarBerita(generic.ListView):

	model = Berita

	def get_context_data(self, **kwargs):
		context = super(DaftarBerita, self).get_context_data(**kwargs)
		context['daftar_profil'] = Profil.objects.order_by('created')
		return context	

class DetailBerita(generic.DetailView):

    model = Berita

    def get_context_data(self, **kwargs):
        context = super(DetailBerita, self).get_context_data(**kwargs)
        context['daftar_profil'] = Profil.objects.order_by('created')
        return context

