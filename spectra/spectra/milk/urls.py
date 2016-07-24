from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from spectra.milk.views import search, add, transaction, post_transaction

urlpatterns = [
    url(r'^add/?', add, name='add_search'),


urlpatterns = [
	url(r'^add/?', add, name='add_search'),
    url(r'^transaction/?', transaction, name='transaction'),
    url(r'^post_transaction/?', post_transaction, name='post_transaction'),
    url(r'^', search, name='milk_search'),
]
