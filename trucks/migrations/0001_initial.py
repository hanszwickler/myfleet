# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comments', models.CharField(max_length=200)),
                ('maintenance_date', models.DateTimeField(verbose_name='TÜV Datum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wheels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('distance', models.IntegerField(default=0)),
                ('truck', models.ForeignKey(to='trucks.Truck')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
