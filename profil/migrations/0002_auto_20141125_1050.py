# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'ordering': ['-judul'], 'verbose_name_plural': 'Edit Profil'},
        ),
    ]
