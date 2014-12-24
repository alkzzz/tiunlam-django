# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('judul', models.CharField(max_length=50)),
                ('isi', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False, verbose_name=b'Tampilkan di Halaman Depan')),
                ('gambar', models.ImageField(upload_to=b'gambar/featured', null=True, verbose_name=b'Featured Image', blank=True)),
                ('dokumen', models.FileField(upload_to=b'dokumen/%Y/%m/%d', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
