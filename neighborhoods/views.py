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
        #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def bernalheights (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1500,
        'latitude': 37.738995, 
        'longitude': -122.415454,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/bernalheights.html', context=context)
 

def castro (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.762592, 
        'longitude': -122.434194,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/castro.html', context=context)
 

def chinatown (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':400,
        'latitude': 37.794222, 
        'longitude': -122.407303,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/chinatown.html', context=context)
 

def civiccenter (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def colevalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def diamondheights (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def excelsior (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1500,
        'latitude': 37.726265, 
        'longitude': -122.419818

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/excelsior.html', context=context)
 

def filmore (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def financialdistrict (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def foresthills (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def forestknolls (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def glenpark (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def goldengate (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def haightashbury (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def hayesvalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def bayview (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def ingleside (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def japantown (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def lowerhaight (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def marina (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def miraloma (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def mission (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def neighborwoods (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def nobhill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def noevalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def northbeach (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def oceanview (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def outermission (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def pacificheights (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def parkmerced (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def thepresidio (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def portrerohill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def richmonddistrict (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def russianhill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def soma (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def sunsetdistrict (request):
    #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':48,
        'radius':2000,
        'latitude':37.752030, 
        'longitude': -122.485998,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses'],
        
    }

    return render(request,'neighborhoods/sunset.html', context=context)

def tenderloin (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def twinpeaks (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def unionsquare (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def westportal (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)
 

def westernaddition (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.777514,
        'longitude': -122.432802,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/alamosquare.html', context=context)

