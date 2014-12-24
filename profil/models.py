from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class Profil(models.Model):
	judul = models.CharField(max_length=50)
	isi = RichTextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, unique=True)

	class Meta:
		verbose_name_plural = "Edit Profil"
		ordering = ["created"]

	def __unicode__(self):
		return self.judul

	def get_absolute_url(self):
		return reverse ('profil:detail-profil', kwargs={"slug":self.slug})
