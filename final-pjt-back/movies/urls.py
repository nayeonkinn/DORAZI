from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/wish/', views.wish, name='wish'),
    path('search/', views.SearchView.as_view()),
    path('<int:pk>/enter/', views.search_add, name='search_add'),
]
