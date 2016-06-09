from django.contrib import admin

# Register your models here.
from .models import YoutubeSearchFilters, YoutubeData


class YoutubeSearchFiltersAdmin(admin.ModelAdmin):
    list_display = ('search_term', 'order')


class YoutubeDataAdmin(admin.ModelAdmin):
    list_display = ('is_already_reviewed', 'comment_count', 'view_count', 'video_count', 'subscriber_count',
                    'google_plus_user_Id', 'description', 'title', 'channel_id', 'country')


admin.site.register(YoutubeSearchFilters, YoutubeSearchFiltersAdmin)
admin.site.register(YoutubeData, YoutubeDataAdmin)
