from django.views import generic

from profil.models import Profil

class DaftarProfil(generic.ListView):

    model = Profil

    def get_context_data(self, **kwargs):
        context = super(DaftarProfil, self).get_context_data(**kwargs)
        return context

class DetailProfil(generic.DetailView):

	model = Profil

	def get_context_data(self, **kwargs):
		context = super(DetailProfil, self).get_context_data(**kwargs)
		context['daftar_profil'] = Profil.objects.order_by('created')
		return context
