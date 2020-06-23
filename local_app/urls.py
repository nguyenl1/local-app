from django.urls import path
from . import views
import requests
import json
from .config import get_my_key

# #define the api, endpoint, and header
# API_KEY = get_my_key()
# ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
# HEADERS = {'Authorization':'bearer %s' % API_KEY}

# PARAMETERS = {
#     'term':'food',
#     'location': 'San Francisco',
# }

# #make a request to the yelp APi

# response = requests.get(url = ENDPOINT, params= PARAMETERS, headers= HEADERS)

# #convert json string to a dictionary 

# business_data = response.json()

# a = business_data['businesses']

# slug = a[3] 



urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:id>/', views.location_details, name="location_details"),
]