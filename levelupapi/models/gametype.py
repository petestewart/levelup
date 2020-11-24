"""GameType model module"""
from django.db import models

class GameType(models.Model):

    """GameType database module"""
    label = models.CharField(max_length=255)
    