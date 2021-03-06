# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-20 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attd', '0002_auto_20170920_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical', 'Mechanical'), ('Mathematics', 'Mathematics')], help_text='department', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
