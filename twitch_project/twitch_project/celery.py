from __future__ import absolute_import
from celery import Celery
from django.conf import settings

import os
if not settings.configured:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'twitch_project.settings'

app = Celery('twitch_project', broker='redis://localhost')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
