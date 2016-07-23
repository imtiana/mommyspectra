from django.db import models

from spectra.user.models import UserProfile

class Location(models.Model):
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)


class MilkTransaction(models.Model):
    provider = models.ManyToManyField(UserProfile, related_name="provider")
    customer = models.ManyToManyField(UserProfile, related_name="customer")
    request_date = models.DateField()
    quantity = models.IntegerField()
    approval_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    provider_rating = models.IntegerField(blank=True, null=True)
    customer_rating = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
