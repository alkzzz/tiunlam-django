from haystack.views import SearchView
from django.shortcuts import render_to_response

class CustomSearchView(SearchView):
	
	def create_response(self):
		context = {
		'query': self.query,
		'form': self.form,
		'suggestion': None,
		'hasil_cari': self.results
		}

		if self.results and hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
			context['suggestion'] = self.form.get_suggestion()
		
		context.update(self.extra_context())
		return render_to_response(self.template, context, context_instance=self.context_class(self.request))

