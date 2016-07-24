from django import forms

from spectra.milk.models import Location

class MilkForm(forms.Form):
    quantity = forms.IntegerField()

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('address', 'city', 'region', 'state', 'country')