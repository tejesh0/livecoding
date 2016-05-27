from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Geo
# Create your views here.
# import googlemaps
from geopy.geocoders import Nominatim


@csrf_exempt
def fetch_location(request):
    print "######"
    print request.method
    if request.method == 'POST':
        print(request.POST.get('address'))
        if request.POST.get('address'):
            geolocator = Nominatim()
            location = geolocator.geocode(request.POST.get('address'))
            print(location.address, location.latitude, location.longitude)
            Geo.objects.create(latitude=location.latitude, longitude=location.longitude, address=location.address)
        return HttpResponse("Check console for fetched address ")

    return render(request, 'geo_coding.html', context=None)
