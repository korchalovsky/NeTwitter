from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delite()
        return Response(status=status.HTTP_200_OK)


class ArticleRetrieveView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ProfileRetrieveView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


