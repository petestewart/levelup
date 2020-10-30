"""EventGuest model module"""
from django.db import models

class EventGuest(models.Model):

    """EventGuest database module"""
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)