from django.conf.urls import url
from twitter_bot import views

urlpatterns = [
    url(r'^livecoding/oath$', views.livecoding_oath),
    url(r'^livecoding-redirect$', views.livecoding_redirect_view),
    url(r'^tweet-streamers$', views.tweet_current_streams),
    url(r'^suggest$', views.suggest_livecoding_tweet),
    url(r'^engage$', views.retweet_and_like_following_account_tweets),
    url(r'^retweet-random$', views.retweet_and_like_random_account_tweets),
    url(r'^favorite$', views.like_livecoding_tweets),

]
