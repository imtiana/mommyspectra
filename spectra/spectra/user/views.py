from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django import forms
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from spectra.user.forms import UserForm, UserProfileForm
from spectra.milk.models import *

# Create your views here.

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/milk/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    context = RequestContext(request)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        up_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and up_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            up = up_form.save(commit=False)
            up.user = user
            up.save()

            user = authenticate(username=user.username, password=user_form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/milk/')

    else:
        user_form = UserForm()
        up_form = UserProfileForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'up_form': up_form},
            context)

def profile(request):
    context = RequestContext(request)
    milk_posts = MilkPost.objects.filter(provider=request.user.userprofile)
    context['posts'] = milk_posts
    return render_to_response('profile.html', context=context)
