# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('python', 'Python'), ('java', 'JAVA'), ('go', 'GO'), ('js', 'JS'), ('c', 'C'), ('c++', 'C++'), ('gcc', 'GCC'), ('r', 'R')], max_length=50, verbose_name='语言名称')),
                ('version', models.CharField(max_length=10, verbose_name='语言版本')),
                ('status', models.SmallIntegerField(choices=[(0, '未使用'), (1, '正在使用'), (2, '已删除')], verbose_name='语言状态')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'version')]),
        ),
    ]