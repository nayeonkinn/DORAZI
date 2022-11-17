from rest_framework import serializers
from .models import Movie, Genre

class MovieListSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genres','release_date','poster_path']
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
