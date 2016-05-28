from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from .models import LivecodingHandle, KeywordSearchSuggest
from .views import api

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="like_and_retweet_livecoding_mentions",
    ignore_result=True
)
def like_and_retweet_livecoding_mentions():

    for result in LivecodingHandle.objects.all():
        search_results = api.search(q=result.keyword)

        data = []
        tweet_counter = 0
        for status in search_results:
            tweet_info = {}
            if not status.favorited and tweet_counter % 4 == 0:
                data.append(tweet_info)
                try:
                    api.create_favorite(status.id)
                except:
                    # rate limit exceeded
                    pass
            tweet_counter = tweet_counter + 1
        logger.info("liked and retweeted tweets consisting" + result.keyword + "term")


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="like_and_retweet_livecoding_mentions",
    ignore_result=True
)
def retweet_and_like_following_account_tweets():

    # get following accounts
    friends_ids = api.friends_ids(screen_name='tejesh95')

    retweet_count = 0
    for friend_id in friends_ids:
        # get tweets from past
        statuses = api.user_timeline(friend_id, count=4)
        for status in statuses:
            # check if tweet has 40 retweets
            if status._json['retweet_count'] > 40 and not status._json['retweeted']:
                try:
                    # TO DO confirm if retweeting intended tweet
                    api.retweet(status._json['id'])
                except:
                    # rate limit exceeded
                    pass
                retweet_count = retweet_count + 1
            # if tweet has 40 likes
            if status._json['favorite_count'] > 40 and not status._json['favorited']:
                try:
                    api.create_favorite(status._json['id'])
                except:
                    # rate limit exceeded
                    pass
    logger.info("liked and retweeted one in 4 tweets from following accounts tweets")


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="suggest_livecoding_by_keywords",
    ignore_result=True
)
def suggest_livecoding_by_keywords():
    keyword_objects = KeywordSearchSuggest.objects.all()

    for keyword in keyword_objects:

        q = keyword.include_words + ' -' + keyword.exclude_words
        search_results = api.search(q=q, count=50, result_type='recent')

        tweet_counter = 0

        for status in search_results:
            if not status.favorited and tweet_counter % 4 == 0:
                api.create_favorite(status.id)

            if not status.retweeted and tweet_counter % 3 == 0:
                api.retweet(status.id)

            tweet_counter += 1

        logger.info("suggest livecoding by keywords")
