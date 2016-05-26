from django.conf.urls import url
from twitter_bot import views

urlpatterns = [
    # url(r'^$', views.fetch_user_token),
    url(r'^test$', views.test_tweept_api),
    url(r'^tweet-streamers$', views.tweet_current_streams),
    # url(r'^group/(?P<group_id>[\d]+)$', views.fetch_facebook_group_members),
]
