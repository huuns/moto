# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ProductA(models.Model):
    class Meta:
        ordering = ['id'] #ascending mode
        #ordering = ['-id'] #descending mode
        db_table = 'product_a'

    name_kr    = models.CharField(max_length=128, unique=True, verbose_name=u"한국어이름(name_kr)")
    name_en    = models.CharField(max_length=128, unique=True, verbose_name=u"영어이름(name_en)")
    maker_code = models.IntegerField(unique=True, verbose_name=u"메이커코드(maker_code)")
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)
