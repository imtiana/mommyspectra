from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from spectra.user.views import profile, register, user_login, user_logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/?$', user_login, name='login'),
    url(r'^register/?$', register),
    url(r'^logout/?$', user_logout, name='logout'),
    url(r'^profile/?$', profile, name='profile'),
    url(r'^milk/?', include('spectra.milk.urls')),
    url(r'^', TemplateView.as_view(template_name='index.html'))
]
