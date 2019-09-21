# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 06:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_title', models.CharField(max_length=222)),
                ('country_code', models.IntegerField()),
                ('country_iso', models.CharField(max_length=222)),
                ('country_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('country_track', models.TextField(blank=True, null=True)),
                ('country_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_title', models.CharField(max_length=222)),
                ('state_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('state_track', models.TextField(blank=True, null=True)),
                ('state_ctid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
                ('state_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]