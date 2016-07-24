from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    phone_number = models.IntegerField()
    biography = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

