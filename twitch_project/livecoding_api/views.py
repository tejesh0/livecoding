from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
import json
import urllib2

# Create your views here.


# https://www.livecoding.tv/developer/applications/137/
LIVECODING_KEY = 'Kn1zdoDZGRkcTQZW5NuA1CQ4nkjEYezmZ72knmRA'
LIVECODING_SECRET = '8kaCWGAWEFhUrh0vpW4oeQt2JdRehxQL3pNLAl9A3XFRlYTF0GxMvE5hcU9e2t8vHL4cBGTVOfmus5jAllwTh1CAzRS95mwI2F8I11c9xeFzAcXih4sPLiITCdUAisGz'
LIVECODING_REDIRECT_URI = 'http://localhost:5000' + '/livecoding/redirect'
MY_CODE = 'qImSS03cdLm7CDeXDlZBoQ9ZL62bS8'

# {"access_token": "GAp8cjFJ0QfcU82ZvKmlE8BNZJjNoS",
# "token_type": "Bearer", "expires_in": 36000,
# "refresh_token": "pcyIJzc1HK1YJ0CXHqS1BJ45p83OOj", "scope": "read"}


def livecoding_oath(request):
    auth_end_point = 'https://www.livecoding.tv/o/authorize/?scope=read&state=' + '46c3c39d-512a-4bd0-8d59-63d7c9732180' + \
        '&redirect_uri=' + LIVECODING_REDIRECT_URI + '&response_type=code&client_id=' + LIVECODING_KEY
    print(auth_end_point)

    return HttpResponseRedirect(auth_end_point)


def livecoding_redirect_view(request):

    code = request.GET.get('code')
    if code is None:
        return HttpResponse("code param is empty/not found")
    try:
        url = "https://www.livecoding.tv/o/token/"
        data = dict(code=code, grant_type='authorization_code', redirect_uri=LIVECODING_REDIRECT_URI,
                    client_id=LIVECODING_KEY, client_secret=LIVECODING_SECRET)
        response = requests.post(url, data=data)
    except urllib2.URLError as e:
        print(e)
        return HttpResponse("Failed to make POST request to fetch token")

    return HttpResponse(response.content)


def fetch_schedules(request):
    access_token = livecoding_oath(request)
    print("################")
    print(access_token)
    print("#####################")
    try:
        headers = {"Authorization": "Bearer " + access_token}
        response = requests.get('https://www.livecoding.tv/api/scheduledbroadcast/?limit=5&offset=5', headers=headers)
        return HttpResponse(response.content)
    except urllib2.URLError as e:
        print(e)
        return HttpResponse('Try Agian')


def add_events_to_calendar(request):

    return render(request, 'add_events_to_calendar.html')
