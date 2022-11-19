from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer, MovieSerializer, ProfileSerializer


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def profile_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = user.article_set.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile_wishes(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    wishes = user.wish_movies.all()
    serializer = MovieSerializer(wishes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user
    you = get_object_or_404(get_user_model(), username=username)
    if you != me:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            'followers_count' : you.followers.count(),
            'followings_count' : you.followings.count()
        }
        return JsonResponse(context)
