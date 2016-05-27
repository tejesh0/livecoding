from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# import googlemaps
from geopy.geocoders import Nominatim


def fetch_location(request):
    if request.method == 'POST':
        print(request.POST.get('address'))
        if request.POST.get('address'):
            geolocator = Nominatim()
            location = geolocator.geocode(request.POST.get('address'))
            print(location.address, location.latitude, location.longitude)
        return HttpResponse("Check console for fetched address ")

    return render(request, 'geo_coding.html', context=None)
