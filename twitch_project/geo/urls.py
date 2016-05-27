from django.conf.urls import url
from geo import views

urlpatterns = [
    url(r'^$', views.fetch_location),
]
