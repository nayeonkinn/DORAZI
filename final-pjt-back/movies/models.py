from django.db import models
from django.conf import settings


class Movie(models.Model):
    movie_code = models.IntegerField()
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    genre_ids = models.JSONField(default=dict, null=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_code = models.IntegerField()
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
