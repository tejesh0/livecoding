from __future__ import absolute_import, print_function
from django.shortcuts import render
from django.http import HttpResponse
from .models import Credentials
import tweepy

# Create your views here.
# CONSUMER_KEY = 'OxcxPEtqcmDkXxKCWS2oZ0Yhh'
# CONSUMER_SECRET = 'xJdCnVqfM1O6NROkEbQdmqVDslvIDp3OSTDMyhnrTj2PRzauua'
# ACCESS_TOKEN = '2587698888-dtnflvcSem75KjKXFg8h7nwwNWNcQrbwm6xHMRT'
# ACCESS_TOKEN_SECRET = 'RJZrL0TI6s9S9cPg09wgbZjNUBxzcLGVCspwazGU7Ss4L'

credentials = Credentials.objects.all()[0]
ACCESS_TOKEN = credentials.access_token
ACCESS_TOKEN_SECRET = credentials.access_token_secret
CONSUMER_SECRET = credentials.consumer_secret
CONSUMER_KEY = credentials.consumer_key
HOURS = 24
SCREEN_NAME = 'NowLivecodingtv'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

MIN_RETWEET_COUNT = 30
MIN_FAVORITE_COUNT = 40
RETWEET_LIMIT = 20  # per day

# TO DO create interface
# BLACKLISTED_WORDS = [word.rsplit() for word in open('black_listed_words.txt', 'r')]
BLACKLISTED_WORDS = ['penis', 'drugs', 'sex', 'race', 'kiss']


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
                if status.retweet_count > MIN_RETWEET_COUNT and not status.retweeted:
                    try:
                        # TO DO confirm if retweeting intended tweet
                        api.retweet(status.id)
                    except:
                        # rate limit exceeded
                        pass
                    retweet_count = retweet_count + 1
                # if tweet has 20 likes
                if status.favorite_count > MIN_FAVORITE_COUNT and not status.favorited:
                    try:
                        api.create_favorite(status.id)
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
                print("###", status.id)
                try:
                    api.retweet(status.id)
                except Exception, e:
                    print(e)

                retweet_count = retweet_count + 1
            # if tweet has 20 likes
            if status.favorite_count > 5 and not status.favorited:
                try:
                    api.create_favorite(status.id)
                except Exception, e:
                    print(e)


def retweet_and_like_random_account_tweets(request):
    if request.method == 'POST':
        print(request.POST.get('keyword'))
        if request.POST.get('keyword') is None:
            return render(request, 'retweet_and_like_random_account_tweets.html')
        else:
            search_query = request.POST.get('keyword')

        print(search_query)
        search_results = api.search(q=search_query, count=50, result_type='recent',
                                    geocode="37.0902, 95.7129, 10000mi")

        retweet_and_like(search_results)

        return render(request, 'retweet_and_like_random_account_tweets.html', context={'search_results': search_results})
    else:
        return render(request, 'retweet_and_like_random_account_tweets.html')


def like_livecoding_tweets(request):
    q = request.GET.get('q')
    if q is None:
        search_results = api.search(q='@livecodingtv')
    else:
        try:
            search_results = api.search(q=q)
        except Exception as e:
            print(e)

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


def follow_followers_of_given_accounts(request):
    """
        view to follow followers of account handles given in 
        FollowFollowersOfAccount model
    """

    followers_ids = api.followers_ids(screen_name='html5')

    print(followers_ids)

    for follower_id in followers_ids[5:7]:
        f = api.create_friendship(follower_id)
    

    return HttpResponse("Success")
