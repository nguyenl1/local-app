import config

from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
leaflet = Twython(config.leaflet)