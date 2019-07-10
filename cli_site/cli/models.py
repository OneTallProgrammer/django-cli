from django.db import models
from django.utils import timezone
from django.conf import settings

class Agent(models.Model):
    agent_name = models.CharField(max_length=200)
    agent_type = models.IntegerField()

    def __str__(self):
        return self.agent_name

class Command(models.Model):
    cmd = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def write(self):
        self.timestamp = timezone.now()
        self.save()

    def __str__(self):
        return self.cmd
