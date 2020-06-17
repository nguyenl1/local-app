from django.shortcuts import render, redirect, get_object_or_404
# from .models import 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json
from .config import get_my_key

#define the api, endpoint, and header
API_KEY = get_my_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization':'bearer %s' % API_KEY}


def alamosquare (request):
    pass 

def bernalheights (request):
    pass 

def castro (request):
    pass 

def chinatown (request):
    pass 

def civiccenter (request):
    pass 

def colevalley (request):
    pass 

def diamondheights (request):
    pass 

def excelsior (request):
    pass 

def filmore (request):
    pass 

def financialdistrict (request):
    pass 

def forestHills (request):
    pass 

def forestknolls (request):
    pass 

def glenpark (request):
    pass 

def goldengate (request):
    pass 

def haightashbury (request):
    pass 

def hayesvalley (request):
    pass 

def bayview (request):
    pass 

def ingleside (request):
    pass 

def japantown (request):
    pass 

def lowerhaight (request):
    pass 

def marina (request):
    pass 

def miraloma (request):
    pass 

def mission (request):
    pass 

def neighborwoods (request):
    pass 

def nobhill (request):
    pass 

def noevalley (request):
    pass 

def northbeach (request):
    pass 

def oceanview (request):
    pass 

def outermission (request):
    pass 

def pacificheights (request):
    pass 

def parkmerced (request):
    pass 

def thepresidio (request):
    pass 

def portrerohill (request):
    pass 

def richmonddistrict (request):
    pass 

def russianhill (request):
    pass 

def soma (request):
    pass 

def sunsetdistrict (request):
    #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':2000,
        'latitude':37.752030, 
        'longitude': -122.485998,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/sunset.html', context=context)

def tenderloin (request):
    pass 

def twinpeaks (request):
    pass 

def unionsquare (request):
    pass 

def westportal (request):
    pass 

def westernaddition (request):
    pass 
