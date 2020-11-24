"""Event model module"""
from django.db import models

class Event(models.Model):

    """Event database module"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="registrations")
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    description = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=6)
