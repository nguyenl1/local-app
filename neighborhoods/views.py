from django.shortcuts import render, redirect, get_object_or_404
# from .models import 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json
from .config import get_my_key
from django.core.paginator import Paginator

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
        'latitude': 37.779439, 
        'longitude': -122.418100,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/civiccenter.html', context=context)
 

def colevalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':400,
        'latitude': 37.765880,
        'longitude': -122.449944,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/colevalley.html', context=context)
 

def diamondheights (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.742692, 
        'longitude': -122.441789,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/diamondheights.html', context=context)
 

def excelsior (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.725695, 
        'longitude': -122.421417,

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
        'radius':800,
        'latitude': 37.780981,
        'longitude': -122.428956

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/filmore.html', context=context)
 

def financialdistrict (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':400,
        'latitude': 37.794367, 
        'longitude': -122.401436,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/financialdistrict.html', context=context)
 

def foresthills (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':400,
        'latitude': 37.747934,
        'longitude': -122.464413,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/foresthills.html', context=context)
 

def forestknolls (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.758336, 
        'longitude': -122.457947,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/forestknolls.html', context=context)
 

def glenpark (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.737774, 
        'longitude': -122.431653,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/glenpark.html', context=context)
 

def goldengate (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.769376, 
        'longitude': -122.478405,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/goldengate.html', context=context)
 

def haightashbury (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.772538,
        'longitude':  -122.445892,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/haightashbury.html', context=context)
 

def hayesvalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.775154, 
        'longitude': -122.425161,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/hayesvalley.html', context=context)
 

def bayview (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.731062, 
        'longitude': -122.385524,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/bayview.html', context=context)
 

def ingleside (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.721254, 
        'longitude': -122.454165,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/ingleside.html', context=context)
 

def japantown (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.785741, 
        'longitude': -122.430525,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/japantown.html', context=context)
 

def lowerhaight (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.771866, 
        'longitude': -122.434065,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/lowerhaight.html', context=context)
 

def marina (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':600,
        'latitude': 37.803818, 
        'longitude': -122.437024,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/marina.html', context=context)
 

def miraloma (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':600,
        'latitude': 37.739274, 
        'longitude': -122.449636,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/miraloma.html', context=context)
 

def mission (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':750,
        'latitude': 37.758954,
        'longitude':  -122.415774,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/mission.html', context=context)
 

def neighborwoods (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.734321,
        'longitude':  -122.463429,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/neighborwoods.html', context=context)
 

def nobhill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':250,
        'latitude': 37.793062, 
        'longitude': -122.416112,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/nobhill.html', context=context)
 

def noevalley (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.749310,
        'longitude':  -122.433147,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/noevalley.html', context=context)
 

def northbeach (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.804390, 
        'longitude': -122.408304,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/northbeach.html', context=context)
 

def oceanview (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.717612, 
        'longitude': -122.459150,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/oceanview.html', context=context)
 

def outermission (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.725315, 
        'longitude': -122.441747,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/outermission.html', context=context)
 

def pacificheights (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.792462,
        'longitude':  -122.434437,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/pacificheights.html', context=context)
 

def parkmerced (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':750,
        'latitude': 37.720648, 
        'longitude': -122.486948,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/parkmerced.html', context=context)
 

def thepresidio (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.797867, 
        'longitude': -122.464513,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/thepresidio.html', context=context)
 

def portrerohill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':400,
        'latitude': 37.758435, 
        'longitude': -122.393235,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/portrerohill.html', context=context)
 

def richmonddistrict (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.780218,
        'longitude':  -122.482365,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/richmonddistrict.html', context=context)
 

def russianhill (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':500,
        'latitude': 37.801239, 
        'longitude': -122.417800,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/russianhill.html', context=context)
 

def soma (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':1000,
        'latitude': 37.778407, 
        'longitude': -122.396539,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/soma.html', context=context)
 

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
        'business_data':business_data['businesses'],
        
    }

    return render(request,'neighborhoods/sunset.html', context=context)

def tenderloin (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.784252, 
        'longitude': -122.414426,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/tenderloin.html', context=context)
 

def twinpeaks (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':200,
        'latitude': 37.751860, 
        'longitude': -122.449009,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/twinpeaks.html', context=context)
 

def unionsquare (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':200,
        'latitude': 37.787600, 
        'longitude': -122.406583,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/unionsquare.html', context=context)
 

def westportal (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':300,
        'latitude': 37.741321, 
        'longitude': -122.466598,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/westportal.html', context=context)
 

def westernaddition (request):
            #define the parameters
    PARAMETERS = {
        'term':'food',
        'limit':50,
        'radius':350,
        'latitude': 37.781568, 
        'longitude': -122.433332,

        }

    #make a request to the yelp API

    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers=HEADERS)

    #convert json string to a dictionary
    business_data = response.json()

    context = {
        'business_data':business_data['businesses']
    }

    return render(request,'neighborhoods/westernaddition.html', context=context)

