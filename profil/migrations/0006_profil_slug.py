# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0005_auto_20141125_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 11, 26, 1, 51, 38, 648439, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
