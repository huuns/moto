from django.conf.urls import include, url 
from testapp import views

urlpatterns = [ 
    url(r'^st/' , views.test_view, name='test_view'),
]


