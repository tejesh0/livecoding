from django.contrib import admin

# Register your models here.
from .models import Geo


class GeoAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'address')

admin.site.register(Geo, GeoAdmin)
