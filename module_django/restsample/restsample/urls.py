# -*- coding: utf-8 -*-

#django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product_a/', include('a_management.urls')),

    # (r'^$', 'django_sample.plus.views.index'),
    # (r'^oauth2callback', 'django_sample.plus.views.auth_return'),
]
