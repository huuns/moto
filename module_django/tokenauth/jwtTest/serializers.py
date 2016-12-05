# -*- coding:utf-8 -*-
from rest_framework import serializers

from jwtTest.models import ProductA

class ProductASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductA
        fields = ('id', 'name_kr', 'name_en', 'maker_code', 'url' )
