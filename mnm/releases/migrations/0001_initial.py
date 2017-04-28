# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateTimeField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('_version', models.CharField(db_index=True, max_length=255)),
                ('version_major', models.PositiveIntegerField()),
                ('version_minor', models.PositiveIntegerField()),
                ('version_patch', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-_version',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('version_major', 'version_minor', 'version_patch')]),
        ),
    ]