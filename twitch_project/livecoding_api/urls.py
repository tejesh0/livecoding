from django.conf.urls import url
from twitter_bot import views

urlpatterns = [
    url(r'^livecoding/oath$', views.livecoding_oath),
    url(r'^livecoding-redirect$', views.livecoding_redirect_view),
    url(r'^tweet-streamers$', views.tweet_current_streams),
]
