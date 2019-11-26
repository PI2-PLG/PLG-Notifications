from django.db import models
from django.utils import timezone

class Notification(models.Model):
    title = models.CharField(max_length=100, blank=False, default="")
    message = models.CharField(max_length=255, blank=False)
    module_name = models.CharField(max_length=100, blank=False, default="")
    date = models.DateTimeField(default=timezone.now)