# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dName', models.CharField(default=b'data_name', max_length=30)),
                ('dDescription', models.CharField(default=b'data_description', max_length=300)),
                ('dLevel', models.IntegerField(default=11, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16')])),
                ('dDate', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
