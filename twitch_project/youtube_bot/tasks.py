from celery.utils.log import get_task_logger
from .models import YoutubeSearchFilters, YoutubeData
from apiclient.discovery import build
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from apiclient.errors import HttpError
logger = get_task_logger(__name__)

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
DEVELOPER_KEY = 'AIzaSyCv3VYLRXJdOk1KhsTMxcDLRfht-7jEzbQ'


def youtube_search(options):
    print(options)
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    # https://www.googleapis.com/youtube/v3/channels
    search_response = youtube.search().list(
        q=options['q'],
        type="channel",
        # location=options.location,
        # locationRadius=options.location_radius,
        order='date',
        part="id,snippet",
        maxResults=5
    ).execute()

    print(search_response['items'])

    for item in search_response['items']:
        # print(item)
        # print(item['snippet']['title'])
        # print(item['snippet']['channelId'])
        # print(item['snippet']['description'])

        channel_response = youtube.channels().list(
            part="snippet, statistics, contentDetails, id",
            id=item['snippet']['channelId'],
        ).execute()

        # print(channel_response['items'])
        for response in channel_response['items']:

            youtube_data = YoutubeData(channel_id=item['snippet']['channelId'])

            youtube_data.comment_count = response['statistics']['commentCount']
            youtube_data.view_count = response['statistics']['viewCount']
            youtube_data.video_count = response['statistics']['videoCount']
            youtube_data.subscriber_count = response['statistics']['subscriberCount']
            if 'googlePlusUserId' in response['contentDetails']:
                youtube_data.google_plus_user_Id = response['contentDetails']['googlePlusUserId']
            youtube_data.description = response['snippet']['description']
            if 'title' in response['snippet']:
                youtube_data.title = response['snippet']['title']
            if 'country' in response['snippet']:
                youtube_data.country = response['snippet']['country']
            try:
                youtube_data.save()
            except Exception as e:
                # channel already exists
                print(e)
            print("===============================================")


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="fetch_youtube_search_results",
    ignore_result=True
)
def fetch_search_results():
    print("inside youtube task")

    search_filters = YoutubeSearchFilters.objects.all()

    for search_filter in search_filters:
        try:
            # TO DO search keywords must be fetched from Database
            youtube_search({'q': search_filter.search_term})
            # logger.info("Saved " + search_term + " datap to Database")
        except HttpError, e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    logger.info("Saved youtube channels to Database")
