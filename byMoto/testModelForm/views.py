from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from testModelForm.models import TestData
from testModelForm.forms import AddDataForm

class DataListView(ListView):
    template_name = 'dataList.html'
    model = TestData

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        context['dlist'] = self.model.objects.all()
        return context

class AddDataView(FormView):
    success_url = "/testModel"
    template_name = 'addData.html'
    form_class = AddDataForm

    def form_valid(self, form):
        sg = form.save()
        print sg.__dict__

        messages.info( self.request, "successfully added" )
        return super(AddDataView, self).form_valid(form)
