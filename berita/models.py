from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.db import router
from django.forms import ValidationError
from django.core.urlresolvers import reverse

# Create your models here.

class Berita(models.Model):
	judul = models.CharField(max_length=150)
	isi = RichTextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	featured = models.BooleanField('Tampilkan di Halaman Depan', default=False)
	gambar = models.ImageField('Featured Image', upload_to='gambar/featured', blank=True, null=True)
	dokumen = models.FileField(upload_to='dokumen/%Y/%m/%d', blank=True)
	slug = models.SlugField(max_length=150, unique=True)

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

	def save(self, force_insert=False, force_update=False, using=None,
			 update_fields=None):
		using = using or router.db_for_write(self.__class__, instance=self)
		if force_insert and (force_update or update_fields):
			raise ValueError("Cannot force both insert and updating in model saving.")

		if update_fields is not None:
			if len(update_fields) == 0:
				return

			update_fields = frozenset(update_fields)
			field_names = set()

			for field in self._meta.fields:
				if not field.primary_key:
					field_names.add(field.name)

					if field.name != field.attname:
						field_names.add(field.attname)

			non_model_fields = update_fields.difference(field_names)

			if non_model_fields:
				raise ValueError("The following fields do not exist in this "
								 "model or are m2m fields: %s"
								 % ', '.join(non_model_fields))

		elif not force_insert and self._deferred and using == self._state.db:
			field_names = set()
			for field in self._meta.concrete_fields:
				if not field.primary_key and not hasattr(field, 'through'):
					field_names.add(field.attname)
			deferred_fields = [
				f.attname for f in self._meta.fields
				if (f.attname not in self.__dict__ and
					isinstance(self.__class__.__dict__[f.attname], DeferredAttribute))
			]

			loaded_fields = field_names.difference(deferred_fields)
			if loaded_fields:
				update_fields = frozenset(loaded_fields)

		self.save_base(using=using, force_insert=force_insert,
					   force_update=force_update, update_fields=update_fields)
		if self.gambar:
		    super(Berita, self).save()
		    image = Image.open(self.gambar)
		    (width, height) = image.size
		    size = (800, 400)
		    image = image.resize(size, Image.ANTIALIAS)
		    image.save(self.gambar.path)

	save.alters_data = True


