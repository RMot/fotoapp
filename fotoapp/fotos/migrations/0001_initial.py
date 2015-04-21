# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name=b'name')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'im\xc3\xa1gen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
