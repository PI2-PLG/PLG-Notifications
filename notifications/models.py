from django.db import models
from django.utils import timezone

class Notification(models.Model):
    type = models.CharField(max_length=50, blank=False, default="")
    title = models.CharField(max_length=100, blank=False, default="")
    message = models.CharField(max_length=255, blank=False)
    module_name = models.CharField(max_length=100, blank=False, default="")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    velocity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ppm = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)