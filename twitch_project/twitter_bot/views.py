from django.shortcuts import render
from django.http import HttpResponse
import urllib2
# import tweepy

# # Create your views here.
# CONSUMER_KEY = 'OxcxPEtqcmDkXxKCWS2oZ0Yhh'
# CONSUMER_SECRET = 'xJdCnVqfM1O6NROkEbQdmqVDslvIDp3OSTDMyhnrTj2PRzauua'
# ACCESS_TOKEN = '2587698888-dtnflvcSem75KjKXFg8h7nwwNWNcQrbwm6xHMRT'
# ACCESS_TOKEN_SECRET = 'RJZrL0TI6s9S9cPg09wgbZjNUBxzcLGVCspwazGU7Ss4L'


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.secure = True
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# def test_tweept_api(request):

#     # If the authentication was successful, you should
#     # see the name of the account print out
#     print(api.me().name)

#     # If the application settings are set for "Read and Write" then
#     # this line should tweet out the message to your account's
#     # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#     api.update_status(status='Updating using OAuth authentication via Tweepy!')

#     return HttpResponse('check TWITTER')


# def tweet_current_streams(request):
#     try:
#         response = urllib2.urlopen('https://www.livecoding.tv/api/livestreams/?limit=10&offset=0')
#         print response
#         response = response.read()
#     except urllib2.URLError as e:
#         print e
#         return HttpResponse('Try Agian')

#     for streamer in response['results']:
#         print streamer
#         if streamer['is_live']:
#             api.update_status(status='Watch out live : https://livecoding.tv/' + streamer['user__slug'])

#     return HttpResponse('Current Streamers are tweet is made successfully !')
