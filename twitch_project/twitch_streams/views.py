from django.shortcuts import render
from .tasks import twitch_stream_users, twitch_channel_users
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from django.http import HttpResponseRedirect, HttpResponse
from .models import Streamer
import csv

DRIVE_FILENAME = 'Twitch_users'
# Create your views here.

gauth = None


def fetch_results_csv(request, q=None):
    if q is None:
        q = 'programming'
        twitch_stream_users()
        twitch_channel_users()
    else:
        twitch_stream_users(q)
        twitch_channel_users(q)

    print "QQQQQQQQQQQQQQQ"

    return HttpResponse('Done')


def convert_db_to_csv(request):
    """
    Download data in csv format
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Twitch_users.csv"'

    writer = csv.writer(response)
    all_streamers = Streamer.objects.all()
    writer.writerow(['name', 'channel_id', 'status'])
    for streamer in all_streamers:
        writer.writerow([streamer.name.encode('utf-8', 'ignore'), streamer.channel_id,
                         streamer.status.encode('utf-8', 'ignore')])
    return response


def google_oath_client_sdk(request):
    """
     Ask google drive write access permission
     using consent screen in new tab
    """
    gauth = GoogleAuth()
    gauth_url = gauth.Auth()

    return HttpResponseRedirect(gauth_url)


def google_redirect_uri_view(request):

    drive = GoogleDrive(gauth)

    csv_file = drive.CreateFile({'title': DRIVE_FILENAME + '.csv', 'mimeType': 'text/csv'})
    csv_file.SetContentFile(DRIVE_FILENAME + '.csv')
    csv_file.Upload()

    return HttpResponse('File saved to Google Drive successfully')
