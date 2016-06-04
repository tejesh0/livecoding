from celery.decorators import task
from celery.utils.log import get_task_logger
# from .models import YoutubeSearchTerm, YoutbubeData
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
        maxResults=2
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

        print(channel_response['items'])
        for response in channel_response['items']:
            print(response)
            print(response['statistics']['commentCount'], response['statistics']['viewCount'], response['statistics']['videoCount'], response['statistics']['subscriberCount'])
            print('Google plus user id : ', response['contentDetails']['googlePlusUserId'])
            print(response['snippet']['description'], response['snippet']['title'])
        print("===============================================")


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="fetch_youtube_search_results",
    ignore_result=True
)
def fetch_search_results():
    print("inside youtube task")

    try:
        # TO DO search keywords must be fetched from Database
        youtube_search({'q': 'programming lessons'})
        # logger.info("Saved " + search_term + " datap to Database")
    except HttpError, e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    logger.info("Saved youtube channels to Database")
