from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('articles/<int:pk>', ArticleRetrieveView.as_view()),
    path('articles/update/<int:pk>', ArticleUpdateView.as_view()),
    path('articles/new', ArticleCreateView.as_view()),
    path('articles/all', ArticleListView.as_view()),

    path('profile/update/<int:pk>', ProfileUpdateView.as_view()),
    path('profiles/<int:pk>', ProfileRetrieveView.as_view()),
    path('profiles/all', ProfileListView.as_view()),

]
