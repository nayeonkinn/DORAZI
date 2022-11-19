from ..Article.models import Article, ArticleComment
from rest_framework import serializers


class collection(serializers.ModelSerializer):

    class Meta:
        model = Article
