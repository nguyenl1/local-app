from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

class SavedPins(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    bus_id = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    address = models.TextField(max_length = 2000)