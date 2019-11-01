from django.db import models
from django.utils import timezone

class Notification(models.Model):
    token = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(default=timezone.now)