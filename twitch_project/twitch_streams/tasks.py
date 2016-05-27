import urllib2
import json
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from .models import Streamer

logger = get_task_logger(__name__)


def twitch_stream_users(q=None):
    if q is None:
        q = 'programming'
    offset = 0
    limit = 100
    stream_type = ''

    source = urllib2.urlopen("https://api.twitch.tv/kraken/search/streams" + "?q=" + q +
                             '&limit=' + str(limit) + '&offset=' + str(offset) + '&stream_type=' + stream_type)

    json_res = json.load(source)

    prev_streamers = []

    streamers = Streamer.objects.all()
    for streamer in streamers:
        prev_streamers.append(streamer.name)

    # get total streamers to iterate over results
    source_total = urllib2.urlopen("https://api.twitch.tv/kraken/search/streams" + "?q=" + q)
    json_res_total = json.load(source_total)
    total_streamers = json_res_total['_total']

    for i in range(-1, total_streamers / limit):
        source = urllib2.urlopen("https://api.twitch.tv/kraken/search/streams" + "?q=" + q +
                                 '&limit=' + str(limit) + '&offset=' + str(offset) + '&stream_type=' + stream_type)
        json_res = json.load(source)
        offset = offset + 1

        for r in json_res['streams']:
            if r['channel']['name'] not in prev_streamers:
                Streamer.objects.create(name=r['channel']['name'], channel_id=r[
                    'channel']['_id'], status=r['channel']['status'])


def twitch_channel_users(q=None):
    if q is None:
        q = 'programming'

    offset = 0
    limit = 100
    stream_type = ''

    source = urllib2.urlopen("https://api.twitch.tv/kraken/search/channels" + "?q=" + q +
                             '&limit=' + str(limit) + '&offset=' + str(offset) + '&stream_type=' + stream_type)

    json_res = json.load(source)

    prev_streamers = []

    streamers = Streamer.objects.all()
    for streamer in streamers:
        prev_streamers.append(streamer.name)


    # get total streamers to iterate over results
    source_total = urllib2.urlopen("https://api.twitch.tv/kraken/search/channels" + "?q=" + q)
    json_res_total = json.load(source_total)
    total_streamers = json_res_total['_total']

    for i in range(-1, total_streamers / limit):
        source = urllib2.urlopen("https://api.twitch.tv/kraken/search/channels" + "?q=" + q +
                                 '&limit=' + str(limit) + '&offset=' + str(offset) + '&stream_type=' + stream_type)
        json_res = json.load(source)
        offset = offset + 1

        for r in json_res['channels']:
            if r['name'] not in prev_streamers:
                Streamer.objects.create(name=r['name'], channel_id=r['_id'], status=r['status'])


@periodic_task(
    run_every=(crontab()),
    name="fetch_users_from_twitch_stream",
    ignore_result=True
)
def fetch_users_from_twitch_stream(q=None):
    twitch_stream_users(q)

    logger.info("Saved streaming users to Database")


@periodic_task(
    run_every=(crontab()),
    name="fetch_users_from_twitch_channels",
    ignore_result=True
)
def fetch_users_from_twitch_channels(q=None):
    twitch_channel_users(q)
    logger.info("Saved streaming channels to Database")
