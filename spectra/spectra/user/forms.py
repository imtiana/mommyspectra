from django import forms
from django.contrib.auth.models import User

from spectra.user.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'biography')
