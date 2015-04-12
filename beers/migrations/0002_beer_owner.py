# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='owner',
            field=models.ForeignKey(related_name='beers', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
