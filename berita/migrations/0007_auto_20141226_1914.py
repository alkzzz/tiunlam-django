# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0006_auto_20141125_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='slug',
            field=models.SlugField(unique=True, max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
