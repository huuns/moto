#django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

#test
from samplepage import views

urlpatterns = [
    url(r'^autocomplete/',      views.awesomplete,    name='autocomplete_view' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
