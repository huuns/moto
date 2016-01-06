# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def test_view(request):
  try:
    return render(request, 'statictest.html')
  except:
    return HttpResponseNotFound(u'<h1>잘못된 접근입니다.</h1>')
