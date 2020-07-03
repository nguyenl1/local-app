from django.shortcuts import render, redirect, get_object_or_404
from .models import SavedPin, MyTrip
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json
from .config import get_my_key
import cloudinary
import cloudinary.uploader
import cloudinary.api

def home(request):
    return render(request, "local_app/index.html")

def location_details(request,id):
    api_key = get_my_key()
    endpoint = f"https://api.yelp.com/v3/businesses/{id}"
    headers = {'Authorization':'bearer %s' % api_key}

    response = requests.get(url = endpoint, headers= headers)

    business_data = json.loads(response.text)

    context = {
        'biz':business_data
    }

    return render(request,'local_app/location_details.html', context)

def my_pins(request):
    pins = SavedPin.objects.filter(user=request.user)

    trips = MyTrip.objects.filter(user=request.user)

    context = {
        'pins':pins,
        'trips':trips,
    }
    return render(request, 'local_app/mypins.html', context)

def save_pins(request,id):
    api_key = get_my_key()
    endpoint = f"https://api.yelp.com/v3/businesses/{id}"
    headers = {'Authorization':'bearer %s' % api_key}

    response = requests.get(url = endpoint, headers= headers)

    business_data = json.loads(response.text)

    location = business_data["location"]
    coordinates = business_data["coordinates"]
    photos = business_data["photos"]
    print(photos[0])


    if request.method == 'POST':
        save = SavedPin(request.POST)

        user = save.user = request.user
        bus_id = save.bus_id = business_data['id']
        name = save.name = business_data['name']
        address = save.address = location['address1']
        city = save.city = location['city']
        zip_code = save.zip_code = location ['zip_code']
        state = save.zip_code = location['state']
        image = save.image = business_data ['image_url']
        image_2 = save.image_2 = photos[1]
        image_3 = save.image_3 = photos[2]
        latitude = save.latitude = coordinates['latitude']
        longitude = save.longitude = coordinates['longitude']
        

        SavedPin.objects.create(bus_id=bus_id, name=name, address=address, image=image, image_2=image_2, image_3=image_3, user=user, city=city, zip_code=zip_code, state=state, latitude=latitude, longitude=longitude)
        
        return redirect(request.META['HTTP_REFERER'])
    return render(request,"local_app/location_details.html")


def add_trip(request,id):
    if request.method == "POST":
        save = MyTrip(request.POST)
        user = save.user = request.user
        saved_pin = SavedPin.objects.get(id=id)
        saved_pin.pk = None
        saved_pin.save()

        MyTrip.objects.create(user=user, saved_pin=saved_pin)
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'local_app/mytrips.html')

def my_trips(request):
    
    trips = MyTrip.objects.filter(user=request.user)

    context = {
        'trips':trips,
    }
    return render(request, 'local_app/mytrips.html', context) 

def remove_pins(request,id):
    remove = get_object_or_404(SavedPin, pk=id)
    remove.delete()
    return redirect("local_app:my_pins")

def remove_trip(request,id):
    remove = get_object_or_404(MyTrip, pk=id)
    remove.delete()
    return redirect("local_app:my_trips")

def my_dashboard(request):

    pins = SavedPin.objects.filter(user=request.user)

    trips = MyTrip.objects.filter(user=request.user)

    context = {
        'pins':pins,
        'trips':trips,
    }
    return render(request, 'local_app/dashboard.html', context)