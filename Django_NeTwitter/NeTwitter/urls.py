from django.urls import path, include

from .views import *

urlpatterns = [
    path('articles/all', ArticleListView.as_view()),
]