from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *
# Create your views here.


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
