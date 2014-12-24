# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='berita',
            options={'verbose_name_plural': 'Daftar Berita'},
        ),
    ]
