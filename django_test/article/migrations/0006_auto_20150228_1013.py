# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
        
class Migration(migrations.Migration):
    

    dependencies = [
        ('article', '0005_auto_20150226_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='first_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='second_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
