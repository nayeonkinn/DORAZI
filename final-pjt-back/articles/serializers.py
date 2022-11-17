from .models import Article, ArticleComment
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','movie','like_users')


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('user','article','like_users','parent_comment')



