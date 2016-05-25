from django.contrib import admin
from .models import GroupMember

# Register your models here.


class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'name', 'is_admin')

admin.site.register(GroupMember, GroupMemberAdmin)
