from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count

from .serializers import ArticleSerializer, ArticleCommentSerializer, UserSerializer, ArticleExampleSerializer
from .models import Article, ArticleComment
from movies.models import Movie

from itertools import chain


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def articles_list(request):
    followings = request.user.followings.all()
    followings = chain(followings, [request.user])
    articles = get_list_or_404(Article.objects.order_by(
        '-created_at'), user__in=followings)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(('GET', 'PUT', 'DELETE'))
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    print(request.data)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        print(request.data)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        comments = get_list_or_404(ArticleComment, article=article)
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def child_comment_create(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(ArticleComment, pk=comment_pk)
    mention_to = None
    if comment.parent_comment:
        comment, mention_to = comment.parent_comment, comment.user.username
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user_id=request.user.id,
                        parent_comment=comment, mention_to=mention_to)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(('GET', 'PUT', 'DELETE'))
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(ArticleComment, pk=comment_pk)
    if request.method == 'GET':
        serializer = ArticleCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=comment.article)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def comment_like(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(ArticleComment, pk=comment_pk)
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
        serializer = ArticleCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchView(generics.ListCreateAPIView):
    search_fields = ['content',]
    filter_backends = (filters.SearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def recommend_friends(request):
    friends = get_list_or_404(get_user_model().objects.annotate(
        followers_count=Count('followers')).order_by('-followers_count'))
    serializer = UserSerializer(friends[:5], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def recommend_articles(request):
    articles = get_list_or_404(Article.objects.annotate(
        like_count=Count('like_users')).order_by('-like_count'))
    serializer = ArticleExampleSerializer(articles[:5], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
