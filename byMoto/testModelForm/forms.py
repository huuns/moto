# -*- coding: utf-8 -*-

from django import forms
from testModelForm.models import TestData

class AddDataForm(forms.ModelForm):

  class Meta:
      model = TestData
      fields = ('dName', 'dDescription', 'dLevel', 'dDate',)
      widgets = {
                  'dName':        forms.TextInput( attrs={'class': 'form-control',}),
                  'dDescription': forms.Textarea(  attrs={'class': 'form-control',}),
                  'dLevel':       forms.Select(    attrs={'class': 'form-control',}),
                  'dDate':        forms.DateInput( attrs={'class': 'form-control', 'readonly': True,}),
      }
      labels = {
                  'dName': "Name",
                  'dDescription': "Description",
                  'dLevel': "Level",
                  'dDate': "Date",
      }


