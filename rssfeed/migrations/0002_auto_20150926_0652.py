# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='web_url',
            field=models.URLField(max_length=254),
        ),
    ]
