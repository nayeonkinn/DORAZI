from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles_list = []
    articles = user.article_set.all()
    for article in articles:
        article_json = {
            'movie_pk': article.movie.pk,
            'movie_title': article.movie.title,
            'movie_release_date': article.movie.release_date,
            'movie_poster_path': article.movie.poster_path,
            'article_pk': article.pk,
            'content': article.content,
            'spoiler': article.spoiler,
            'created_at': article.created_at,
            'likes_count': article.like_users.count()
        }
        articles_list.append(article_json)
    wishes_list = []
    wishes = user.wish_movies.all()
    for wish in wishes:
        wish_json = {
            'movie_pk': wish.pk,
            'movie_title': wish.title,
            'movie_release_date': wish.release_date,
            'movie_poster_path': wish.poster_path,
        }
        wishes_list.append(wish_json)
    context = {
        'username': user.username,
        'followers_count': user.followers.count(),
        'followings_count': user.followings.count(),
        'articles_count': user.article_set.count(),
        'articles_list': articles_list,
        'wishes_count': user.wish_movies.count(),
        'wishes_list': wishes_list,
    }
    return JsonResponse(context)


@api_view(['GET'])
def profile_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles_list = []
    articles = user.article_set.all()
    for article in articles:
        article_json = {
            'movie_pk': article.movie.pk,
            'movie_title': article.movie.title,
            'movie_release_date': article.movie.release_date,
            'movie_poster_path': article.movie.poster_path,
            'article_pk': article.pk,
            'content': article.content,
            'spoiler': article.spoiler,
            'created_at': article.created_at,
            'likes_count': article.like_users.count()
        }
        articles_list.append(article_json)
    context = {
        'username': user.username,
        'articles_list': articles_list,
    }
    return JsonResponse(context)


@api_view(['GET'])
def profile_wishes(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    wishes_list = []
    wishes = user.wish_movies.all()
    for wish in wishes:
        wish_json = {
            'movie_pk': wish.pk,
            'movie_title': wish.title,
            'movie_release_date': wish.release_date,
            'movie_poster_path': wish.poster_path,
        }
        wishes_list.append(wish_json)
    context = {
        'username': user.username,
        'wishes_list': wishes_list,
    }
    return JsonResponse(context)


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
