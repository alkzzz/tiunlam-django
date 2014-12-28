from haystack import indexes
from berita.models import Berita

class BeritaIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Berita