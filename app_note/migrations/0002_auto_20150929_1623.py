# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtags',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
