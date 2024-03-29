"""twitch_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from twitch_streams import views
# from django.apps import facebook_users

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.convert_db_to_csv),
    # url(r'^google/$', views.google_oath_client_sdk),
    url(r'^livecoding/', include('livecoding_api.urls')),
    url(r'^csv/$', views.fetch_results_csv),
    url(r'^facebook/', include('facebook_users.urls')),
    url(r'^twitter/', include('twitter_bot.urls')),
    url(r'^geo/', include('geo.urls')),
]
