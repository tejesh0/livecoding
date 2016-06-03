from django.contrib import admin

# Register your models here.
from .models import LivecodingHandle, KeywordSearchSuggest, Credentials


class LivecodingHandleAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('keyword',)


class KeywordSearchSuggestAdmin(admin.ModelAdmin):
    list_display = ('include_words', 'exclude_words')


class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'access_token_secret', 'consumer_secret', 'consumer_key')


admin.site.register(LivecodingHandle, LivecodingHandleAdmin)
admin.site.register(KeywordSearchSuggest, KeywordSearchSuggestAdmin)
admin.site.register(Credentials, CredentialsAdmin)
