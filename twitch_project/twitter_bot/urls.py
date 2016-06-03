from django.conf.urls import url
from twitter_bot import views

urlpatterns = [
    url(r'^engage$', views.retweet_and_like_following_account_tweets),
    url(r'^retweet-random$', views.retweet_and_like_random_account_tweets),
    url(r'^favorite$', views.like_livecoding_tweets),
]
