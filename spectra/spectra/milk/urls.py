from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from spectra.milk.views import search, add

urlpatterns = [
    url(r'^add/?', add, name='add_search'),
    url(r'^', search, name='milk_search'),
]
