from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.template import RequestContext

from spectra.milk.models import MilkPost, MilkTransaction
from spectra.user.forms import UserForm

@login_required
def search(request):
    context = RequestContext(request)
    milk_posts = MilkPost.objects.filter(status=MilkPost.AVAILABLE)
    if request.GET.get('search_city'):
        milk_posts = milk_posts.filter(location__city=request.GET.get('search_city'))
    context['posts'] = milk_posts
    return render_to_response('milk_search.html', context=context)

def transaction(request):
    context = RequestContext(request)
    post = MilkPost.objects.get(id=request.GET.get('post'))
    context['post'] = post
    return render_to_response('transaction.html', context=context)


def post_transaction(request):
    context = RequestContext(request)
    post = MilkPost.objects.get(id=request.GET.get('post'))
    transaction = MilkTransaction(post=post, customer=request.user.userprofile, approval_date=None, completed_date=None, provider_rating=None, customer_rating=None)
    transaction.save()
    return render_to_response('post_transaction.html', context=context)
