from django.conf.urls import url
from facebook_users import views

urlpatterns = [
    url(r'^$', views.fetch_user_token),
    url(r'^login_success$', views.redirect_uri_view),
    url(r'^group/(?P<group_id>[\d]+)$', views.fetch_facebook_group_members),
    url(r'^page$', views.fetch_facebook_page_fans),

]
