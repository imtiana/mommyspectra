from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from spectra.milk.forms import MilkForm, LocationForm

from spectra.milk.models import MilkPost
from spectra.user.forms import UserForm

@login_required
def search(request):
    milk_posts = MilkPost.objects.filter(status=MilkPost.AVAILABLE)
    return render_to_response('milk_search.html', context={'posts': milk_posts})

@login_required
def add(request):
    context = RequestContext(request)

    if request.method == 'POST':
        location_form = LocationForm(data=request.POST)
        milk_form = MilkForm(data=request.POST)

        if location_form.is_valid() and milk_form.is_valid():
            location = location_form.save()
            MilkPost(quantity=milk_form.cleaned_data.get("quantity"), location=location, provider=request.user.userprofile, post_date=datetime.now()).save()

    return render_to_response('add_milk.html', context = context)
