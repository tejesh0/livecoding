from __future__ import absolute_import, print_function
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib2
import json
import tweepy

# Create your views here.
CONSUMER_KEY = 'OxcxPEtqcmDkXxKCWS2oZ0Yhh'
CONSUMER_SECRET = 'xJdCnVqfM1O6NROkEbQdmqVDslvIDp3OSTDMyhnrTj2PRzauua'
ACCESS_TOKEN = '2587698888-dtnflvcSem75KjKXFg8h7nwwNWNcQrbwm6xHMRT'
ACCESS_TOKEN_SECRET = 'RJZrL0TI6s9S9cPg09wgbZjNUBxzcLGVCspwazGU7Ss4L'

# https://www.livecoding.tv/developer/applications/137/
LIVECODING_KEY = 'Kn1zdoDZGRkcTQZW5NuA1CQ4nkjEYezmZ72knmRA'
LIVECODING_SECRET = '8kaCWGAWEFhUrh0vpW4oeQt2JdRehxQL3pNLAl9A3XFRlYTF0GxMvE5hcU9e2t8vHL4cBGTVOfmus5jAllwTh1CAzRS95mwI2F8I11c9xeFzAcXih4sPLiITCdUAisGz'
LIVECODING_REDIRECT_URI = 'http://localhost:5000' + '/twitter/livecoding-redirect'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def test_tweept_api(request):

    # If the authentication was successful, you should
    # see the name of the account print out
    print(api.me().name)

    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    # api.update_status(status='Updating using OAuth authentication via Tweepy!')

    return HttpResponse('Redirect successfully !')


def livecoding_oath(request):
    auth_end_point = 'https://www.livecoding.tv/o/authorize/?scope=read&state=' + LIVECODING_SECRET +'&redirect_uri='+ LIVECODING_REDIRECT_URI +'&response_type=code&client_id=' + LIVECODING_KEY
    print(auth_end_point)
    try:
        res = urllib2.urlopen(auth_end_point)
    except urllib2.URLError as e:
        print(e)
        return HttpResponse('livecoding authorisation failed!')
    print(res)
    return HttpResponseRedirect(res.read())


def livecoding_redirect_view(request):
    print(request.GET)

    return HttpResponse(' Fetched access token')


def tweet_current_streams(request):
    try:
        response = urllib2.urlopen('https://www.livecoding.tv/api/livestreams/?limit=10&offset=0')
        print(response)
        response = response.read()
    except urllib2.URLError as e:
        print(e)
        return HttpResponse('Try Agian')

    for streamer in response['results']:
        print(streamer)
        if streamer['is_live']:
            api.update_status(status='Watch out live : https://livecoding.tv/' + streamer['user__slug'])

    return HttpResponse('Current Streamers are tweet is made successfully !')


def suggest_livecoding_tweet(request):

    search_results = api.search(q="live programming", count=100, result_type='recent')

    for result in search_results[:10]:
        # print(result)
        print(result.author._json['screen_name'])
        try:
            api.update_status('Hey, you should checkout https://Livecoding.tv @'+result.author._json['screen_name'])
        except:
            return HttpResponse('Open after some time, no new results found to tweet')
    return HttpResponse('Suggested')
