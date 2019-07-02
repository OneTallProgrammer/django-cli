from django.db import models
from django.utils import timezone
from django.conf import settings

class Command(models.Model):
    cmd = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def write(self):
        self.timestamp = timezone.now()
        self.save()

    def __str__(self):
        return self.cmd
