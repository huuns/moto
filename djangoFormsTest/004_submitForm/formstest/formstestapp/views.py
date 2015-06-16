# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import Context

from formstestapp.forms import TestForm
from django.views.generic.edit import FormView

class Formstest_view(FormView):
    template_name = 'formstest.html'
    success_url = '/success/'
    form_class = TestForm

    def get_context_data(self, **kwargs):
      context = super(Formstest_view, self).get_context_data(**kwargs)
      context['name'] = 'forms_test_template'
      context['var1'] = 'var1_text'
      context['var2'] = 'var2_text'
      context['var3'] = 'var3_text'
      context['form'] = TestForm()
      return context

    def form_valid(self, form):
      form.submitted(self.request)
      return super(Formstest_view, self).form_valid(form)

