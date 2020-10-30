"""Event model module"""
from django.db import models

class Event(models.Model):

    """Event database module"""
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="registrations")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    location = models.CharField(max_length=50)
