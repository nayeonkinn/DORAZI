from django.db import models
from django.conf import settings

class Movie(models.Model):
    movie_code = models.IntegerField()
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    genre_ids = models.CharField(null=True, max_length=300)
    release_date = models.DateField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField(null = True)
    backdrop_path = models.TextField(null = True)
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    vote_average = models.FloatField(null=True)
    search_history = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='search_movies')


    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_code = models.IntegerField()
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
