# -*- coding:utf-8 -*-

#models.py =====================================================================

from __future__ import unicode_literals

#django
from django.db import models

#python
import uuid

#boto
from storages.backends.s3boto import S3BotoStorage

def set_uuid_filename(instance, filename):
    return str(uuid.uuid4())+filename

class SAMPLE(models.Model):
    class Meta:
        ordering = ['-id'] #descending mode
        db_table = 'sample'

    myfile = models.FileField(upload_to=set_uuid_filename, default='default/none.txt', storage=S3BotoStorage(bucket='bucketname'))
#===============================================================================



#serializers.py ================================================================
#rest
from rest_framework import serializers

from models import SAMPLE

class SAMPLESerializer(serializers.HyperlinkedModelSerializer):

    myfile = serializers.FileField(max_length=None, use_url=True, required=False)

    class Meta:
        model = sample
        fields = ('id', 'myfile', 'url')
#===============================================================================




#views.py ======================================================================
#django
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponseNotFound, QueryDict, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings

#rest
from rest_framework import viewsets, status, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import detail_route, list_route, permission_classes

from models import SAMPLE
from serializers import SAMPLESerializer

#boto
from boto.s3.connection import S3Connection, Bucket, Key


@permission_classes((IsAdminUser, ))
class SAMPLEViewSet(viewsets.ModelViewSet):
    queryset = SAMPLE.objects.all()
    serializer_class = SAMPLESerializer

    def create(self, request, format=None):
        serializer = SAMPLESerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host='s3.ap-northeast-2.amazonaws.com')
        b = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
        k = Key(b)

        k.key = str(instance.left_footscan_stl)
        b.delete_key(k)

        k.key = str(instance.right_footscan_stl)
        b.delete_key(k)

        instance.delete()
#===============================================================================
