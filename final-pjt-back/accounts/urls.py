from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('delete/', views.delete, name='delete'),
    path('newenter/<int:movie_pk>/', views.search_add, name='search_add'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/articles/', views.profile_articles, name='profile_articles'),
    path('<str:username>/wishes/', views.profile_wishes, name='profile_wishes'),
    path('<str:username>/follow/', views.follow, name='follow'),
]
