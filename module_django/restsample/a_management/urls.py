# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from rest_framework import routers
from a_management import views

router = routers.DefaultRouter()
router.register(r'management',     views.ProductAViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
