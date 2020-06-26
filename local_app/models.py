from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

class SavedPin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    bus_id = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    address = models.TextField(max_length = 2000)
    image = models.TextField(max_length=2000, blank=True)

class MyTrip(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    saved_pin = models.ForeignKey(SavedPin, on_delete=models.PROTECT, null=True)