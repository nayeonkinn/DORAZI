from rest_framework import serializers
from .models import Movie, Genre
from articles.models import Article
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username')

# class ArticleSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('user','movie','like_users')



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre_ids','release_date','poster_path',]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    articles_list = ArticleSerializer(source='article_set', many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['wish_users']
