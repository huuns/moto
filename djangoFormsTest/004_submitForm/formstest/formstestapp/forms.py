# -*- coding: utf-8 -*-

from django import forms


class TestForm(forms.Form):
  textField1 = forms.CharField(label="input text filed 1")
  textField2 = forms.CharField(label="input text field 2")

  def submitted(self, request):
    print "submitted!!!!!"
    print "submitted!!!!!"
    print "submitted!!!!!"
    print "submitted!!!!!"
    print request.POST['textField1']
    print request.POST['textField2']



