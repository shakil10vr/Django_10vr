# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='second_name',
        ),
    ]
