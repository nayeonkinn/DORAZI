from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .serializers import ArticleSerializer, ArticleCommentSerializer
from movies.models import Movie
from .models import Article


@api_view(('GET',))
def articles_list(request):
    followings = request.user.followings.all()
    articles = get_list_or_404(Article.objects.order_by('-created_at'), user__in=followings)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(('POST',))
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    print(request.data)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(('GET','PUT','DELETE'))
def detail(request, article_pk):
    print(request.data)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('POST',))
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def comment_list(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        comments = get_list_or_404(ArticleComment, article=article)
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(('POST',))
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(('GET','PUT','DELETE'))
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(ArticleComment, pk=comment_pk)
    if request.method == 'GET':
        serializer = ArticleCommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=comment.article)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(('POST',))
def comment_like(request, article_pk, comment_pk):
     if request.user.is_authenticated:
        comment = get_object_or_404(ArticleComment, pk=comment_pk)
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
        serializer = ArticleCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import generics
from rest_framework import filters


class Searchlist(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Article.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset