# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tools.Type', verbose_name='上级类别'),
        ),
    ]