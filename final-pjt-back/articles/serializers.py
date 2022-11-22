from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article, ArticleComment
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'poster_path',)

class UserExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
    

class ArticleExampleSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    user = UserExampleSerializer()
    movie = MovieSerializer()
    
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    hot_article = ArticleExampleSerializer(read_only=True, many=True, source='article_set')
    followers = UserExampleSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'
        # fields = ('id', 'username')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['hot_article'] = sorted(response['hot_article'], key=lambda x: -x['like_count'])[:1]
        return response

class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class ChildCommentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = ArticleComment
        fields = '__all__'


class ArticleCommentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    child_comment = ChildCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('article', 'like_users', 'parent_comment')



class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    like_users = SimpleUserSerializer(many=True, read_only=True)
    articlecomment_set = ArticleCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('like_users',)



