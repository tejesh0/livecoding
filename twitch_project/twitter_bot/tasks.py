from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from .models import LivecodingHandle, KeywordSearchSuggest
from .views import api, BLACKLISTED_WORDS

logger = get_task_logger(__name__)

PROGRAMMING_RELATED_WORDS = ['gist', 'programming', 'nodejs', '#python', 'coding', 'dev', 'github', 'html']


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="like_and_retweet_livecoding_mentions",
    ignore_result=True
)
def like_and_retweet_livecoding_mentions():

    for result in LivecodingHandle.objects.all():
        search_results = api.search(q=result.keyword, count=100,
                                    since_id=result.last_tweet_id)

        data = []
        tweet_counter = 0
        for status in search_results:
            tweet_info = {}
            flag = True
            for word in status.text.split(' '):
                if word in BLACKLISTED_WORDS:
                    flag = False
                    break
            if flag:
                if tweet_counter % 4 == 0:
                    data.append(tweet_info)
                    try:
                        api.create_favorite(status.id)
                        result.last_tweet_id = status.id
                        result.save()
                        logger.info('favorited tweet id : ' + status.id)
                    except Exception as e:
                        # rate limit exceeded
                        print(e)
                tweet_counter = tweet_counter + 1
        logger.info("liked and retweeted tweets consisting" + result.keyword + "term")


@periodic_task(
    run_every=(crontab(minute='*/60')),
    name="like_and_retweet_livecoding_mentions",
    ignore_result=True
)
def retweet_and_like_following_account_tweets():

    # get following accounts
    friends_ids = api.friends_ids(screen_name='livecodingtv')

    retweet_count = 0
    for friend_id in friends_ids:
        # get tweets from past
        statuses = api.user_timeline(friend_id, count=5)
        for status in statuses:
            # check if tweet has 40 retweets
            flag = True
            for word in status.text.split(' '):
                if word in BLACKLISTED_WORDS and word not in PROGRAMMING_RELATED_WORDS:
                    flag = False
                    break
            if flag:
                if status.retweet_count > 10:
                    try:
                        # TO DO confirm if retweeting intended tweet
                        api.retweet(status.id)
                        logger.info('retweeted tweet id : ' + status.id)
                    except Exception as e:
                        print(e)
                    retweet_count = retweet_count + 1
                # if tweet has 40 likes
                if status.favorite_count > 10:
                    try:
                        api.create_favorite(status.id)
                        logger.info('favorited tweet id : ' + status.id)
                    except Exception as e:
                        print(e)
    logger.info("liked and retweeted from following accounts tweets")


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="suggest_livecoding_by_keywords",
    ignore_result=True
)
def suggest_livecoding_by_keywords():
    keyword_objects = KeywordSearchSuggest.objects.all()

    for keyword in keyword_objects:
        if keyword.exclude_words:
            q = keyword.include_words + ' -' + keyword.exclude_words
        else:
            q = keyword.include_words
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(q)
        search_results = api.search(q=q, since_id=keyword.last_tweet_id, count=100,
                                    result_type='recent')
        print("#############LENGTH OF RESULTS", len(search_results))
        for status in search_results:

            flag = True
            for word in status.text.split(' '):
                if word in BLACKLISTED_WORDS:
                    flag = False
                    break
            if flag:
                print(status.favorite_count)
                if status.favorite_count >= keyword.minimum_likes:
                    try:
                        api.create_favorite(status.id)
                        logger.info('favorited tweet id : ' + status.id)
                    except Exception as e:
                        print(e)

                    keyword.last_tweet_id = status.id
                    keyword.save()

                if status.retweet_count >= keyword.minimum_retweets:
                    try:
                        api.retweet(status.id)
                        logger.info('retweeted tweet id : ' + status.id)
                    except Exception as e:
                        print(e)
                    keyword.last_tweet_id = status.id
                    keyword.save()

        logger.info("suggest livecoding by keywords")
