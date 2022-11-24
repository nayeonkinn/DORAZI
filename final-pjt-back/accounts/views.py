from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer, MovieSerializer, ProfileSerializer, UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = user.article_set.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_wishes(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    wishes = user.wish_movies.all()
    serializer = MovieSerializer(wishes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
            'is_followed': is_followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count()
        }
        return JsonResponse(context, status=status.HTTP_200_OK)


class SearchView(generics.ListCreateAPIView):
    search_fields = ['username', ]
    filter_backends = (filters.SearchFilter,)
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    movies = user.search_movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_friend(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    articles = serializer.data["articles_list"]
    seen = []
    for article in articles:
        seen.append(article["movie"]["id"])
    seen = list(set(seen))
    followers = serializer.data["followings"]
    result = []
    for follower in followers:
        you = get_object_or_404(get_user_model(), pk=follower)
        you_serializer = ProfileSerializer(you)
        articles = you_serializer.data["articles_list"]
        for article in articles:
            if article["movie"]["id"] in seen:
                continue
            result.append(article["movie"])
    return Response(result, status=status.HTTP_200_OK)
