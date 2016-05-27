from django.contrib import admin

# Register your models here.
from .models import LivecodingHandle, KeywordSearchSuggest


class LivecodingHandleAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('keyword',)


class KeywordSearchSuggestAdmin(admin.ModelAdmin):
    list_display = ('include_words', 'exclude_words')

admin.site.register(LivecodingHandle, LivecodingHandleAdmin)
admin.site.register(KeywordSearchSuggest, KeywordSearchSuggestAdmin)
