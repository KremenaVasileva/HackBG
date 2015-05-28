# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('projection_type', models.SmallIntegerField(default=1, choices=[(1, '2D'), (2, '3D'), (3, '4D'), (4, '4DX')])),
                ('time', models.DateTimeField()),
                ('movie', models.ForeignKey(to='website.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projection', models.ForeignKey(to='website.Projection')),
            ],
        ),
    ]
