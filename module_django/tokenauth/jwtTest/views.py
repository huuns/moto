#-*- coding:utf-8 -*-

#django & python
import time, logging, re
import logging.handlers

#rest
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#django
from jwtTest.models import ProductA
from jwtTest.serializers import ProductASerializer



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
class ProductAViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (JSONWebTokenAuthentication,)

    queryset = ProductA.objects.all()
    serializer_class = ProductASerializer
    pagination_class = LargeResultsSetPagination


## example
## get token     : curl -X GET -H "Content-Type: application/json" -d '{"username":"id~~~~","password":"pw~~~~"}' http://localhost:8000/api-token-auth/
## verify token  : curl -X GET -H "Content-Type: application/json" -d '{"username":"id~~~~","password":"pw~~~~"}' http://localhost:8000/api-token-verify/

## endpoint call : curl -H "Authorization: JWT ~~~tokenValue~~~ " http://localhost:8000/product_a/management/
