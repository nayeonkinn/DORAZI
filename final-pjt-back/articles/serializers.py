from .models import Article, ArticleComment
from rest_framework import serializers
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class ArticleSerializer(serializers.ModelSerializer):
    user2 = UserSerializer(read_only=True, source='user')

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'movie','like_users')


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('user','article','like_users','parent_comment')



