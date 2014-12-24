# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0004_auto_20141125_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='slug',
            field=models.SlugField(default=None, unique=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='berita',
            name='judul',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
