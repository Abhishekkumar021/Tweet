from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create_tweet/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit_tweet/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete_tweet/', views.delete_tweet, name='delete_tweet'),
    path('register/', views.userRegistration, name='userRegistration'),
]