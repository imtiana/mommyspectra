from django.db import models

from spectra.user.models import UserProfile

class Location(models.Model):
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)


class MilkPost(models.Model):
    AVAILABLE = 'available'
    PENDING = 'pending'
    CANCELLED = 'cancelled'

    POST_STATUS = (
        (AVAILABLE, 'Available'),
        (PENDING, 'Pending'),
        (CANCELLED, 'Cancelled')
    )

    provider = models.ForeignKey(UserProfile, related_name="provider")
    quantity = models.IntegerField()
    post_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    status = models.CharField(max_length=20, choices=POST_STATUS, default=AVAILABLE)


class MilkTransaction(models.Model):
    post = models.ForeignKey(MilkPost)
    customer = models.ForeignKey(UserProfile, related_name="customer")
    approval_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    provider_rating = models.IntegerField(blank=True, null=True)
    customer_rating = models.IntegerField(blank=True, null=True)
