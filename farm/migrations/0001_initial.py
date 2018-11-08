# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('decription', models.TextField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
