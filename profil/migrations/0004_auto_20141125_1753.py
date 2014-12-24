# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_auto_20141125_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'ordering': ['created'], 'verbose_name_plural': 'Edit Menu Profil'},
        ),
    ]
