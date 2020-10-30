"""Game model module"""
from django.db import models

class Game(models.Model):

    """Game database module"""
    title = models.CharField(max_length=255)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    