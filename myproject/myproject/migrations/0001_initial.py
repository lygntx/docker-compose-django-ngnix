# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'fibonacci', b'fibonacci'), (b'power', b'power')], max_length=20)),
                ('status', models.CharField(choices=[(b'pending', b'pending'), (b'started', b'started'), (b'finished', b'finished'), (b'failed', b'failed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('argument', models.PositiveIntegerField()),
                ('result', models.IntegerField(null=True)),
            ],
        ),
    ]
