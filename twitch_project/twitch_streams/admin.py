from django.contrib import admin

# Register your models here.
from .models import Streamer


class StreamerAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('name', 'channel_id', 'status')

admin.site.register(Streamer, StreamerAdmin)
