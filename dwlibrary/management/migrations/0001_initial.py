# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('publisher', models.CharField(max_length=50)),
                ('publish_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('author', models.ForeignKey(blank=True, to='management.Author', null=True)),
            ],
        ),
    ]
