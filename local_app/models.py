from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

class SavedPin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    bus_id = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200, blank=True)
    city = models.CharField(max_length = 200, blank=True)
    zip_code = models.CharField(max_length = 200, blank=True)
    state = models.CharField(max_length = 200, blank=True)
    image = models.TextField(max_length=2000, blank=True)
    latitude = models.TextField(max_length=2000, blank=True)
    longitude = models.TextField(max_length=2000, blank=True)

class MyTrip(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    saved_pin = models.ForeignKey(SavedPin, on_delete=models.PROTECT, null=True)