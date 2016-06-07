from django.contrib import admin

# Register your models here.
from .models import LivecodingHandle, KeywordSearchSuggest, Credentials, FollowFollowersOfAccount


class LivecodingHandleAdmin(admin.ModelAdmin):
    # fields = ('name', 'channel_id', 'status')
    list_display = ('keyword', 'minimum_retweets', 'minimum_likes')


class KeywordSearchSuggestAdmin(admin.ModelAdmin):
    list_display = ('include_words', 'exclude_words', 'minimum_retweets', 'minimum_likes')


class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'access_token_secret', 'consumer_secret', 'consumer_key')


class FollowFollowersOfAccountAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'is_accounts_followed')


admin.site.register(LivecodingHandle, LivecodingHandleAdmin)
admin.site.register(KeywordSearchSuggest, KeywordSearchSuggestAdmin)
admin.site.register(Credentials, CredentialsAdmin)
admin.site.register(FollowFollowersOfAccount, FollowFollowersOfAccountAdmin)
