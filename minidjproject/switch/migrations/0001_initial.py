# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='switch_details',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('switch_model', models.CharField(max_length=100)),
                ('switch_ip', models.CharField(max_length=100)),
                ('netmask', models.CharField(max_length=100)),
                ('gateway', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
            ],
        ),
    ]
