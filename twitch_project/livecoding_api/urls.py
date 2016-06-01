from django.conf.urls import url
from livecoding_api import views

urlpatterns = [
    url(r'^oath$', views.livecoding_oath),
    url(r'^redirect$', views.livecoding_redirect_view),
    url(r'^api/scheduledbroadcast/$', views.fetch_schedules),
]
