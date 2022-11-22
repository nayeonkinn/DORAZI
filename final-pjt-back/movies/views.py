from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MovieSerializer, GenreSerializer, MovieListSerializer
from .models import Movie, Genre

# Create your views here.

@api_view(('GET',))
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    # 장르를 id 가 아닌, 한글로 return 하기 위해선 여기서 작성해야 하는가? 아니면 외부에서 따로 받아서 html에서 작업을 해야 하는가?
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('POST',))
def like(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('POST',))
def wish(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.wish_users.filter(pk=request.user.pk).exists():
            movie.wish_users.remove(request.user)
        else:
            movie.wish_users.add(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework import generics
from rest_framework import filters

class SearchView(generics.ListCreateAPIView):
    search_fields = ['title','original_title','genre_ids']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['POST'])
def search_add(request, pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=pk)
    if not(movie.search_history.filter(pk=user.pk).exists()):
        movie.search_history.add(user)
        print(movie.search_history)

    return Response(status=status.HTTP_200_OK)
