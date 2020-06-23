from django.shortcuts import render, redirect, get_object_or_404
from .models import SavedPins
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json
from .config import get_my_key

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

    return render(request,'local_app/location_details.html', context=context)

def my_pins(request):
    pins = SavedPins.objects.filter(user=request.user)
    context = {
        'pins':pins,
    }
    return render(request, 'local_app/mypins.html', context)

def save_pins(request,id):
    api_key = get_my_key()
    endpoint = f"https://api.yelp.com/v3/businesses/{id}"
    headers = {'Authorization':'bearer %s' % api_key}

    response = requests.get(url = endpoint, headers= headers)

    business_data = json.loads(response.text)

    if request.method == 'POST':
        save = SavedPins(request.POST)
        bus_id = save.bus_id = business_data['id']
        name = save.name = business_data['name']
        address = save.address = business_data['location']
        user = save.user = request.user

        SavedPins.objects.create(bus_id=bus_id, name=name, address=address, user=user)
        
        return redirect("my_pins")
    return render(request,"local_app/location_details.html")


def add_trip(request,id):
    pass 