# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0005_auto_20141125_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='slug',
            field=models.SlugField(unique=True, max_length=150),
            preserve_default=True,
        ),
    ]
