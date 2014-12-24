# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0002_auto_20141120_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='berita',
            options={'verbose_name_plural': 'Edit Berita'},
        ),
    ]
