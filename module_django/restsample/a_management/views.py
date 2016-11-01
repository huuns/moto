#-*- coding:utf-8 -*-

#django & python
import time, logging, re
import logging.handlers

#rest
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


#django
from a_management.models import ProductA
from a_management.serializers import ProductASerializer



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

@permission_classes((AllowAny, ))
class ProductAViewSet(viewsets.ModelViewSet):
    queryset = ProductA.objects.all()
    serializer_class = ProductASerializer
    pagination_class = LargeResultsSetPagination
