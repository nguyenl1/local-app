from django.shortcuts import render, redirect, get_object_or_404
# from .models import 
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
        
    