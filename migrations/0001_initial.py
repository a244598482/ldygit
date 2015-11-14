# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=5)),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.CharField(max_length=3)),
                ('Countury', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=7)),
                ('Title', models.CharField(max_length=12)),
                ('Publisher', models.CharField(max_length=20)),
                ('PublishDate', models.CharField(max_length=15)),
                ('Price', models.CharField(max_length=3)),
                ('AuthorID', models.ForeignKey(to='addr_book.Author')),
            ],
        ),
    ]
