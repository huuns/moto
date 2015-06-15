# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import Context

def formstest_view(request):
  try:
    context = Context({'name': 'forms_test_template',
                       'var1': 'var1_text',
                       'var2': 'var2_text',
                       'var3': 'var3_text',
              })
    return render(request, 'formstest.html', context)
  except:
    return HttpResponseNotFound(u'<h1>잘못된 접근</h1>')


