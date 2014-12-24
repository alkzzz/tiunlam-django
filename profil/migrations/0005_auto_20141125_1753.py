# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_auto_20141125_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'ordering': ['created'], 'verbose_name_plural': 'Edit Profil'},
        ),
    ]
