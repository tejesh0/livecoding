from django.contrib import admin

# Register your models here.
from .models import Streamer, Profile


class StreamerAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('name', 'channel_id', 'status')


class ProfileAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('name', 'channel_id', 'status', 'views', 'followers', 'url',
                    'language', 'full_name', 'game', 'broadcaster_language', 'is_already_reviewed')

admin.site.register(Streamer, StreamerAdmin)
admin.site.register(Profile, ProfileAdmin)
