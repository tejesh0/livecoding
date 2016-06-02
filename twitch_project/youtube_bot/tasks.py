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
    search_response = youtube.search().list(
        q=options['q'],
        type="video",
        # location=options.location,
        # locationRadius=options.location_radius,
        part="id,snippet",
        # maxResults=options.max_results
    ).execute()

    search_videos = []

    # Merge video ids
    for search_result in search_response.get("items", []):
        search_videos.append(search_result["id"]["videoId"])
    video_ids = ",".join(search_videos)

    print(video_ids)

    # Call the videos.list method to retrieve location details for each video.
    video_response = youtube.videos().list(
        id=video_ids,
        part='snippet, recordingDetails'
    ).execute()

    videos = []

    # Add each result to the list, and then display the list of matching videos.
    for video_result in video_response.get("items", []):
        videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"]
                                       # video_result["recordingDetails"]["location"]["latitude"],
                                       # video_result["recordingDetails"]["location"]["longitude"]
                                       ))

    print "Videos:\n", "\n".join(videos), "\n"


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="fetch_youtube_search_results",
    ignore_result=True
)
def fetch_search_results():
    print("####################################3")
    # search_objects = YoutubeSearchTerm.objects.all()

    # argparser.add_argument("--q", help="Search term", default="Google")
    # argparser.add_argument("--location", help="Location", default="37.42307,-122.08427")
    # argparser.add_argument("--location-radius", help="Location radius", default="5km")
    # argparser.add_argument("--max-results", help="Max results", default=25)
    # args = argparser.parse_args()

    # for search_term in search_objects:
    try:
        youtube_search({'q': 'programming'})
        # logger.info("Saved " + search_term + " datap to Database")
    except HttpError, e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    logger.info("Saved streaming users to Database")
