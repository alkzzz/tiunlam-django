# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0003_auto_20141125_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='berita',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Edit Berita'},
        ),
    ]
