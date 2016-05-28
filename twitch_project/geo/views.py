from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Geo
# Create your views here.
# import googlemaps
from geopy.geocoders import Nominatim


@csrf_exempt
def fetch_location(request):
    if request.method == 'POST':
        if request.POST.get('address'):
            geolocator = Nominatim()
            try:
                location = geolocator.geocode(request.POST.get('address'))
            except:
                return HttpResponse('There is some problem decoding to lat long, Please try again!')
            Geo.objects.create(latitude=location.latitude, longitude=location.longitude, address=location.address)
        return HttpResponse("Check console for fetched address ")

    return render(request, 'geo_coding.html', context=None)
