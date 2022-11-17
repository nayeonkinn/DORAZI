from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleSerializer, ArticleCommentSerializer
from .models import Article, ArticleComment

# Create your views here.
def create(request, pk):
    pass

def detail(request, pk):
    pass

def like(request, pk):
    pass

def comment_list(request, pk):
    pass

def comment_create(request, pk):
    pass

def comment_detail(request, ariticle_pk, comment_pk):
    pass

def comment_like(request, ariticle_pk, comment_pk):
    pass

def search(request, keyword):
    pass