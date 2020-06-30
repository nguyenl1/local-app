import googlemaps
from datetime import datetime
from config import get_my_key
from django.apps import apps


mytrip = apps.get_model('local_app', 'MyTrip')
gmaps = googlemaps.Client(key= get_my_key())

print(mytrip.longitude)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((mytrip[1] , MyTrip.longitude))
# print (reverse_geocode_result)

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)