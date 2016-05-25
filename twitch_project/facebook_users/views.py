from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .tasks import fetch_members_from_group
import urllib2
import json
# Create your views here.

APP_ID = '818991478245556'
APP_SECRET = '2579d3f1a38b7f0ab5ea9d8c8c4bdfa5'
VERSION = '2.6'
REDIRECT_URI = 'http://localhost:5000/facebook/login_success'
HOST = 'https://graph.facebook.com'
VERSION = 'v2.6'

# DO NOT use this access token, will automate fetching soon
access_token = 'EAALo3lAiiLQBACfDtgMkmDQiuZAzGjvpOBodrlWX5ctBq5yd9XKxSQNd2QMNHBCdc90uw5nYZBxW6LXXxKfirloZBJOweiJvDJAJbk2HqZAPvbcwZCkUEcIOhcgZBAt7XyOePJFVvNG0MGfTZC9otlPOB9G5LATRmsZD'


def fetch_user_token(request):
    """
    invoke the login dialog to ask user for access permissions
    """
    login_url = "https://www.facebook.com/dialog/oauth?client_id=" + APP_ID + "&redirect_uri=" + REDIRECT_URI

    return HttpResponseRedirect(login_url)


def redirect_uri_view(request):
    code = request.GET['code']
    exchange_code_url = "https://graph.facebook.com/v2.6/oauth/access_token?client_id=" + \
        APP_ID + "&redirect_uri=" + REDIRECT_URI + "&client_secret=" + APP_SECRET + "&code=" + code

    # response = urllib2.urlopen(exchange_code_url)
    return HttpResponseRedirect(exchange_code_url)


def search_groups(request, query=None):
    if query is None:
        return HttpResponse('Enter keywords to search for groups')
    return render(request, 'group_search.html', context=None)


def fetch_facebook_group_members(request, group_id=None):
    if group_id is None:
        return HttpResponse('Enter group_id Example: /facebook/group/123456789 ')

    api_end_point = HOST + '/' + VERSION + '/' + group_id + '/members' + '?access_token=' + access_token

    # TO DO run this as background task
    try:
        response = urllib2.urlopen(api_end_point).read()
    except urllib2.URLError as e:
        print e.reason
        return HttpResponseRedirect('/facebook/group/' + group_id)
    members = json.loads(response)

    # TO DO ---> PAGINATION
    fetch_members_from_group.delay(members)

    return HttpResponse('DONE')
