import urllib2
import json
from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import GroupMember

logger = get_task_logger(__name__)


@task(name='fetch_members_from_group')
def fetch_members_from_group(members):
    def save_members_to_db(members):
        for member in members['data']:
            print member
            try:
                # the member may exist already in database
                # TO DO add group id they belong to
                GroupMember.objects.create(profile_id=member['id'], name=member[
                                           'name'], is_admin=member['administrator'])
            except:
                pass
        if members['paging']['next']:
            try:
                response = urllib2.urlopen(members['paging']['next']).read()
            except urllib2.URLError as e:
                print e.reason
            members = json.loads(response)
            save_members_to_db(members)

    save_members_to_db(members)
    logger.info("Saved streaming users to Database")
