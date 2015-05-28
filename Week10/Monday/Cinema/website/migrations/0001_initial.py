# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('rating', models.FloatField()),
                ('movie_type', models.PositiveSmallIntegerField(default=1)),
                ('cover', models.ImageField(upload_to='')),
            ],
        ),
    ]
