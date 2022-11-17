from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('create/<int:movie_pk>/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/like/',views.like, name='like'),
    path('<int:article_pk>/comment_list/', views.comment_list, name='comment_list'),
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:article_pk>/comment/<int:comment_pk>/like/', views.comment_like, name='comment_like'),
    path('search/<str:keyword>/',views.search, name='search'),
]
