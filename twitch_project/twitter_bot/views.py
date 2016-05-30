from __future__ import absolute_import, print_function
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib2
import tweepy

# Create your views here.
# CONSUMER_KEY = 'OxcxPEtqcmDkXxKCWS2oZ0Yhh'
# CONSUMER_SECRET = 'xJdCnVqfM1O6NROkEbQdmqVDslvIDp3OSTDMyhnrTj2PRzauua'
# ACCESS_TOKEN = '2587698888-dtnflvcSem75KjKXFg8h7nwwNWNcQrbwm6xHMRT'
# ACCESS_TOKEN_SECRET = 'RJZrL0TI6s9S9cPg09wgbZjNUBxzcLGVCspwazGU7Ss4L'

ACCESS_TOKEN = "4415348663-Zuk3qz3CAQdsrdbcIyUe8UnIcFq3SvMrla9ooZV"
ACCESS_TOKEN_SECRET = "1StiYbP497HOzqXX0c8GVqxoZu0qNceAN0HHQPyCPZRXE"
CONSUMER_SECRET = "0Q2uAPUZ9Dny9SKeHFQ684eGJsI4ZMAP5htJ2Af91z2ygRIdx9"
CONSUMER_KEY = "ur9NcowJYOBXKgd45XPIFADmc"
HOURS = 24
SCREEN_NAME = 'NowLivecodingtv'

# https://www.livecoding.tv/developer/applications/137/
LIVECODING_KEY = 'Kn1zdoDZGRkcTQZW5NuA1CQ4nkjEYezmZ72knmRA'
LIVECODING_SECRET = '8kaCWGAWEFhUrh0vpW4oeQt2JdRehxQL3pNLAl9A3XFRlYTF0GxMvE5hcU9e2t8vHL4cBGTVOfmus5jAllwTh1CAzRS95mwI2F8I11c9xeFzAcXih4sPLiITCdUAisGz'
LIVECODING_REDIRECT_URI = 'http://localhost:5000' + '/twitter/livecoding-redirect'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

MIN_RETWEET_COUNT = 30
MIN_FAVORITE_COUNT = 40
RETWEET_LIMIT = 20  # per day

BLACKLISTED_WORDS = ['penis', 'drugs', 'sex', 'race', 'kiss']


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
    auth_end_point = 'https://www.livecoding.tv/o/authorize/?scope=read&state=' + LIVECODING_SECRET + \
        '&redirect_uri=' + LIVECODING_REDIRECT_URI + '&response_type=code&client_id=' + LIVECODING_KEY
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
        api.search()
        if streamer['is_live']:
            api.update_status(status='Watch out live : https://livecoding.tv/' + streamer['user__slug'])

    return HttpResponse('Current Streamers are tweet is made successfully !')


def suggest_livecoding_tweet(request):
    """
    Check for tweets with keywords like 'livestreaming code' 'live programming'
    but livecoding.tv missing
    and suggest Livecoding.tv to them.
    Hey! You should checkout Livecoding.tv ;)
    """
    # if q is not None:

    # TO DO If ('livestreaming code' in tweet) and ('live programming' in
    # tweet) and ('livecoding.tv/' not in tweet)
    # search_results = api.search(q="live programming", count=100, result_type='recent')

    # for result in search_results[:10]:
    #     # print(result)
    #     print(result.author._json['screen_name'])
    #     try:
    #         # api.update_status('Hey, you should checkout https://Livecoding.tv @' + result.author._json['screen_name'])
    #         # TO DO like and retweet the status
    #     except:
    #         return HttpResponse('Open after some time, no new results found to tweet')
    return HttpResponse('Suggested')


def retweet_and_like_following_account_tweets(request):

    # get following accounts
    friends_ids = api.friends_ids(screen_name=SCREEN_NAME)

    retweet_count = 0
    for friend_id in friends_ids:
        # get tweets from past
        statuses = api.user_timeline(friend_id, count=4)
        for status in statuses:
            # check if tweet has 10 retweets
            flag = True
            for word in status.text.split(' '):
                if word in BLACKLISTED_WORDS:
                    flag = False
                    break
            if flag:
                if status._json['retweet_count'] > MIN_RETWEET_COUNT and not status._json['retweeted']:
                    try:
                        # TO DO confirm if retweeting intended tweet
                        api.retweet(status._json['id'])
                    except:
                        # rate limit exceeded
                        pass
                    retweet_count = retweet_count + 1
                # if tweet has 20 likes
                if status._json['favorite_count'] > MIN_FAVORITE_COUNT and not status._json['favorited']:
                    try:
                        api.create_favorite(status._json['id'])
                    except:
                        # rate limit exceeded
                        pass

    return HttpResponse('Retweeted and liked the tweets of following accounts !')


def retweet_and_like(search_results):
    retweet_count = 0
    for status in search_results:
        flag = True
        for word in status.text.split(' '):
            if word in BLACKLISTED_WORDS:
                flag = False
                break
        if flag:
            print(status.retweet_count, status.retweeted, status.favorite_count, status.favorited)
            if status.retweet_count > 5 and not status.retweeted:
                # try:
                print("###", status.id, status)
                try:
                    api.retweet(status.id)
                except Exception, e:
                    print(e)

                print("####")
                # except:
                #     # rate limit exceeded
                #     pass
                retweet_count = retweet_count + 1
            # if tweet has 20 likes
            if status.favorite_count > 5 and not status.favorited:
                # try:
                api.create_favorite(status.id)
                # except:
                #     # rate limit exceeded
                #     pass


def retweet_and_like_random_account_tweets(request):
    if request.method == 'POST':
        print(request.POST.get('keyword'))
        if request.POST.get('keyword') is None:
            return render(request, 'retweet_and_like_random_account_tweets.html')
        else:
            search_query = request.POST.get('keyword')

        print(search_query)
        search_results = api.search(q=search_query, count=50, result_type='recent')

        retweet_and_like(search_results)

        return render(request, 'retweet_and_like_random_account_tweets.html', context={'search_results': search_results})
    else:
        return render(request, 'retweet_and_like_random_account_tweets.html')


def like_livecoding_tweets(request):
    search_results = api.search(q='@livecodingtv')

    data = []
    tweet_count = 0
    for status in search_results:
        tweet_info = {}
        flag = True
        for word in status.text.split(' '):
            if word in BLACKLISTED_WORDS:
                flag = False
                break
        if flag:
            # just making sure it is a tweet that had been liked by others (>4)
            if not status.favorited and tweet_count % 4 == 0:
                tweet_info['tweet_id'] = status.id
                tweet_info['favorites'] = status.favorite_count
                tweet_info['text'] = status.text
                tweet_info['url'] = 'https://twitter.com/statuses/' + str(status.id)
                data.append(tweet_info)
                try:
                    api.create_favorite(status.id)
                except:
                    # rate limit exceeded
                    pass
            tweet_count = tweet_count + 1
    return render(request, 'liked_livecoding_tweets.html', context={'favorited_tweets': data})
