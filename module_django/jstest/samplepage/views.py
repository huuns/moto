# -*- coding:utf-8 -*-

#django
from django.shortcuts import render
from django.http import HttpResponseNotFound, QueryDict, HttpResponse
from django.http import HttpRequest
from django.template import loader


def awesomplete(request):
    try:
        return render(request, 'test_awesomplete.html', {})
    except:
        return HttpResponseNotFound('error not found')
