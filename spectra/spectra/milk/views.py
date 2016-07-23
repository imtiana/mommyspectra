from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from spectra.milk.models import MilkPost
from spectra.user.forms import UserForm

@login_required
def search(request):
    milk_posts = MilkPost.objects.filter(status=MilkPost.AVAILABLE)
    return render_to_response('milk_search.html', context={'posts': milk_posts})
