from rest_framework import serializers
from .models import Movie, Genre
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','movie','like_users')


class MovieListSerializer(serializers.ModelSerializer):
    articles_list = ArticleSerializer(source='article_set', many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre_ids','release_date','poster_path', 'articles_list']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['like_users','wish_users']
