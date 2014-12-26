from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Berita(models.Model):
	judul = models.CharField(max_length=150)
	isi = RichTextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	featured = models.BooleanField('Tampilkan di Halaman Depan', default=False)
	gambar = models.ImageField('Featured Image', upload_to='gambar/featured', blank=True, null=True)
	dokumen = models.FileField(upload_to='dokumen/%Y/%m/%d', blank=True)
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	class Meta:
		verbose_name_plural = "Edit Berita"
		ordering = ["-created"]

	def __unicode__(self):
		return self.judul

	def get_absolute_url(self):
		return reverse ('berita:detail-berita', kwargs={"slug":self.slug})

	def clean(self):
		if self.featured:
			if not self.gambar:
				raise ValidationError('Pilih gambar yang akan ditampilkan di halaman depan')

	def save(self, *args, **kwargs):
		if self.gambar:
			super(Berita, self).save()
			image = Image.open(self.gambar)
			(width, height) = image.size
			size = (800, 400)
			image = image.resize(size, Image.ANTIALIAS)
			image.save(self.gambar.path)
		self.slug = slugify(self.judul)
		super(Berita, self).save(*args, **kwargs)


