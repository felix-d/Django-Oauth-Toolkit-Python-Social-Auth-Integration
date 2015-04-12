# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(default=b'', max_length=100)),
                ('beer_type', models.CharField(default=b'', max_length=100)),
                ('ml', models.IntegerField(default=330)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
