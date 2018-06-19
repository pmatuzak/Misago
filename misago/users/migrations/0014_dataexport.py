# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-17 14:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import misago.users.models.dataexport


class Migration(migrations.Migration):

    dependencies = [
        ('misago_users', '0013_auto_20180609_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Requested'), (1, 'Processing'), (2, 'Ready'), (3, 'Expired')], db_index=True, default=0)),
                ('requester_name', models.CharField(max_length=255)),
                ('requested_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('export_file', models.FileField(blank=True, null=True, upload_to=misago.users.models.dataexport.get_export_upload_to)),
                ('requester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]