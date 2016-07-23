from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from spectra.milk.views import search

urlpatterns = [
    url(r'^', search, name='milk_search'),
]
