from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    search_history = models.ForeignKey('movies.Movie' , on_delete=models.CASCADE)
