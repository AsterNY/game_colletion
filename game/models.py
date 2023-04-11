from django.db import models

class Game(models.Model):
    rank = models.PositiveIntegerField()
    bgg_url = models.URLField()
    game_id = models.PositiveIntegerField(unique=True)
    names = models.CharField(max_length=255)
    min_players = models.PositiveIntegerField()
    max_players = models.PositiveIntegerField()
    avg_time = models.PositiveIntegerField()
    min_time = models.PositiveIntegerField()
    max_time = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    avg_rating = models.FloatField()
    geek_rating = models.FloatField()
    num_votes = models.PositiveIntegerField()
    image_url = models.URLField()
    age = models.PositiveIntegerField()
    mechanic = models.TextField()
    owned = models.PositiveIntegerField()
    category = models.TextField()
    designer = models.CharField(max_length=255)
    weight = models.FloatField()

    class Meta:
        db_table = 'game'